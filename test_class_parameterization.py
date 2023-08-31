import pandas as pd  # Import des données avec pandas
import pytest  # Tests unitaires

from meteo_app import value_ville, df  # Import des éléments depuis meteo_app

# Test de type pour une variable
def test_string():
    assert isinstance(value_ville, str)  # Vérification du type str pour value_ville

# Test de non-vacuité du DataFrame pour st.map
def test_map_dataframe_not_empty():
    assert not df.empty  # Vérification de non-vacuité du DataFrame df
