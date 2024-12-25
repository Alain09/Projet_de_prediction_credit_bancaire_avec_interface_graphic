import requests # type: ignore
import pandas as pd

# URL de base de l'API
url_base =  "http://localhost:8000"

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
    "Saving_accounts"	: "little",
    "Credit_amount": 2096,
    "Checking_account" : "little",
    
}

# Test du endpoint de prédiction
"""response = requests.post(f"{url_base}/predire", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)
"""

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)
result = response.json()

#df=pd.DataFrame({"Prediction":result['resultats']['prediction'],"Probabilite_score":f"{result['resultats']['probabilite_score']*100:.2f}"})
print("affcihe ",response.json()['resultats'])
print("Réponse bzbabab du endpoint de prediction hjb:", {"Prediction":result['resultats']['prediction'],"Probabilite_score":f"{result['resultats']['probabilite_score']*100:.2f}"})