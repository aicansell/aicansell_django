from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet
from users.views import UserSubOrgViewSet, UserMappingViewSet

UsersViewSetRouter = DefaultRouter()
UserSubOrgViewSetRouter = DefaultRouter()
UserMappingViewSetRouter = DefaultRouter()

UsersViewSetRouter.register("", UsersViewSet, basename='users')
UserSubOrgViewSetRouter.register("", UserSubOrgViewSet, basename='user_suborgs')
UserMappingViewSetRouter.register("", UserMappingViewSet, basename='user_mappings')

urlpatterns = [
    path("user/", include(UsersViewSetRouter.urls)),
    path("usersuborg/", include(UserSubOrgViewSetRouter.urls)),
    path("usermapping/", include(UserMappingViewSetRouter.urls)),
]
