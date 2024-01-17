from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("hello-viewset",
                viewset=views.HelloViewSet,
                basename="hello-viewset")

urlpatterns = [
    path("hello-view", view=views.HelloApiView.as_view(), name="hello-api"),
    path("", include(router.urls))
]
