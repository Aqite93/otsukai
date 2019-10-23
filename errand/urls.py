from django.urls import path
from .views import ErrandIndexView, ErrandRegisterView
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = "errand"

urlpatterns = [
    path('', ErrandRegisterView.as_view(), name='register'),
    path('index/', ErrandIndexView.as_view(), name='index'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
