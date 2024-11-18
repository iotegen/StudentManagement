from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollment, Course
from analytics.models import CoursePopularity
import logging

logger = logging.getLogger('app_logger')
def get(self, request, *args, **kwargs):
    course_id = kwargs.get('pk')  # Assuming Course Detail API uses `pk` as ID
    course = Course.objects.get(pk=course_id)

    # Increment course access count
    popularity, created = CoursePopularity.objects.get_or_create(course=course)
    popularity.access_count += 1
    popularity.save()

    return Response({"course": CourseSerializer(course).data})

class CourseListView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        # Log the list of courses
        logger.info(f"Course list accessed by {request.user.username}")
        return Response({"courses": [course.name for course in courses]})

class EnrollmentView(APIView):
    def post(self, request, *args, **kwargs):
        student = request.user.student_profile
        course_id = request.data.get('course_id')
        course = Course.objects.get(id=course_id)

        # Log the enrollment
        enrollment = Enrollment.objects.create(student=student, course=course)
        logger.info(f"Student {student.user.username} (ID: {student.user.id}) enrolled in course {course.name} (ID: {course.id})")

        return Response({"message": "Enrollment successful"}, status=status.HTTP_201_CREATED)
