from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet

UsersViewSetRouter = DefaultRouter()

UsersViewSetRouter.register("", UsersViewSet, basename='users')

urlpatterns = [
    path("", include(UsersViewSetRouter.urls))
]
