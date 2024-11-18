from rest_framework.viewsets import ModelViewSet
from .models import APIRequestLog, UserActivity, CoursePopularity
from .serializers import APIRequestLogSerializer, UserActivitySerializer, CoursePopularitySerializer

class APIRequestLogViewSet(ModelViewSet):
    queryset = APIRequestLog.objects.all()
    serializer_class = APIRequestLogSerializer

class UserActivityViewSet(ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

class CoursePopularityViewSet(ModelViewSet):
    queryset = CoursePopularity.objects.all()
    serializer_class = CoursePopularitySerializer
