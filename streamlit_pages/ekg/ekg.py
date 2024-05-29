import pandas as pd
import plotly.express as px
from streamlit_pages.ekg.person import Person
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.datasets import electrocardiogram
from scipy.signal import find_peaks

class EKGData:

    def __init__(self, ekg_dict):
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])
        self.peaks = None


    def find_peaks(self, height=None, distance=None, prominence=None):
        '''Find peaks in the EKG data.'''
        x = self.df['Messwerte in mV'].values
        peaks, _ = find_peaks(x, height=height, distance=distance, prominence=prominence)
        self.peaks = peaks

    def make_plot(self):
        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        fig = px.line(self.df, x="Zeit in ms", y="Messwerte in mV")
        # Highlight peaks if they exist
        if self.peaks is not None:
            peak_df = self.df.iloc[self.peaks]
            fig.add_trace(
                go.Scatter(
                    x=peak_df.index,
                    y=peak_df["Messwerte in mV"],
                    mode='markers',
                    marker=dict(color='red', size=8),
                    name='Peaks'
                )
            )
        return fig 
    
    @staticmethod
    def load_by_id(person_id, ekg_id):
        person = Person.load_by_id(person_id)
        
        if not person:
            return None
        
        for ekg in person.get("ekg_tests", []):
            if ekg["id"] == ekg_id:
                return ekg
        
        return None