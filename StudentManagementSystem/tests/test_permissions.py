from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model  # Dynamically fetch the user model
from rest_framework import status

class UserProfilePermissionTest(TestCase):
    def setUp(self):
        """
        This method runs before each test.
        We create two users: one admin and one regular user.
        """
        self.client = APIClient()
        User = get_user_model()  # Dynamically get the correct user model
        self.admin_user = User.objects.create(username="admin", password="password", is_staff=True)  # Admin user
        self.regular_user = User.objects.create(username="user", password="password")  # Regular user

    def test_admin_access(self):
        """
        Test that an admin user can access the admin-only endpoint.
        """
        self.client.force_authenticate(user=self.admin_user)  # Authenticate as admin
        response = self.client.get("/api/admin-only-endpoint/")  # Make request
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Admin should have access

    def test_regular_user_denied(self):
        """
        Test that a regular user is denied access to the admin-only endpoint.
        """
        self.client.force_authenticate(user=self.regular_user)  # Authenticate as regular user
        response = self.client.get("/api/admin-only-endpoint/")  # Make request
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Regular user should be denied access
