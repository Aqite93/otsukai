from django.urls import path
from .views import login_view

urlpatterns = [
    path("", login_view.project_index, name="project_index"),
    path("<int:pk>/", login_view.project_detail, name="project_detail"),
]
