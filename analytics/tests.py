from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import APIRequestLog, UserActivity, CoursePopularity
from courses.models import Course

User = get_user_model()

class AnalyticsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

    def test_api_request_logging(self):
        response = self.client.get('/some-api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(APIRequestLog.objects.count(), 1)

    def test_course_popularity(self):
        course = Course.objects.create(name="Test Course")
        response = self.client.get(f'/courses/{course.id}/')
        self.assertEqual(response.status_code, 200)
        popularity = CoursePopularity.objects.get(course=course)
        self.assertEqual(popularity.access_count, 1)
