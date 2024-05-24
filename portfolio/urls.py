from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.home),
    path('experiences/', include('experiences.urls')),
    path('projects/', include('projects.urls')),
    path('generalSettings/', include('generalSettings.urls')),
    path('send-resume/', views.send_resume_with_email, name='send_resume_with_email'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)