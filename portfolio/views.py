from django.shortcuts import render

# Create your views here.

from .models import Course, Discipline


def courses_view(request):
    courses = Discipline.objects.all()
    return render(request, 'portfolio/courses.html', {'courses': courses})