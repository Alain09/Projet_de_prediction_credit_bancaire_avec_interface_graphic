import streamlit as st
import requests
import pandas as pd

# Titre de l'application
st.title("Prédiction de Score Bancaire")

# Formulaire d'entrée utilisateur
st.header("Entrez les données nécessaires")
Age = st.number_input("Âge", min_value=18, max_value=100, step=1)
Sex = st.selectbox("Sexe", options=["male", "female"])
Job = st.number_input("Type d'emploi", min_value=0,max_value=3)
Housing = st.selectbox("Logement", options=["own", "rent", "free"])
Duration = st.number_input("Durée (en mois)", min_value=1, step=5)
Purpose = st.selectbox("But", options=["radio/TV", "car", "education", "others"])
Saving_accounts = st.selectbox("Épargne", options=["little", "moderate", "rich"])
Credit_amount = st.number_input("Montant du crédit", min_value=0, step=100)
Checking_account = st.selectbox("Compte courant", options=["little", "moderate", "rich"])



# Bouton pour soumettre
if st.button("Prédire"):
    # Préparer les données pour l'API
    data = {
        "Age": Age,
        "Sex": Sex,
        "Job": Job,
        "Housing": Housing,
        "Duration": Duration,
        "Purpose": Purpose,
        "Saving_accounts": Saving_accounts,
        "Credit_amount": Credit_amount,
        "Checking_account": Checking_account,
        
      
    }
    
    try:
        # Appel à l'API Flask
        response = requests.post("http://localhost:8000/predire", json=data)
        st.write("affcihe",response.status_code)
        if response.status_code == 200:
            result = response.json()
            #df=pd.DataFrame({"Prediction":result.resultats.prediction,"Probabilite_score":f"{result.resultats.probabilite_score*100:.2f}"})
            st.success(f"Résultat de la prédiction : {result['resultats']['prediction']}")
            st.success(f"Probabilite_score : {result['resultats']['probabilite_score']}")
        else:
            st.error(f"Erreur : {response.json().get('erreur', 'Erreur inconnue')}")
    except Exception as e:
        st.error(f"Erreur lors de l'appel à l'API : {e}")
