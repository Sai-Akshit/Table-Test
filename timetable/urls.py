from django.urls import path

from . import views

urlpatterns = [
    path("junior/", views.juniorTable, name='juniorTable'),
    path("senior/", views.seniorTable, name='seniorTable'),
]