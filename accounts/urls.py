from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
]
