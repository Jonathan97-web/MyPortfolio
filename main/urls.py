from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'), name='projects_urls'),
    path('accounts/', include('allauth.urls')),
    path('', include('profiles.urls'), name='profiles_urls'),
]

handler404 = "main.views.handler404"
handler500 = "main.views.handler500"
