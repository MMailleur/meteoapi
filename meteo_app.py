import streamlit as st  # Création d'applications web interactives
import requests  # Requêtes HTTP
import pandas as pd  # Manipulation de données avec pandas
import numpy as np  # Opérations mathématiques

#donnée de loc dans l'idéal les données de l'api
city_data = {
    'lat': [48.8566, 43.2965, 45.75, 43.6045, 43.7102],
    'lon': [2.3522, 5.3699, 4.85, 1.4440, 7.2620]
}
#ville choisi string attendu par pytest
value_ville = "Carcassonne"

#découpage pour visualisation
col11, col22, col33 = st.columns(3)
with col22:
    #titre
    st.title(value_ville)

#découpage pour visualisation
col1, col2, col3 = st.columns((2, 0.5, 0.5))
with col1:
    #dataframe ville et affichage de la map
    df = pd.DataFrame(city_data)
    st.map(df)

with col3:
    #affichage des truc de mort de maxime
    st.metric(label=":sunny:", value=32)
    st.metric(label=":moon:", value=7)
    st.metric(label=":sunny:", value=42)
    st.metric(label=":moon:", value=10)
    st.metric(label=":sunny:", value=30)
