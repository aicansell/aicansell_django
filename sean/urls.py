from django.urls import path, include, re_path
from . import views
from sean.views import ItemList


urlpatterns = [
    path('item_list/', views.item_list, name='item_list'),
    #path('itemlist/', views.itemlist, name='itemlist'),
    #path('item_result/', views.item_result, name='item_result'),
    re_path(r'^api/item_results/(?P<pk>[0-9]+)$', views.item_result),

    path('itemlist/', views.itemlist, name='itemlist'),
    path('itemli/', ItemList.as_view(), name="Item_List")
    
]
