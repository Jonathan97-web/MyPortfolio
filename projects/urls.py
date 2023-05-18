from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProjectList.as_view(), name="home"),
    path('<int:id>/<slug:slug>/', views.ProjectDetail, name='project_detail'),
    path('project_create/', views.CreateProject, name='project_create'),
    path('project_edit/<int:id>', views.edit_project, name='project_edit'),
    path(
        'project_delete/<int:id>',
        views.delete_project, name='project_delete'),
    path('comment_edit/<int:id>', views.edit_comment, name='comment_edit'),
    path(
        'comment_delete/<int:id>',
        views.delete_comment, name='comment_delete'),
    path('like/<int:id>/<slug:slug>', views.project_like, name='project_like'),
]
