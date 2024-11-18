# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

class AdminOnlyEndpoint(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "This is an admin-only endpoint."}, status=status.HTTP_200_OK)


class UserProfileListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

