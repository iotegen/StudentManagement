from django.urls import path
from .views import MarkAttendanceView

urlpatterns = [
    path('', MarkAttendanceView.as_view(), name='attendance-list'),
]
