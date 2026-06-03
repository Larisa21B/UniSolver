from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import (
    UserViewSet,
    AcademicProfileViewSet,
    SkillViewSet,
    AvailabilitySlotViewSet,
    RegisterView,

    login_page,
    register_page,
    dashboard_page,
    logout_page,

    student_dashboard_page,
    tutor_dashboard_page,
    admin_dashboard_page,

    tutors_page,
    tutor_profile_page,
    send_request_page,
    tutoring_requests_page,

    received_requests_page,
    approve_request,
    reject_request,

    project_teams_page,
    create_team_page,
    reviews_page,

    add_skill_page,
    edit_profile_page,
    my_sessions_page,
)

from tutoring.views import TutoringRequestViewSet
from teams.views import ProjectTeamViewSet, TeamMemberViewSet
from reviews.views import ReviewViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'academic-profiles', AcademicProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'availability-slots', AvailabilitySlotViewSet)
router.register(r'tutoring-requests', TutoringRequestViewSet, basename='tutoring-request')
router.register(r'project-teams', ProjectTeamViewSet)
router.register(r'team-members', TeamMemberViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),

    path('', login_page, name='home'),
    path('login/', login_page, name='login-page'),
    path('register/', register_page, name='register-page'),
    path('logout/', logout_page, name='logout-page'),

    path('dashboard/', dashboard_page, name='dashboard-page'),
    path('student-dashboard/', student_dashboard_page, name='student-dashboard'),
    path('tutor-dashboard/', tutor_dashboard_page, name='tutor-dashboard'),
    path('admin-dashboard/', admin_dashboard_page, name='admin-dashboard'),

    path('tutors/', tutors_page, name='tutors-page'),
    path('tutor-profile/<int:tutor_id>/', tutor_profile_page, name='tutor-profile'),
    path('send-request/<int:skill_id>/', send_request_page, name='send-request-page'),
    path('tutoring-requests/', tutoring_requests_page, name='tutoring-requests-page'),

    path('received-requests/', received_requests_page, name='received-requests'),
    path('approve-request/<int:request_id>/', approve_request, name='approve-request'),
    path('reject-request/<int:request_id>/', reject_request, name='reject-request'),

    path('project-teams/', project_teams_page, name='project-teams-page'),
    path('project-teams/create/', create_team_page, name='create-team-page'),

    path('reviews/', reviews_page, name='reviews-page'),

    path('add-skill/', add_skill_page, name='add-skill'),
    path('edit-profile/', edit_profile_page, name='edit-profile'),
    path('my-sessions/', my_sessions_page, name='my-sessions'),
]