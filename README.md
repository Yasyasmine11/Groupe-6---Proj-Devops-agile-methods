# Team 6 : Devops & Agile methods

## Objectif du projet :

Note projet DevOps Notifier, est une application en python qui Surveille un dépôt Azure DevOps, envoie des alertes email à chaque nouveau commit ou échec de build, Permet un petit dashboard de build (texte ou web), et permet de stocker les secrets dans Azure Key Vault.

## Fonctionnalités : 

1. Vérifie régulièrement un dépôt Azure DevOps pour détecter les nouveaux commits ou les échecs de build.
2. Envoie des alertes par email à chaque nouveau commit ou échec de build.
3. Log dans Applications insights.
4. sécuriser des secrets dans Azure Key Vault.
5. Mini dashboard en ligne de commande.

## on a installer les dépendances avec la commande suivante : 

>> pip install azure-devops opencensus-ext-azure azure-identity azure-keyvault-secrets requests

![alt text](image.png)