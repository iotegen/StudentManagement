from django.db import models
from user.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    dob = models.DateField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
# students/models.py
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'present', 'absent'

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.status}"
