from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("user", views.UserViewSet)
router.register("submit", views.SubmissionsViewSet)

urlpatterns = [
    path("hello/", views.hello_world, ),
    path("", include(router.urls)),
]

urlpatterns += router.urls
