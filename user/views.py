# user/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .models import User  # Import the custom User model
from .permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
class AssignRoleView(APIView):
    permission_classes = [IsAdminUser]  # Only admin users can assign roles

    def post(self, request):
        # Get the user ID and the new role from the request data
        user_id = request.data.get('user_id')
        role = request.data.get('role')

        if not user_id or not role:
            return Response({"error": "Both 'user_id' and 'role' are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the user based on the provided user_id
            user = User.objects.get(id=user_id)

            # Check if the role is valid
            if role not in dict(User.ROLES):
                return Response({"error": "Invalid role provided."}, status=status.HTTP_400_BAD_REQUEST)

            # Update the user's role
            user.role = role
            user.save()

            return Response({"message": f"Role for {user.username} updated to {role}."}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            # Return an error if the user is not found
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
