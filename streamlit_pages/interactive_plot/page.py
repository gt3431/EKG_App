import streamlit as st
import streamlit_pages.interactive_plot.create_plot as cp

def page():

    col1, col2= st.columns(2)
    df, fig = cp.create_plot("data/activities/activity.csv", 200)

    with col1:
        st.markdown('#### Messwerte')
        st.metric(label="Mittelwert Leistung", value=f"{int(df["PowerOriginal"].mean())} W", delta="1.2 °F")

    with col2:
        st.markdown('#### Graph')
        st.plotly_chart(fig)
        




