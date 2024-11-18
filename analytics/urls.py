from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import APIRequestLogViewSet, UserActivityViewSet, CoursePopularityViewSet

router = DefaultRouter()
router.register(r'api-logs', APIRequestLogViewSet)
router.register(r'user-activity', UserActivityViewSet)
router.register(r'course-popularity', CoursePopularityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
