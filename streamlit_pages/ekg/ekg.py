import pandas as pd
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

    def make_plot(self):
        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit auf der x-Achse
        df_copy = self.df.copy()
        df_copy['Zeit in s'] = df_copy['Zeit in ms'] / 1000
        fig = px.line(df_copy.head(2000), x=("Zeit in s"), y="Messwerte in mV")
        # Highlight peaks if they exist
        if self.peaks is not None:
            # Restrict peaks to the first 2000 values
            peak_df = df_copy.iloc[self.peaks]
            peak_df = peak_df[peak_df.index < 2000]
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