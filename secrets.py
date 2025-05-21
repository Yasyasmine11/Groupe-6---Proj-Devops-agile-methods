from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_secret(secret_name, vault_url):
    """
    Récupère un secret depuis Azure Key Vault.
    En environnement de développement, retourne une valeur factice.
    """
    if "monkeyvault" in vault_url:  # Détection d'environnement de dev
        print(f"[DEV] Simulation de récupération du secret: {secret_name}")
        dev_secrets = {
            "github-pat": "fake-pat-for-development",
        }
        return dev_secrets.get(secret_name, "default-secret-value")
    
    # Mode production
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vault_url, credential=credential)
        return client.get_secret(secret_name).value
    except Exception as e:
        print(f"Erreur lors de la récupération du secret: {str(e)}")
        print("Retour d'une valeur par défaut pour permettre le développement")
        return "default-secret-value"