from django.shortcuts import render

# Create your views here.

from .models import Discipline


def disciplines_view(request):
    disciplines = Discipline.objects.all()
    return render(request, 'portfolio/disciplines.html', {'disciplines': disciplines})