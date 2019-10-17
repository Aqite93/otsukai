from django.urls import path
from .views import ErrandIndexView, ErrandRegisterView

app_name = "errand"

urlpatterns = [
    path('', ErrandRegisterView.as_view(), name='register'),
    path('index/', ErrandIndexView.as_view(), name='index'),
]
