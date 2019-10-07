from django.urls import path
from .views import PredictionView

app_name = "prediction"

urlpatterns = [
    path('prediction/', PredictionView.as_view(), name='index'),
]
