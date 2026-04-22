
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name="home"),
    path('disciplines/', views.disciplines_view, name="disciplines"),
]