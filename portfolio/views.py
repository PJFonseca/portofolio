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
    all_commits = []

    while url:
        response = requests.get(url, params={'per_page': 100})
        all_commits.extend(response.json())
        url = response.links.get('next', {}).get('url')

    # Sort by date, newest first
    all_commits.sort(
        key=lambda c: c['commit']['author']['date'],
        reverse=True
    )

    return render(request, 'portfolio/changelog.html', {'commits': all_commits})