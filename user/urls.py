from django.urls import path
from .views import AssignRoleView

urlpatterns = [
    path('', AssignRoleView.as_view(), name='assign-role'),
]
