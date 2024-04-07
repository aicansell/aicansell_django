from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter

from sean.views import ItemList, item_result, item_rec
from sean.views import ItemViewSet, ItemHandleViewSet
from sean.views import ItemProcessingViewSet, ItemAnalysticsViewSet, LeaderBoardViewSet

ItemViewSetRouter = DefaultRouter()
ItemHandleViewSetRouter = DefaultRouter()
ItemProcessingViewSetRouter = DefaultRouter()
ItemAnalysticsViewSetRouter = DefaultRouter()
LeaderBoardViewSetRouter = DefaultRouter()

ItemViewSetRouter.register('', ItemViewSet, basename='item')
ItemHandleViewSetRouter.register('', ItemHandleViewSet, basename='itemhandle')
ItemProcessingViewSetRouter.register('', ItemProcessingViewSet, basename='itemprocessing')
ItemAnalysticsViewSetRouter.register('', ItemAnalysticsViewSet, basename='itemanalystics')
LeaderBoardViewSetRouter.register('', LeaderBoardViewSet, basename='leaderboard')


urlpatterns = [
    re_path(r'^api/item_results/(?P<pk>[0-9]+)$', item_result),
    re_path(r'^api/item_rec/(?P<pk>[0-9]+)$', item_rec),
    path('item/', include(ItemViewSetRouter.urls)),
    path('itemhandle/', include(ItemHandleViewSetRouter.urls)),
    path('itemprocessing/', include(ItemProcessingViewSetRouter.urls)),
    path('itemanalystics/', include(ItemAnalysticsViewSetRouter.urls)),
    path('itemli/', ItemList.as_view(), name="Item_List"),
    path('leaderboard/', include(LeaderBoardViewSetRouter.urls)),
]