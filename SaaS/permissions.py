from rest_framework import permissions

from assessments.models import AssessmentResult
from sean.models import ItemResult
from SaaS.models import SaaS, FeatureList

from datetime import datetime, timedelta

def current_week(option):
    current_date = datetime.now()
    if option == 'day':
        start_date = current_date
        end_date = current_date
    elif option == 'week':
        start_date = current_date - timedelta(days=current_date.weekday())
        end_date = start_date + timedelta(days=6)
    elif option == 'month':
        start_date = current_date.replace(day=1)
        end_date = (
            current_date.replace(day=1) + 
            timedelta(days=current_date.replace(day=1).monthrange()[1] - 1)
        )
    return start_date, end_date

class SaaSAccessPermissionAssessment(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = request.data.get('user', None)
        try:
            user_subcriptions = SaaS.objects.get(user__id=user_id)
        except SaaS.DoesNotExist:
            return False
        
        if user_subcriptions:
            if user_subcriptions.feature.name.lower() == 'premium':
                return True
            elif user_subcriptions.feature.name.lower() == 'free':
                feature = FeatureList.objects.get(name__icontains='assessment', feature=user_subcriptions.feature)
                if feature.frequency == 'unlimited':
                    return True
                start_date, end_date = current_week(feature.frequency)
                assessment_submitted = AssessmentResult.objects.filter(
                                        created_at__gte=start_date,
                                        created_at__lte=end_date,
                                        user=request.user
                                    )
                if assessment_submitted.count() < feature.times:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

class SaaSAccessPermissionItem(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user_subcriptions = SaaS.objects.get(user=request.user)
        except SaaS.DoesNotExist:
            return False
        
        if user_subcriptions:
            if user_subcriptions.feature.name.lower() == 'premium':
                return True
            elif user_subcriptions.feature.name.lower() == 'free':
                feature = FeatureList.objects.get(name__icontains='simulation', feature=user_subcriptions.feature)
                if feature.frequency == 'unlimited':
                    return True
                start_date, end_date = current_week(feature.frequency)
                item_submitted = ItemResult.objects.filter(
                                        created_at__gte=start_date,
                                        created_at__lte=end_date,
                                        user=request.user
                                    )
                if item_submitted.count() < feature.times:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
