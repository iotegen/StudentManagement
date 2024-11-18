# notifications/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from user.models import User

@shared_task
def send_daily_attendance_reminder():
    """
    Sends a reminder to students to mark their attendance.
    """
    today = timezone.now().date()
    students = User.objects.filter(is_active=True)

    for student in students:
        send_mail(
            subject="Attendance Reminder",
            message=f"Hi {student.username}, don't forget to mark your attendance today!",
            from_email="noreply@school.com",
            recipient_list=[student.email]
        )

@shared_task
def send_grade_update_notification(student_id, course_name, grade):
    """
    Sends an email notification when a grade is updated.
    """
    student = User.objects.get(id=student_id)
    send_mail(
        subject=f"Grade Update for {course_name}",
        message=f"Hi {student.username}, your grade for {course_name} has been updated to {grade}.",
        from_email="noreply@school.com",
        recipient_list=[student.email]
    )

@shared_task
def send_daily_report():
    """
    Generates and sends a daily report summarizing attendance and grades.
    """
    # This can be a complex task where you generate a report
    # and send it to the administrators or teachers.
    report = generate_attendance_and_grade_report()  # A function to generate the report.
    send_mail(
        subject="Daily Attendance and Grade Report",
        message=report,
        from_email="admin@school.com",
        recipient_list=["admin@school.com"]
    )
# notifications/tasks.py
@shared_task
def send_daily_attendance_reminder():
    """
    Sends a reminder to students to mark their attendance.
    """
    today = timezone.now().date()
    students = User.objects.filter(is_active=True)

    for student in students:
        send_mail(
            subject="Attendance Reminder",
            message=f"Hi {student.username}, don't forget to mark your attendance today!",
            from_email="noreply@school.com",
            recipient_list=[student.email]
        )

