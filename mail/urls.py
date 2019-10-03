from django.conf.urls import url
from . import views

app_name = "mail"

urlpatterns = [
    url('mail/', views.send, name='sendmail'),
]
