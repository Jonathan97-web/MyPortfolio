from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProjectList.as_view(), name="home"),
    path('<int:id>/<slug:slug>/', views.ProjectDetail, name='project_detail'),
    path('project_create/', views.CreateProject, name='project_create')
]
