import streamlit as st
import requests
import pandas as pd
import numpy as np


st.header('Nom de ville')

city_data = {
    'lat': [48.8566, 43.2965, 45.75, 43.6045, 43.7102],
    'lon': [2.3522, 5.3699, 4.85, 1.4440, 7.2620],
    'temp' :[22,26,30,12,21]
}

df = pd.DataFrame(city_data)
st.map(latitude="lat",longitude="lon", size =14)
