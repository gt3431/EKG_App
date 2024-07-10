import streamlit as st
import pandas as pd
import streamlit_pages.interactive_plot.powerzones.create_plot as cp
from streamlit_pages.interactive_plot.powerzones.data_analize import analyze_data
from streamlit_pages.interactive_plot.power_curve.create_plot_power import create_power_curve, create_plot_power_curve
from streamlit_pages.interactive_plot.activity import Activity
from streamlit_pages.ekg.edit_masks import new_activity_test
import os
def page():
    activities = st.session_state.person.get_activity_names()
    activities.append((-1, 'Neuen Test hinzufügen'))
    st.write("## Aktivitätsdaten")
    st.session_state.aktivity_name = st.selectbox(
        'Testauswahl',
        options=activities,
        format_func=lambda option: option[1],
        key="sbActivityTestauswahl"
    )
    
    # Überprüfen, ob ein neuer Test hinzugefügt werden soll
    if st.session_state.aktivity_name and st.session_state.aktivity_name[0] == -1:
        new_activity_test()
            
    
    
    if st.session_state.aktivity_name and st.session_state.aktivity_name[0] != -1:
        
        tab_heartrate,tab_powercurve = st.tabs(["Powerzones", "Power Curve"])
        with tab_heartrate:
            
            input_max_heartrate = st.slider("Geben Sie ihre maximale Herzfrequents ein:", 110, 210, 180)
            df, fig = cp.create_plot(Activity.get_by_id(st.session_state.aktivity_name[0]).data, input_max_heartrate)

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
            df = pd.read_csv(Activity.get_by_id(st.session_state.aktivity_name[0]).data, encoding='utf-8',sep = ",", header=0, skiprows=[1])
            power_data = df['PowerOriginal']
            power_curve_df = create_power_curve(power_data, time_beween_samples=1, resolution_watts=1)
            fig = create_plot_power_curve(power_curve_df)
            st.plotly_chart(fig)

    ## Aktivität Löschen
    if st.session_state.aktivity_name and st.session_state.aktivity_name[0] != -1:
        if st.button("Delete Aktivity"):
            # Lade die Aktivität
            activity = Activity.get_by_id(st.session_state.aktivity_name[0])
            # Lösche die Aktivität
            activity.delete_instance()
            os.remove(activity.data)
            # Aktualisiere die Sitzung
            st.session_state.aktivity_name = None
            st.success("Aktivität erfolgreich gelöscht!")
            st.experimental_rerun()
    else:
        st.warning("Bitte wählen Sie eine Aktivität aus.")
