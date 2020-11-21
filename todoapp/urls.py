from django.urls import path
from .views import home, TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", TodoViewSet, basename="todo")

urlpatterns = [path("home", home, name="home")] + router.urls
