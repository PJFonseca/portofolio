from django.shortcuts import render

# Create your views here.

from .models import Discipline


def index_view(request):
    return render(request, 'portfolio/index.html')

def disciplines_view(request):
    disciplines = Discipline.objects.all()
    return render(request, 'portfolio/disciplines.html', {'disciplines': disciplines})