from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

class APIRequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(auto_now=True)
    total_requests = models.IntegerField(default=0)

class CoursePopularity(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    access_count = models.IntegerField(default=0)
