from django.db import models
from django.conf import settings  # Import the settings module

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def get_bio(self):
        return self.bio or "No bio available"

    def __str__(self):
        return self.user.username
