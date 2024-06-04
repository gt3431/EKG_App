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
        # Create a line plot with the selected range of values and time on the x-axis
        mask = (self.df['Zeit in ms'] > lower) & (self.df['Zeit in ms'] < upper)
        df_selected = self.df.loc[mask]
        fig = px.line(df_selected, x="Zeit in ms", y="Messwerte in mV")
        
        # Highlight peaks if they exist
        if self.peaks is not None:
            # Restrict peaks to the selected range of values
            peak_df = self.df.iloc[self.peaks]
            peak_df = peak_df[mask]
            fig.add_trace(
                go.Scatter(
                    x=peak_df["Zeit in ms"],
                    y=peak_df["Messwerte in mV"],
                    mode='markers',
                    marker=dict(color='red', size=8),
                    name='Peaks'
                )
            )
        return fig

    def estimate_hr(self):
        '''Estimate heart rate based on peaks over 350 mV.'''
        # Identify peaks over 350 mV
        peaks_over_350 = self.df[(self.df['Messwerte in mV'] > 350)]
        
        # Find the indices of these peaks
        peak_indices = peaks_over_350.index

        # Calculate the time differences between consecutive peaks
        if len(peak_indices) > 1:
            time_diffs = np.diff(self.df.loc[peak_indices, 'Zeit in ms'].values)
            
            # Calculate heart rate: 60,000 ms per minute divided by average time difference in ms
            avg_time_diff = np.mean(time_diffs)
            hr = int(6000 / avg_time_diff)
        else:
            hr = None

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