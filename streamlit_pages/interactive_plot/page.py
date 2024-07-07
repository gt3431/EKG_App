import streamlit as st
import pandas as pd
import streamlit_pages.interactive_plot.powerzones.create_plot as cp
from streamlit_pages.interactive_plot.powerzones.data_analize import analyze_data
from streamlit_pages.interactive_plot.power_curve.create_plot_power import create_power_curve, create_plot_power_curve

def page():

    st.markdown('## Interaktiver Plot')
    # Create a selection box for navigation
    tab_heartrate,tab_powercurve = st.tabs(["Powerzones", "Power Curve"])
    
    #einteilung in die beiden analysen
    with tab_heartrate:
        input_max_heartrate = st.slider("Geben Sie ihre maximale Herzfrequents ein:", 50, 300, 180)
        df, fig = cp.create_plot("data/activities/activity.csv", input_max_heartrate)
        
        st.markdown('#### Graph')
        st.plotly_chart(fig)

        st.markdown('#### Messwerte')
        col1, col2 = st.columns([1, 1])
        with col1:
            st.metric(label="Mittelwert Leistung", value=f"{int(df['PowerOriginal'].mean())} W")
        with col2:
            st.metric(label="Maximalwert Leistung", value=f"{int(df['PowerOriginal'].max())} W")
        
        st.markdown('#### Zonen Analyse')
        combined_df = analyze_data(df)
        st.dataframe(combined_df) 

    with tab_powercurve:
        df = pd.read_csv('data/activities/activity.csv', encoding='utf-8',sep = ",", header=0, skiprows=[1])
        power_data = df['PowerOriginal'][10:300]
        power_curve_df = create_power_curve(power_data, time_beween_samples=1, resolution_watts=1)
        fig = create_plot_power_curve(power_curve_df)
        st.plotly_chart(fig)