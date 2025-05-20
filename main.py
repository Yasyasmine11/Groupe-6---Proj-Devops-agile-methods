# script principal
from azure_devops import get_latest_commits, get_build_status
from secrets import get_secret
from notifier import send_email
from logger import log_message
from dashboard import print_build_dashboard

# Configurations
ORG_URL = "https://dev.azure.com/elyesboudabous/"
PROJECT = "project_estiam"
REPO = "Groupe-6---Proj-Devops-agile-methods"
VAULT_URL = "https://monkeyvault.vault.azure.net/"
SECRET_NAME = "az-pat"

pat = get_secret(SECRET_NAME, VAULT_URL)

commits = get_latest_commits(ORG_URL, PROJECT, REPO, pat)
builds = get_build_status(ORG_URL, PROJECT, pat)

# Envoie un mail si échec build
for build in builds['value'][:1]:
    if build['result'] == "failed":
        send_email("Build Échoué", f"Le build {build['buildNumber']} a échoué.", "destinataire@mail.com")
        log_message("Alerte: Build échoué envoyé")

print_build_dashboard(builds)