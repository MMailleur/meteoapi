import streamlit as st
import requests
import os
from dotenv import load_dotenv
import folium
# from streamlit_folium import folium_static

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv("API_KEY")

def convert_to_celsius(temperature_in_kelvin):
    return temperature_in_kelvin - 273.15

def find_current_weather(city):
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['main']
        temperature = round(convert_to_celsius(weather_data['main']['temp']))
        max_temperature = round(convert_to_celsius(weather_data['main']['temp_max']))
        feels_temp = round(convert_to_celsius(weather_data['main']['feels_like']))
        humidity = weather_data['main']['humidity']
        coords = weather_data['coord']
    except KeyError:
        st.error('Ville pas trouvé')
        st.stop()
    return general, temperature, max_temperature, feels_temp, humidity, coords

def main():
    st.set_page_config(page_title="Weather App", layout="wide")  # Set page to full width

    # Add a default city
    default_city = "Carcassonne"

    st.header("☀️Méteo Carcassonne 🌥️")
    city = st.text_input("Entre la ville", default_city).lower()
    if st.button('Find'):
        general, temperature, max_temperature, feels_temp, humidity, coords = find_current_weather(city)

        # Adjust the column ratios here
        col1, col2 = st.columns([2, 1])  # First column is twice as wide as the second

        with col1:  # Display the map on the left
            st.header("Location ville sur Carte 🗺️")
            map_center = [coords['lat'], coords['lon']]
            m = folium.Map(location=map_center, zoom_start=10)
            folium.Marker(map_center, popup=city.capitalize()).add_to(m)
            folium_static(m)  # Display the map in Streamlit

        with col2:  # Display the weather predictions on the right
            st.header("Prédictions méteo🌦️")
            st.metric('Temperature', str(temperature)+'℃', str(max_temperature-temperature)+'℃')
            st.metric('Ressenti', str(feels_temp)+'℃')
            st.metric('Humidité', str(humidity)+'%', '☔')
            st.write(general)


        # # Add spacing between columns
        # st.markdown("---")  # Horizontal rule for separation

if __name__ == '__main__':
    main()
