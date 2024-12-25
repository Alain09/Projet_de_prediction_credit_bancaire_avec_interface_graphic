# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /Predit_score_bancaire_api

# Copier uniquement les fichiers nécessaires pour limiter la taille de l'image
COPY requirements.txt ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port utilisé par Flask
EXPOSE 8000

# Commande pour lancer l'application Flask
CMD ["python", "main.py"]
