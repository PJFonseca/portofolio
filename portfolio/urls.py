
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name="home"),
    path('changelog/', views.changelog_view, name="changelog"),
    path('disciplines/', views.disciplines_view, name="disciplines"),
    path('disciplines/create/', views.discipline_create, name='discipline_create'),
    path('disciplines/<int:id>/edit/', views.discipline_edit, name='discipline_edit'),
    path('disciplines/<int:id>/delete/', views.discipline_delete, name='discipline_delete'),
    path('projects/', views.projects_view, name="projects"),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:id>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:id>/delete/', views.project_delete, name='project_delete'),
]