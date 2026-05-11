import requests
import json
import os
from django.conf import settings

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required       

from portfolio.forms import ProjectForm

CACHE_FILE = os.path.join(settings.BASE_DIR, 'changelog_cache.json')

from .models import Discipline, Course, Project, Certification, Type_Technology, Teacher, Discipline_Teacher, FinalProject

def index_view(request):
    return render(request, 'portfolio/index.html')

def disciplines_view(request):
    disciplines = Discipline.objects.all()
    is_gestor = request.user.groups.filter(name='gestor-portfolio').exists()
    context = {
        'disciplines': disciplines,
        'is_gestor': is_gestor,
    }
    return render(request, 'portfolio/disciplines.html', context)

from .forms import DisciplineForm

@login_required
def discipline_create(request):
    form = DisciplineForm(request.POST or None)

    print(f"Request method: {request.method}")
    print(f"Form is valid: {form.is_valid()}")
    print(f"Form errors: {form.errors}")
    print(f"POST data: {request.POST}")

    if form.is_valid():
        form.save()
        return redirect('disciplines')

    courses = Course.objects.all().order_by('name')
    return render(request, 'portfolio/discipline_form.html', {'courses': courses, 'form': form, 'action': 'Create'})

@login_required
def discipline_edit(request, id):
    discipline = get_object_or_404(Discipline, id=id)

    if request.POST:
        form = DisciplineForm(request.POST, request.FILES, instance=discipline)
        if form.is_valid():
            form.save()
            return redirect('disciplines')
    else:
        form = DisciplineForm(instance=discipline)

    courses = Course.objects.all().order_by('name')
    return render(request, 'portfolio/discipline_form.html', {'form': form, 'courses': courses, 'discipline': discipline, 'action': 'Edit'})

@login_required
def discipline_delete(request, id):
    discipline = get_object_or_404(Discipline, id=id)
    
    if request.method == 'POST':
        discipline.delete()
        return redirect('disciplines')
    
    return render(request, 'portfolio/discipline_confirm_delete.html', {'discipline': discipline})

def projects_view(request):
    projects = Project.objects.all() 
    print(f"Projects count: {projects.count()}")
    print(f"Projects: {list(projects)}")

    is_gestor = request.user.groups.filter(name='gestor-portfolio').exists()
    
    return render(request, 'portfolio/projects.html', {'projects': projects, 'is_gestor': is_gestor})

@login_required
def project_create(request):
    form = ProjectForm(request.POST or None)

    print(f"Request method: {request.method}")
    print(f"Form is valid: {form.is_valid()}")
    print(f"Form errors: {form.errors}")
    print(f"POST data: {request.POST}")

    if form.is_valid():
        form.save()
        return redirect('projects')

    disciplines = Discipline.objects.all().order_by('name')
    return render(request, 'portfolio/project_form.html', {'disciplines': disciplines, 'form': form, 'action': 'Create'})

@login_required
def project_edit(request, id):
    project = get_object_or_404(Project, id=id)

    if request.POST:
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    disciplines = Discipline.objects.all().order_by('name')
    return render(request, 'portfolio/project_form.html', {
        'disciplines': disciplines,
        'form': form,
        'project': project,
        'action': 'Edit'
    })

@login_required
def project_delete(request, id):
    project = get_object_or_404(Project, id=id)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    return render(request, 'portfolio/project_confirm_delete.html', {'project': project})

#Done with AI help :)
def changelog_view(request):
    IGNORED_EXTENSIONS = ['.pyc', '.pyo']
    IGNORED_DIRS = ['__pycache__', '.git', 'migrations']

    def is_relevant_file(filename):
        if any(filename.endswith(ext) for ext in IGNORED_EXTENSIONS):
            return False
        if any(ignored in filename for ignored in IGNORED_DIRS):
            return False
        return True

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {settings.TOKEN_PORTFOLIO}'
    }

    # Load existing cache
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cached_commits = json.load(f)
    else:
        cached_commits = []

    # Get the SHA of the most recent cached commit
    latest_sha = cached_commits[0]['sha'] if cached_commits else None
    print(f"Latest cached SHA: {latest_sha}")

    # Fetch only new commits since latest_sha
    url = 'https://api.github.com/repos/PJFonseca/portfolio/commits'
    new_raw_commits = []

    while url:
        response = requests.get(
            url,
            params={'per_page': 100, 'sha': 'main'},
            headers=headers
        )
        if response.status_code != 200:
            break
        data = response.json()
        if not data:
            break

        # Stop when we reach a commit we already have
        found_existing = False
        for commit in data:
            if commit['sha'] == latest_sha:
                found_existing = True
                break
            new_raw_commits.append(commit)

        if found_existing:
            break

        url = response.links.get('next', {}).get('url')

    print(f"New commits to fetch: {len(new_raw_commits)}")

    # Fetch details for new commits only
    new_detailed = []
    for commit in new_raw_commits:
        detail = requests.get(commit['url'], headers=headers)
        if detail.status_code != 200:
            continue

        data = detail.json()
        relevant_files = [f for f in data.get('files', []) if is_relevant_file(f['filename'])]

        if not relevant_files:
            continue

        data['files'] = relevant_files
        data['stats'] = {
            'additions': sum(f['additions'] for f in relevant_files),
            'deletions': sum(f['deletions'] for f in relevant_files),
            'total': sum(f['changes'] for f in relevant_files),
        }

        new_detailed.append(data)

    # Merge new commits with cache and save
    if new_detailed:
        all_commits = new_detailed + cached_commits
        with open(CACHE_FILE, 'w') as f:
            json.dump(all_commits, f)
        print(f"Cache updated with {len(new_detailed)} new commits")
    else:
        all_commits = cached_commits
        print("No new commits, using cache")

    return render(request, 'portfolio/changelog.html', {'commits': all_commits})