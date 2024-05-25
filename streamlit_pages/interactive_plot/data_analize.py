import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit_pages.interactive_plot.create_plot as cp
import streamlit as st

def zone_time(df):
    # erstellen eines Dictionarys zum Zählen der verbrachten Zeit in jeder Zone
    zone_times = {}

    # befüllen der zone_times
    for zone in df['PowerZone'].unique():
        zone_times[zone] = df[df['PowerZone'] == zone].shape[0] #shape[0] zählt die anzahl der einträge jeder zone
    
    # Gib die verbrachte Zeit in jeder Zone aus
    for zone, time in zone_times.items():
        minuten = time // 60
        restsekunden = time % 60
        
        if zone in range(1, 6):
            st.write(f"Verbrachte Zeit in Zone {zone}: {minuten} Minute/n und {restsekunden} Sekunde/n")
        else:
            st.write(f"Verbrachte Zeit vor den Zonen: {minuten} Minute/n und {restsekunden} Sekunde/n")


def avg_power_in_zone(df):
    #durschnittspower der einzelnen zonen widergeben 
    power_zones = df.groupby('PowerZone')['PowerOriginal'].mean()
    # Ausgabe der Durchschnittsleistung jeder Zone
    for zone, avg_power in power_zones.items():
        st.write(f"Durchschnittsleistung in Zone {zone}: {round(avg_power, 1)} W")




def format_time(time):
    minutes = time // 60
    seconds = time % 60
    return f"{minutes} Minute{'n' if minutes != 1 else ''} und {seconds} Sekunde{'n' if seconds != 1 else ''}"

def analyze_data(df):
    # Erstellen eines DataFrames zum Zählen der verbrachten Zeit in jeder Zone
    zone_times = {}

    # Befüllen des DataFrames
    for zone in df['PowerZone'].unique():
        zone_times[zone] = df[df['PowerZone'] == zone].shape[0] # Anzahl der Einträge jeder Zone
    zone_times_df = pd.DataFrame.from_dict(zone_times, orient='index', columns=['Time'])
    zone_times_df.index.name = 'Zone'
    

    # Durchschnittsleistung der einzelnen Zonen
    power_zones = round(df.groupby('PowerZone')['PowerOriginal'].mean(), 1)
    avg_power_df = power_zones.reset_index(name='Average Power in Watt')

    # Kombinieren der beiden DataFrames
    combined_df = pd.merge(zone_times_df, avg_power_df, left_index=True, right_on='PowerZone', how='outer')
    combined_df['Time'] = combined_df['Time'].apply(format_time)
    # Neu anordnen der Spalten
    combined_df = combined_df[['PowerZone', 'Time', 'Average Power in Watt']]
    combined_df.set_index('PowerZone', inplace=True)
    return combined_df


