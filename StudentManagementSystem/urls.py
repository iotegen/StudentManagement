from django.contrib import admin
from django.urls import path, include

from StudentManagementSystem.views import AdminOnlyEndpoint, UserProfileListView, UserProfileDetailView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Student Management System API",
        default_version='v1',
        description="API documentation for Student Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('auth/', include('djoser.urls')),  # Authentication routes
    path('auth/', include('djoser.urls.jwt')),  # JWT token management
    path('students/', include('students.urls')),  # Student-specific routes
    path('courses/', include('courses.urls')),  # Course and enrollment routes
    path('grades/', include('grades.urls')),  # Grade-related routes
    path('attendance/', include('attendance.urls')),  # Attendance tracking routes
    path('user/', include('user.urls')),  # Add the new 'user' app URLs for assigning roles
    path('api/admin-only-endpoint/', AdminOnlyEndpoint.as_view(), name='admin-only-endpoint'),
    path('userprofile/', UserProfileListView.as_view(), name='userprofile-list'),  # List and create view
    path('userprofile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),  # Detail view
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
