from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('save_name', views.save_name, name='save_name'),
    path('activity_view', views.activity_view, name='activity_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)