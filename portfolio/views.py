from django.shortcuts import render
import requests

# Create your views here.

from .models import Discipline


def index_view(request):
    return render(request, 'portfolio/index.html')

def disciplines_view(request):
    disciplines = Discipline.objects.all()
    return render(request, 'portfolio/disciplines.html', {'disciplines': disciplines})

def changelog_view(request):
    url = 'https://api.github.com/repos/PJFonseca/portfolio/commits'
    response = requests.get(url)
    commits = response.json()
    return render(request, 'portfolio/changelog.html', {'commits': commits})