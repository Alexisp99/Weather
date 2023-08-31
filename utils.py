import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
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