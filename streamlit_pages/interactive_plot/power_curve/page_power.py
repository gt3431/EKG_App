import streamlit as st
import pandas as pd
import streamlit_pages.interactive_plot.create_plot as cp
from streamlit_pages.interactive_plot.power_curve.create_plot_power import create_power_curve, create_plot_power_curve

def page_power():
    df = pd.read_csv('data/activities/activity.csv', encoding='utf-8',sep = ",", header=0, skiprows=[1])
    power_data = df['PowerOriginal'][10:300]
    power_curve_df = create_power_curve(power_data, time_beween_samples=1, resolution_watts=1)
    fig = create_plot_power_curve(power_curve_df)
    st.plotly_chart(fig)

