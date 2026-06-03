from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import AcademicProfile, Skill, AvailabilitySlot, SkillAvailability
from .serializers import (
    UserSerializer,
    AcademicProfileSerializer,
    SkillSerializer,
    AvailabilitySlotSerializer,
    RegisterSerializer
)

from tutoring.models import TutoringRequest, TutoringSession
from teams.models import ProjectTeam
from reviews.models import Review


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AcademicProfileViewSet(viewsets.ModelViewSet):
    queryset = AcademicProfile.objects.all()
    serializer_class = AcademicProfileSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class AvailabilitySlotViewSet(viewsets.ModelViewSet):
    queryset = AvailabilitySlot.objects.all()
    serializer_class = AvailabilitySlotSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            profile, created = AcademicProfile.objects.get_or_create(
                user=user,
                defaults={
                    'university': 'Nespecificat',
                    'specialization': 'Nespecificat',
                    'study_year': 1,
                    'role': 'student'
                }
            )

            if profile.role == 'student':
                return redirect('/student-dashboard/')
            if profile.role == 'tutor':
                return redirect('/tutor-dashboard/')
            if profile.role == 'admin':
                return redirect('/admin-dashboard/')

            return redirect('/dashboard/')

        return render(request, 'login.html', {
            'error': 'Username sau parola invalidă'
        })

    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if not username or not email or not password or not role:
            return render(request, 'register.html', {
                'error': 'Toate câmpurile sunt obligatorii'
            })

        if role not in ['student', 'tutor']:
            return render(request, 'register.html', {
                'error': 'Rol invalid'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username deja existent'
            })

        if len(password) < 6:
            return render(request, 'register.html', {
                'error': 'Parola trebuie să aibă minim 6 caractere'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        AcademicProfile.objects.create(
            user=user,
            university='Nespecificat',
            specialization='Nespecificat',
            study_year=1,
            role=role
        )

        return redirect('/login/')

    return render(request, 'register.html')


@login_required(login_url='/login/')
def dashboard_page(request):
    profile, created = AcademicProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'university': 'Nespecificat',
            'specialization': 'Nespecificat',
            'study_year': 1,
            'role': 'student'
        }
    )

    if profile.role == 'student':
        return redirect('/student-dashboard/')
    if profile.role == 'tutor':
        return redirect('/tutor-dashboard/')
    if profile.role == 'admin':
        return redirect('/admin-dashboard/')

    return render(request, 'dashboard.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def student_dashboard_page(request):
    return render(request, 'student_dashboard.html')


@login_required(login_url='/login/')
def tutor_dashboard_page(request):
    return render(request, 'tutor_dashboard.html')


@login_required(login_url='/login/')
def admin_dashboard_page(request):
    return render(request, 'admin_dashboard.html')


@login_required(login_url='/login/')
def tutors_page(request):
    subject = request.GET.get('subject', '')

    skills = Skill.objects.all()

    if subject:
        skills = skills.filter(subject=subject)

    return render(request, 'tutors.html', {
        'skills': skills,
        'subject': subject
    })


@login_required(login_url='/login/')
def tutor_profile_page(request, tutor_id):
    tutor = get_object_or_404(User, id=tutor_id)

    profile, created = AcademicProfile.objects.get_or_create(
        user=tutor,
        defaults={
            'university': 'Nespecificat',
            'specialization': 'Nespecificat',
            'study_year': 1,
            'role': 'tutor'
        }
    )

    skills = Skill.objects.filter(user=tutor)

    return render(request, 'tutor_profile.html', {
        'tutor': tutor,
        'profile': profile,
        'skills': skills
    })


@login_required(login_url='/login/')
def add_skill_page(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')

        dates = request.POST.getlist('available_date')
        start_times = request.POST.getlist('start_time')
        end_times = request.POST.getlist('end_time')

        if not subject or not dates or not start_times or not end_times:
            return render(request, 'add_skill.html', {
                'error': 'Alege materia și adaugă cel puțin o disponibilitate.'
            })

        skill = Skill.objects.create(
            user=request.user,
            subject=subject
        )

        for date, start, end in zip(dates, start_times, end_times):
            if date and start and end:
                SkillAvailability.objects.create(
                    skill=skill,
                    available_date=date,
                    start_time=start,
                    end_time=end
                )

        return redirect('/tutor-dashboard/')

    return render(request, 'add_skill.html')


@login_required(login_url='/login/')
def send_request_page(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    tutor = skill.user
    availabilities = SkillAvailability.objects.filter(skill=skill)

    if request.method == 'POST':
        message = request.POST.get('message')
        availability_id = request.POST.get('availability_id')
        requested_start_time = request.POST.get('requested_start_time')
        requested_end_time = request.POST.get('requested_end_time')

        if not message or not availability_id or not requested_start_time or not requested_end_time:
            return render(request, 'send_request.html', {
                'error': 'Alege data, ora de început, ora de sfârșit și completează mesajul.',
                'skill': skill,
                'tutor': tutor,
                'availabilities': availabilities
            })

        availability = get_object_or_404(
            SkillAvailability,
            id=availability_id,
            skill=skill
        )

        if requested_start_time < availability.start_time.strftime('%H:%M') or requested_end_time > availability.end_time.strftime('%H:%M'):
            return render(request, 'send_request.html', {
                'error': 'Intervalul ales trebuie să fie în intervalul disponibil al tutorelui.',
                'skill': skill,
                'tutor': tutor,
                'availabilities': availabilities
            })

        if requested_start_time >= requested_end_time:
            return render(request, 'send_request.html', {
                'error': 'Ora de început trebuie să fie înaintea orei de sfârșit.',
                'skill': skill,
                'tutor': tutor,
                'availabilities': availabilities
            })

        TutoringRequest.objects.create(
            student=request.user,
            tutor=tutor,
            subject=skill.subject,
            message=message,
            requested_date=availability.available_date,
            requested_start_time=requested_start_time,
            requested_end_time=requested_end_time
        )

        return redirect('/tutoring-requests/')

    return render(request, 'send_request.html', {
        'skill': skill,
        'tutor': tutor,
        'availabilities': availabilities
    })

@login_required(login_url='/login/')
def tutoring_requests_page(request):
    requests = TutoringRequest.objects.filter(
        student=request.user
    ).exclude(status='approved')

    return render(request, 'tutoring_requests.html', {
        'requests': requests
    })


@login_required(login_url='/login/')
def received_requests_page(request):
    requests = TutoringRequest.objects.filter(
        tutor=request.user,
        status='pending'
    )

    return render(request, 'received_requests.html', {
        'requests': requests
    })


@login_required(login_url='/login/')
def approve_request(request, request_id):
    tutoring_request = get_object_or_404(
        TutoringRequest,
        id=request_id,
        tutor=request.user,
        status='pending'
    )

    tutoring_request.status = 'approved'
    tutoring_request.save()

    TutoringSession.objects.create(
        student=tutoring_request.student,
        tutor=tutoring_request.tutor,
        subject=tutoring_request.subject,
        session_date=tutoring_request.requested_date,
        start_time=tutoring_request.requested_start_time,
        end_time=tutoring_request.requested_end_time
    )

    return redirect('/received-requests/')


@login_required(login_url='/login/')
def reject_request(request, request_id):
    tutoring_request = get_object_or_404(
        TutoringRequest,
        id=request_id,
        tutor=request.user,
        status='pending'
    )

    tutoring_request.status = 'rejected'
    tutoring_request.save()

    return redirect('/received-requests/')

@login_required(login_url='/login/')
def my_sessions_page(request):
    sessions = (
        TutoringSession.objects.filter(student=request.user) |
        TutoringSession.objects.filter(tutor=request.user)
    )

    sessions_data = []

    for session in sessions:
        sessions_data.append({
            'date': session.session_date.strftime('%Y-%m-%d'),
            'subject': session.subject,
            'student': session.student.username,
            'tutor': session.tutor.username,
            'start': session.start_time.strftime('%H:%M'),
            'end': session.end_time.strftime('%H:%M'),
            'status': session.status
        })

    return render(request, 'my_sessions.html', {
        'sessions_data': sessions_data
    })

@login_required(login_url='/login/')
def project_teams_page(request):
    teams = ProjectTeam.objects.all()

    return render(request, 'project_teams.html', {
        'teams': teams
    })


@login_required(login_url='/login/')
def create_team_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        if not title or not subject or not description:
            return render(request, 'create_team.html', {
                'error': 'Toate câmpurile sunt obligatorii'
            })

        ProjectTeam.objects.create(
            owner=request.user,
            title=title,
            subject=subject,
            description=description,
            status='open'
        )

        return redirect('/project-teams/')

    return render(request, 'create_team.html')


@login_required(login_url='/login/')
def reviews_page(request):
    reviews = Review.objects.all()

    return render(request, 'reviews.html', {
        'reviews': reviews
    })


@login_required(login_url='/login/')
def edit_profile_page(request):
    profile, created = AcademicProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'university': 'Nespecificat',
            'specialization': 'Nespecificat',
            'study_year': 1,
            'role': 'student'
        }
    )

    if request.method == 'POST':
        university = request.POST.get('university')
        specialization = request.POST.get('specialization')
        study_year = request.POST.get('study_year')
        bio = request.POST.get('bio')
        role = request.POST.get('role')

        if not university or not specialization or not study_year or not role:
            return render(request, 'edit_profile.html', {
                'profile': profile,
                'error': 'Toate câmpurile obligatorii trebuie completate'
            })

        profile.university = university
        profile.specialization = specialization
        profile.study_year = study_year
        profile.bio = bio
        profile.role = role
        profile.save()

        if role == 'student':
            return redirect('/student-dashboard/')
        if role == 'tutor':
            return redirect('/tutor-dashboard/')
        if role == 'admin':
            return redirect('/admin-dashboard/')

        return redirect('/dashboard/')

    return render(request, 'edit_profile.html', {
        'profile': profile
    })