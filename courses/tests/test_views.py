from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import TestCase
from StudentManagementSystem.models import UserProfile
from django.urls import reverse  # Best practice to use reverse for URLs

User = get_user_model()  # Dynamically get the correct user model

class UserProfileViewTest(TestCase):
    def setUp(self):
        # Setup test client and create a user
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")  # Use create_user
        self.client.force_authenticate(user=self.user)
        self.profile = UserProfile.objects.create(user=self.user, bio="Test Bio")

    def test_create_profile(self):
        # Use reverse to avoid hardcoding URLs
        url = reverse("userprofile-list")  # Update this name to match your router or view name
        data = {"bio": "New Bio"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["bio"], "New Bio")

    def test_get_profile(self):
        # Use reverse to avoid hardcoding URLs
        url = reverse("userprofile-detail", kwargs={"pk": self.profile.id})  # Update this name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["bio"], "Test Bio")
