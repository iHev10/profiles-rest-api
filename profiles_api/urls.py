from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(
    "hello-viewset",
    viewset=views.HelloViewSet,
    basename="hello-viewset"
)
router.register("userprofile", viewset=views.UserProfileViewSet)
router.register("feed", viewset=views.UserProfileFeedViewSet)

urlpatterns = [
    path("hello-view", view=views.HelloApiView.as_view(), name="hello-api"),
    path("login/", view=views.UserLoginAPIView.as_view()),
    path("", include(router.urls))
]
