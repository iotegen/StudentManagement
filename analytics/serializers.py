from rest_framework import serializers
from .models import APIRequestLog, UserActivity, CoursePopularity

class APIRequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIRequestLog
        fields = '__all__'

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'

class CoursePopularitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePopularity
        fields = '__all__'
