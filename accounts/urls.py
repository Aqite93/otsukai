from django.urls import path
from . import views
from .views import LoginView, SignUp
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('', LoginView.as_view(), name='login-page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
]
