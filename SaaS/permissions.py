from rest_framework import permissions

from assessments.models import AssessmentResult

class SaaSAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)