
from django.urls import path
from . import views


urlpatterns = [
    path('', views.disciplines_view, name="disciplines"),
    path('disciplines/', views.disciplines_view, name="disciplines"),
]