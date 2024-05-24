import streamlit as st
import streamlit_pages.interactive_plot.create_plot as cp
from streamlit_pages.interactive_plot.data_analize import zone_time, avg_power_in_zone, analyze_data


def page():
    # Eingabefeld für eine Zahl
    input_max_heartrate = st.number_input('Geben Sie ihre maximal gemessene Herzfrequents ein:', min_value=0, max_value=300, value=180)

    # col1, col2= st.columns(2)
    df, fig = cp.create_plot("data/activities/activity.csv", input_max_heartrate)
    
    
    st.markdown('#### Graph')
    st.plotly_chart(fig)

    
    st.markdown('#### Messwerte')
    # Erstelle zwei Spalten
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.metric(label="Mittelwert Leistung", value=f"{int(df["PowerOriginal"].mean())} W", delta="1.2 °F")
        st.metric(label="Maximalwert Leistung", value=f"{int(df["PowerOriginal"].max())} W", delta="1.2 °F")
    with col2:
        # zone_times = zone_time(df)
        st.markdown('##### Zonen Analyse:')
        combined_df = analyze_data(df)
        st.write(combined_df.reset_index(drop=True))

    # with col3:
    #     awg_power = avg_power_in_zone(df)
        

        

    return input_max_heartrate        
    
        




