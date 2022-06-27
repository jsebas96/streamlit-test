import streamlit as st


def about_app():
    message = '''
        Bienvenido 

        Esta es una interfaz gráfica para un sistema de medición remota que utiliza el protocolo de comunicación MQTT.
    '''
    with st.container():
        st.write(message)
