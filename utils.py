import pandas as pd
import numpy as np
import streamlit as st
import os
from dotenv import load_dotenv
import requests
from PIL import Image
import pydeck as pdk


## Seconde iteration by Kamel B pour requetes API
load_dotenv()

    # Récupérer la clé API à partir des variables d'environnement
api_key = os.getenv("API_KEY")

# Fonction qui prend en entré le nom de la ville et va faire une requete a l'API
# pour aller chercher la reponse en json
def get_weather_data(city_name):

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(weather_url)
    weather_data = response.json()

    if weather_data["cod"] == 200:

        # Affichage des données météo dans un carré avec bordure
        # Image météo
        icon_id = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        icon = Image.open(requests.get(icon_url, stream=True).raw)
        st.image(icon, caption='Weather Icon', width=100)
        long = {weather_data['coord']['lon']}
        lat =  {weather_data['coord']['lat']}
        return long, lat
    else:
        st.write("Ville non trouvée. Veuillez entrer un nom de ville valide.")

# def world_map(city_name):
#  # Ajouter une ScatterplotLayer pour indiquer l'emplacement de la ville
#         weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

#         response = requests.get(weather_url)
#         weather_data = response.json()
#         long = {weather_data['coord']['lon']}
#         lat =  {weather_data['coord']['lat']}
#         view_state = pdk.ViewState(
#                 latitude=long,
#                 longitude=lat,
#                 zoom=10
#             )
#         scatter_layer = pdk.Layer(
#                 "ScatterplotLayer",
#                 data=[{
#                     'position':[ long , lat],
#                     'color': [255, 0, 0, 255],
#                     'radius': 1000
#                 }],
#                 get_position='position',
#                 get_radius='radius',
#                 get_fill_color='color',
#                 pickable=True,
#                 filled=True
#             )

#         deck = pdk.Deck(layers=[scatter_layer],
#                             map_style='mapbox://styles/mapbox/light-v9',
#                             initial_view_state=view_state)
#         st.pydeck_chart(deck)




# Premiere iteration by Alex P pour mettre en place le streamlit
# World map test, elle fonctionne pas vraiment
def world_map():
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    world = st.map(df)

    return type(world)

# World map test, elle fonctionne pas vraiment
def world_map():
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    world = st.map(df)

    return type(world)


# Rentre un test par un utilisateur
def text_input(value = "") :
     text = st.text_input("ville", value = value)
     return text


# # Créer un bouton méteo
# def btn_meteo():
#     btn_meteo = st.button("Méteo")
#     return btn_meteo

#Créer un drop down menu
def drop_down_menu(value = ""):

    option = st.selectbox("Selectionner la date du jour",
                          (value, "demain", "après demain"))
    #some_value devra être une valeur que l'api transmettra
    some_value = option
    return some_value
