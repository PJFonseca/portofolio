
from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses_view, name="courses"),
    path('courses/', views.courses_view, name="courses"),
]