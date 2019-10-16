from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from .views import LoginView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('', LoginView.as_view(), name='login-page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.logout_view, name='logout'),
]
