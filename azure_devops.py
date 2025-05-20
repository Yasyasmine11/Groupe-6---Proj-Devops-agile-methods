# Connexion et API DevOps
import requests

def get_latest_commits(org_url, project, repo, pat):
    url = f"{org_url}/{project}/_apis/git/repositories/{repo}/commits?api-version=7.1-preview.1"
    response = requests.get(url, auth=('', pat))
    return response.json()

def get_build_status(org_url, project, pat):
    url = f"{org_url}/{project}/_apis/build/builds?api-version=7.1"
    response = requests.get(url, auth=('', pat))
    return response.json()
