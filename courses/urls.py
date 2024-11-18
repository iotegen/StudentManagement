from django.urls import path
from .views import CourseListView, EnrollmentView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),  # View all courses
    path('enroll/', EnrollmentView.as_view(), name='course-enroll'),  # Enroll a student in a course
]
