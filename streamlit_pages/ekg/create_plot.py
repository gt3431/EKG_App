import pandas as pd
import plotly.express as px
import os
import streamlit as st

def make_plot(ekg_test):
    # Erstelle den Pfad zur Datei basierend auf dem Variablennamen
    file_path = os.path.join('data', 'ekg_data', f'{ekg_test}.txt')
    
    # Lade die TXT-Datei in ein DataFrame
    try:
        # Lade die Datei ohne Header und mit Tabulator als Trennzeichen
        data = pd.read_csv(file_path, delimiter="\t", header=None, names=["Messwerte in mV", "Zeit in ms"])
    except FileNotFoundError:
        st.error(f'Datei nicht gefunden: {file_path}')
        return None

    # Überprüfen, ob die notwendigen Spalten vorhanden sind
    if "Zeit in ms" not in data.columns or "Messwerte in mV" not in data.columns:
        st.error(f'Die Datei {file_path} enthält nicht die erforderlichen Spalten.')
        return None

    # Erstelle einen Line Plot, der die ersten 2000 Werte mit der Zeit auf der x-Achse darstellt
    fig = px.line(data.head(2000), x="Zeit in ms", y="Messwerte in mV", title=f'Plot für {ekg_test}')
    return fig
