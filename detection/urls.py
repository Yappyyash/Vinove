from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('save_name', views.save_name, name='save_name'),
    path('activity_view', views.activity_view, name='activity_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





handler404 = 'detection.views.handler404'
handler500 = 'detection.views.handler500'

