import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_pages.ekg.person import Person
import plotly.graph_objects as go
from scipy.signal import find_peaks
from peewee import *
from streamlit_pages.ekg.person import Person

class EKGData(Model):
    date = DateField()
    data = CharField()
    subject = ForeignKeyField(Person, backref='ekg_data')

    #TODO: Make this global
    class Meta:
        database = SqliteDatabase('data/person.db')
    
    def load_data(self):
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV', 'Zeit in ms'])
        self.peaks = None

    def find_peaks(self, height=340, distance=None, prominence=None):
        '''Find peaks in the EKG data.'''
        x = self.df['Messwerte in mV'].values
        peaks, _ = find_peaks(x, height=height, distance=distance, prominence=prominence)
        self.peaks = peaks

    def plot_time_series(self, lower=0, upper=2000):
        df = self.df.copy()
        df['Zeit in s'] = self.df['Zeit in ms'] / 1000
    
        mask = (df['Zeit in s'] > lower) & (df['Zeit in s'] < upper)
        df_selected = df.loc[mask]
        fig = px.line(df_selected, x="Zeit in s", y="Messwerte in mV")
        # Highlight peaks if they exist
        if self.peaks is not None:
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
        hr = int(num_peaks / total_time_min)
        
        return hr
    
    @staticmethod
    def load_by_id(id):
        return EKGData.get(EKGData.id == id)