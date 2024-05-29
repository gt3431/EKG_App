import streamlit as st
import streamlit_pages.interactive_plot.create_plot as cp
from streamlit_pages.interactive_plot.power_curve.create_plot_power import maxtime_spend_in_power, sort_max_time, create_plot_power

def page_power():
    fig = create_plot_power()
    st.plotly_chart(fig)

