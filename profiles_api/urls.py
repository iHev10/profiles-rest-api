from django.urls import path
from . import views

urlpatterns = [
    path("hello-view", view=views.HelloApiView.as_view(), name="hello-api")
]