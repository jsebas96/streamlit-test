import streamlit as st
import pandas as pd
import time
from database.mongo_client import db_collection

def tables():
    placeholder = st.empty()
    for seconds in range(200):

        with placeholder.container():

            col1, col2 = st.columns(2)

            data = db_collection.find()
            date, voltage, current = [], [], []

            for document in data:
                date.append(document['date'].strftime("%Y-%m-%d %H:%M:%S"))
                voltage.append(document['voltage'])
                current.append(document['current'])

            voltage_table = pd.DataFrame({
                'date': date,
                'Voltage': voltage
            }).rename(columns={'date': 'index'}).set_index('index')

            current_table = pd.DataFrame({
                'date': date,
                'Current': current
            }).rename(columns={'date': 'index'}).set_index('index')

            col1.table(
                voltage_table
            )

            col2.table(
                current_table
            )
        time.sleep(2)
