import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
import numpy as np


def maxtime_spend_in_power(power_series, power):
    last_index = 0
    series_list = [0]

    max_power = power_series.max()
    power_data_cut = power_series[power_series>max_power-power]

    for index, value in power_data_cut.items():
        if last_index and last_index == index - 1:
            series_list[-1] += 1
        else:
            series_list.append(1)
        last_index = index

    return max(series_list)

def create_power_curve(power_series, time_beween_samples=1, resolution_watts=1, ):
    data = []
    for p in range(0, power_series.max(), resolution_watts):
        data.append([power_series.max()-p, maxtime_spend_in_power(power_series, p) * time_beween_samples])

    df = pd.DataFrame(data, columns=['Leistung', 'Maximale Zeit'])
    return df


def create_plot_power_curve(power_curve_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=power_curve_df["Leistung"],
        x=power_curve_df["Maximale Zeit"],
        name='Power Curve'
    ))
    fig.update_layout(
        title='Power Curve',
        xaxis_title='Maximale Zeit (s)',
        yaxis_title='Leistung (W)',
        template='plotly_dark'
    )
    return fig
