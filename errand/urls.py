from django.urls import path
from .views import ErrandIndexView

app_name = "errand"

urlpatterns = [
    path('index/', ErrandIndexView.as_view(), name='index'),
]
