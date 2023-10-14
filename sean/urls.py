from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from sean.views import ItemViewSet, ItemHandleViewSet

# from . import views
# #from sean.views import ItemList


# urlpatterns = [
#     path('item_list/', views.item_list, name='item_list'),
#     #path('itemlist/', views.itemlist, name='itemlist'),
#     #path('item_result/', views.item_result, name='item_result'),
#     re_path(r'^api/item_results/(?P<pk>[0-9]+)$', views.item_result),
#     re_path(r'^api/item_rec/(?P<pk>[0-9]+)$', views.item_rec),


#     #path('itemli/', ItemList.as_view(), name="Item_List")
    
# ]

router = DefaultRouter()
router.register('item', ItemViewSet, basename='item')
router.register('itemhandle', ItemHandleViewSet, basename='itemhandle')

urlpatterns = [
    path('', include(router.urls)),
]