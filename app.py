import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import streamlit as st
from utils import *


#create the page of the web app
st.set_page_config(page_title = "Weather",
                   layout = "wide", 
                   )



st.header("La méteo de ma ville")


col1, col2 = st.columns(2)

with col1 :
    
    text_input()
    btn_meteo()
    
    

with col2 :
    
    world_map()
    


