from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status  # Rename to avoid conflict
from .models import Attendance, Course
import logging

logger = logging.getLogger('app_logger')

class MarkAttendanceView(APIView):
    def post(self, request, *args, **kwargs):
        # Get the student from the user profile
        student = request.user.student_profile

        # Get course_id and status from request data
        course_id = request.data.get('course_id')
        attendance_status = request.data.get('status')  # Rename the variable to avoid conflict

        # Fetch the course object using the course_id
        course = Course.objects.get(id=course_id)

        # Create an attendance record
        attendance = Attendance.objects.create(student=student, course=course, status=attendance_status)

        # Log the attendance marking event
        logger.info(f"Attendance marked for {student.user.username} (ID: {student.user.id}) "
                    f"in course {course.name} (ID: {course.id}) as {attendance_status}")

        # Return a successful response
        return Response({"message": "Attendance marked"}, status=http_status.HTTP_200_OK)
