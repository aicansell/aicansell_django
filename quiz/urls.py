from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('quiz_list/', views.quiz_list, name='quiz_list'),
    #path('quiz_result/', views.quiz_result, name='quiz_result'),
    #path('api/quiz_result/(?P<pk>[0-9]+)$', views.tutorial_detail, name='tutorial_detail' ),
    re_path(r'^api/quiz_results/(?P<pk>[0-9]+)$', views.tutorial_detail),
  
]

