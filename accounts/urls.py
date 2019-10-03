from django.urls import path
from .views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
]
