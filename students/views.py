"""from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer

class StudentProfileView(RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.student_profile
"""
from django.core.cache import cache
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer

class StudentProfileView(RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cache_key = f"student_profile_{self.request.user.id}"
        student = cache.get(cache_key)
        if not student:
            student = self.request.user.student_profile
            cache.set(cache_key, student, timeout=600)  # Cache for 10 minutes
        return student

def perform_update(self, serializer):
    instance = serializer.save()
    cache_key = f"student_profile_{self.request.user.id}"
    cache.delete(cache_key)  # Clear the cache after updating the profile

