import requests # type: ignore

# URL de base de l'API
url_base = 'http://127.0.0.1:8000/'

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)
# Données d'exemple pour la prédiction
donnees_predire = {
    "Age" : 23,
    "Sex" : "male",
    "Job" : 2,
    "Housing" : "own",
    "Duration": 45,
    "Purpose" : "radio/TV",
    "Saving_accounts"	: "litte",
    "Credit_amount": 2096,
    "Checking_account" : "litte",
    
}

# Test du endpoint de prédiction
"""response = requests.post(f"{url_base}/predire", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)
"""

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)
print("Réponse du endpoint de prediction:", response.text)