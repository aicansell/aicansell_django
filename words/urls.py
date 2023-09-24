from django.urls import path
from .views import ProductView

urlpatterns = [
    path('bulk_create_word/', ProductView.as_view(), name='bulk-create'),
    # Add other URL patterns as needed
]