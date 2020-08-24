from django.urls import path
from .api import StudentApi

urlpatterns = [
    path('api',StudentApi.as_view()),
]
