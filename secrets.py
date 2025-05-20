# Récupération secrets depuis Key Vault

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_secret(secret_name, vault_url):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    return client.get_secret(secret_name).value
