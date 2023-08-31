import streamlit as st
from utils import *


#create the page of the web app
st.set_page_config(page_title = "Weather",
                   layout = "wide", 
                   )


# Title
st.header("La méteo de ma ville")

# Left and right column
col1, col2 = st.columns(2)

# In column 1
with col1 :
    
    text_input()
    btn_meteo()
 
# In column 2
with col2 :
    
    world_map()
    

drop_down_menu()
