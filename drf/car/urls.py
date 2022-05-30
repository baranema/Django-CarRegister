from django.urls import path
from .api import CarCreateApi, CarApi, CarUpdateApi, CarDeleteApi

urlpatterns = [
    path('api',CarApi.as_view()),
    path('api/create',CarCreateApi.as_view()),
    path('api/<int:pk>',CarUpdateApi.as_view()),
    path('api/<int:pk>/delete',CarDeleteApi.as_view()),
]