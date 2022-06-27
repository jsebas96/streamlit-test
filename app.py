import streamlit as st
from services.mqtt_client import client
from views.about_app import about_app
from views.charts import charts
from views.tables import tables


# Add sidebar
st.sidebar.write('Bienvenido')

# Add a menu to sidebar
menu = ("Sobre la App", "Gráficas", "Tablas")
selected_option = st.sidebar.selectbox("Seleccione una opción", menu, index=0)

if selected_option == "Sobre la App":
    about_app()
elif selected_option == "Gráficas":
    charts()
elif selected_option == "Tablas":
    tables()
        

# ///////////////////////////////////
# '''
#     DEFINE VIEWS TO SHOW DATA
# '''
#//////////////////////////////////###
