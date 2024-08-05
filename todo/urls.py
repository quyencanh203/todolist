from django.urls import path

from . import views

urlpatterns = [
    path("update/<int:id>", views.update, name="update"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("", views.index, name="index"),
]