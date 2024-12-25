from pydantic import BaseModel  # Utilisé pour la validation des données
import numpy as np
import pandas as pd  # Utilisé pour la manipulation de données
import joblib  # Utilisé pour charger le modèle sauvegardé
from flask import Flask, request, jsonify  # Flask est un micro-framework pour les applications web
from flask_cors import CORS

# Charger le modèle de forêt aléatoire depuis le disque
modele = joblib.load("./model_KNN.pkl")

# Définition du schéma des données d'entrée avec Pydantic
# Cela garantit que les données reçues correspondent aux attentes du modèle

class DonneesEntree(BaseModel):
    Age : int
    Sex : str
    Job : int
    Housing : str
    Duration: int
    Purpose: str
    Saving_accounts	: str
    Credit_amount: int
    Checking_account : str
    

# Création de l'instance de l'application Flask

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)
# Définition de la route racine qui retourne un message de bienvenue
@app.route("/", methods=["GET"])
def accueil():
    """ Endpoint racine qui fournit un message de bienvenue. """
    return jsonify({"message": "Bienvenue sur l'API de prediction pour le diagnostic du diabete cfxsgfgfvb "})

# Définition de la route pour les prédictions de diabète
@app.route("/predire", methods=["POST"])
def predire():
    
    #Endpoint pour les prédictions en utilisant le modèle chargé.
    #Les données d'entrée sont validées et transformées en DataFrame pour le traitement par le modèle.

    if not request.json:
        return jsonify({"erreur": "Aucun JSON fourni"}), 400
    
    
    try:
        # Extraction et validation des données d'entrée en utilisant Pydantic
        donnees = DonneesEntree(**request.get_json())
        datas=donnees.model_dump()
        donnees_df = pd.DataFrame([datas])  # Conversion en DataFrame

        # Utilisation du modèle pour prédire et obtenir les probabilités
        predictions = modele.predict(donnees_df)
        probabilities = modele.predict_proba(donnees_df)[:, 1]  # Probabilité de la classe positive (diabète)

        # Compilation des résultats dans un dictionnaire
        resultats = {
            'prediction': int(predictions[0]),
            'probabilite_score': probabilities[0]
        }

        # Renvoie les résultats sous forme de JSON
        return jsonify({"resultats": resultats})
    except Exception as e:
        # Gestion des erreurs et renvoi d'une réponse d'erreur
        return jsonify({"erreur": str(e)}), 400
        
# Point d'entrée pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Lancement de l'application sur le port 8000 avec le mode debug activé