from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("check/", views.check, name="demo"),
    path("rsp/", views.acceptResponse, name="rsp")
]
