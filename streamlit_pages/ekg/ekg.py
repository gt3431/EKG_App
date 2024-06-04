import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_pages.ekg.person import Person
import plotly.graph_objects as go
from scipy.signal import find_peaks
import numpy as np


class EKGData:
    def __init__(self, ekg_dict):
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV', 'Zeit in ms'])
        self.peaks = None

    def find_peaks(self, height=340, distance=None, prominence=None):
        '''Find peaks in the EKG data.'''
        x = self.df['Messwerte in mV'].values
        peaks, _ = find_peaks(x, height=height, distance=distance, prominence=prominence)
        self.peaks = peaks

    def make_plot(self, lower=0, upper=2000):
        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit auf der x-Achse
        df = self.df.copy()
        df['Zeit in s'] = self.df['Zeit in ms'] / 1000
    
        mask = (df['Zeit in s'] > lower) & (df['Zeit in s'] < upper)
        df_selected = df.loc[mask]
        fig = px.line(df_selected, x="Zeit in s", y="Messwerte in mV")
        # Highlight peaks if they exist
        if self.peaks is not None:
            # Restrict peaks to the first 2000 values
            peak_df = df.iloc[self.peaks]
            peak_df = peak_df[mask]
            fig.add_trace(
                go.Scatter(
                    x=peak_df["Zeit in s"],
                    y=peak_df["Messwerte in mV"],
                    mode='markers',
                    marker=dict(color='red', size=8),
                    name='Peaks'
                )
            )
        fig.update_layout(title=f"EKG Daten vom {self.date}")
        return fig 

    def estimate_hr(self):
        '''Estimate heart rate based on peaks over 350 mV.'''
        # Identify peaks over 350 mV
        peaks_over_340 = self.df.iloc[self.peaks]
        
        
        # Count the number of peaks
        num_peaks = len(peaks_over_340)
        
        # Calculate the total time in milliseconds
        total_time_ms = self.df['Zeit in ms'].max() - self.df['Zeit in ms'].min()
        
        # Convert total time to minutes
        total_time_min = total_time_ms / 60000
        
        # Calculate average heart rate
        hr = num_peaks / total_time_min
        
        return hr
    
    @staticmethod
    def load_by_id(person_id, ekg_id):
        person = Person.load_by_id(person_id)
        
        if not person:
            return None
        
        for ekg in person.get("ekg_tests", []):
            if ekg["id"] == ekg_id:
                return ekg
        
        return None