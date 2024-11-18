from django.contrib.auth import get_user_model
from django.test import TestCase
from StudentManagementSystem.models import UserProfile

User = get_user_model()  # Dynamically get the correct user model

class UserProfileModelTest(TestCase):
    def setUp(self):
        # Use the dynamically imported User model
        self.user = User.objects.create(username="testuser", password="password")
        self.profile = UserProfile.objects.create(user=self.user, bio="Test Bio")

    def test_userprofile_creation(self):
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.bio, "Test Bio")
