import datetime
from .models import APIRequestLog, UserActivity

class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Log API Request
            APIRequestLog.objects.create(
                user=request.user,
                endpoint=request.path,
                method=request.method
            )

            # Update User Activity
            activity, created = UserActivity.objects.get_or_create(user=request.user)
            activity.last_activity = datetime.datetime.now()
            activity.total_requests += 1
            activity.save()

        return response
