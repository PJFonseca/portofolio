import requests
import json
import os
from django.shortcuts import render
from django.conf import settings


CACHE_FILE = os.path.join(settings.BASE_DIR, 'changelog_cache.json')

# Create your views here.

from .models import Discipline


def index_view(request):
    return render(request, 'portfolio/index.html')

def disciplines_view(request):
    disciplines = Discipline.objects.all()
    return render(request, 'portfolio/disciplines.html', {'disciplines': disciplines})


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