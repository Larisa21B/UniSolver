from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class AuthTests(TestCase):
    def test_register_page_loads(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_user_can_register(self):
        response = self.client.post('/register/', {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_can_login(self):
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })

        self.assertEqual(response.status_code, 302)

class SkillAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='apiuser',
            password='test123'
        )

    def test_get_skills_requires_auth(self):
        response = self.client.get('/api/skills/')
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_access_skills(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/skills/')

        self.assertEqual(response.status_code, 200)