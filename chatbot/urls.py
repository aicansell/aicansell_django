from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.chatbot_view, name='chatbot_view'),
    
  
]
