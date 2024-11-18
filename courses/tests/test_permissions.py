from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User

class CoursePermissionTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.instructor = User.objects.create(username="instructor", password="password", is_staff=True)
        self.student = User.objects.create(username="student", password="password")

    def test_instructor_access(self):
        self.client.force_authenticate(user=self.instructor)
        response = self.client.post("/api/courses/", {"name": "Science 101", "description": "Basic Science"})
        self.assertEqual(response.status_code, 201)

    def test_student_access_denied(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.post("/api/courses/", {"name": "Science 101", "description": "Basic Science"})
        self.assertEqual(response.status_code, 403)
