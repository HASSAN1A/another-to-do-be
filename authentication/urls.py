from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet
from django.urls import path

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("accounts/", include("rest_registration.api.urls")),
] + router.urls
