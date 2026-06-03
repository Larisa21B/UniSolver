from django.test import TestCase
from django.contrib.auth.models import User

from .models import TutoringRequest


class TutoringRequestTests(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='student',
            password='test123'
        )

        self.tutor = User.objects.create_user(
            username='tutor',
            password='test123'
        )

    def test_create_tutoring_request(self):
        request = TutoringRequest.objects.create(
            student=self.student,
            tutor=self.tutor,
            subject='Matematica',
            message='Am nevoie de ajutor'
        )

        self.assertEqual(request.subject, 'Matematica')
        self.assertEqual(request.status, 'pending')

    def test_tutoring_request_has_student(self):
        request = TutoringRequest.objects.create(
            student=self.student,
            tutor=self.tutor,
            subject='Python',
            message='Ajutor proiect'
        )

        self.assertEqual(request.student.username, 'student')

    def test_tutoring_request_has_tutor(self):
        request = TutoringRequest.objects.create(
            student=self.student,
            tutor=self.tutor,
            subject='SQL',
            message='Ajutor baze de date'
        )

        self.assertEqual(request.tutor.username, 'tutor')