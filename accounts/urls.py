from django.urls import path
from .views import LoginView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    # path('', LoginView.as_view()),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('/', LoginView.as_view(), name='login-page'),
]
