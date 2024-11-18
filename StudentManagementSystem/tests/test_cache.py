from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import TestCase
from StudentManagementSystem.models import UserProfile

User = get_user_model()  # Dynamically get the correct user model

class UserProfileCacheTest(TestCase):
    def setUp(self):
        # Create a user and cache their profile
        self.user = User.objects.create(username="testuser", password="password")
        self.profile = UserProfile.objects.create(user=self.user, bio="Cached Bio")
        cache.set("user_profile", self.profile)

    def test_cache_fetch(self):
        # Fetch the cached profile and assert its bio is correct
        cached_profile = cache.get("user_profile")
        self.assertEqual(cached_profile.bio, "Cached Bio")
