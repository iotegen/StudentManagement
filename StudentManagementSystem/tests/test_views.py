from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from StudentManagementSystem.models import UserProfile

User = get_user_model()

class UserProfileViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)
        self.profile = UserProfile.objects.create(user=self.user, bio="Test Bio")

    def test_create_profile(self):
        url = reverse("userprofile-list")  # Correct URL name for the list view
        data = {"bio": "New Bio"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["bio"], "New Bio")

    def test_get_profile(self):
        url = reverse("userprofile-detail", kwargs={"pk": self.profile.id})  # Correct URL name for the detail view
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["bio"], "Test Bio")
