from django.urls import path, include, re_path
from . import views



urlpatterns = [
    path('item_list/', views.item_list, name='item_list'),
    #path('itemlist/', views.itemlist, name='itemlist'),
    
  
]
