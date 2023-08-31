import pandas as pd
import numpy as np
import streamlit as st

def world_map():
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    world = st.map(df)
    
    return world



def text_input(value = "") :
     text = st.text_input("ville", value = value)
     return text
 
def btn_meteo():
    btn_meteo = st.button("Méteo")
    return btn_meteo

def drop_down_menu():
    
    option = st.selectbox("Selectionner la date du jour",
                          ("Aujourd'hui", "demain", "après demain"))
    #some_value devra être une valeur que l'api transmettra
    some_value = "demain"
    st.write(some_value)