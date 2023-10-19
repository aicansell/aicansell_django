from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductView, WordsViewSet

router = DefaultRouter()
router.register('', WordsViewSet, basename='words')

urlpatterns = [
    path('bulk_create_word/', ProductView.as_view(), name='bulk-create'),
    path('', include(router.urls))
    # Add other URL patterns as needed
]