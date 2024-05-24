import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_plot(csv_path, max_heartrate):
    
    #Read data from csv
    df = pd.read_csv(csv_path, sep=",", header=0)

    # Definiere die Prozentbereiche für die Leistungszonen
    zone_ranges = [(0, 60), (60, 70), (70, 80), (80, 90), (90, 100)]

    # Berechne die Grenzen für die Leistungszonen basierend auf dem maximalen Herzfrequenzwert und den Prozentbereichen
    # durch 100 da wir ganze prozentzahlen haben -> ersetzen die werde der zone_ranges 
    power_zones = [(max_heartrate * low / 100, max_heartrate * high / 100) for low, high in zone_ranges]

    # Funktion zur Zuordnung der Zone basierend auf der Herzfrequenz
    def assign_power_zone(heart_rate):
        for zone_index, (zone_min, zone_max) in enumerate(power_zones, start=1):
            if zone_min <= heart_rate <= zone_max:
                return zone_index
        return 1

    # Eine neue Spalte für die Leistungszonen erstellen und die Zone für jeden Eintrag im DataFrame bestimmen
    df['PowerZone'] = df['HeartRate'].apply(assign_power_zone)
    
    # Erstelle ein Plotly-Figure-Objekt
    fig = go.Figure()

    # Erstelle ein Plotly-Figure-Objekt mit zwei y-Achsen
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Füge die Power-Daten zum Diagramm hinzu
    fig.add_trace(go.Scatter(x=df.index, y=df['PowerOriginal'], mode='lines', name='Power'), secondary_y=False)

    # Füge die Heartrate-Daten zum Diagramm hinzu
    fig.add_trace(go.Scatter(x=df.index, y=df['HeartRate'], mode='lines', name='HeartRate'), secondary_y=True)

    # Define the zones and colors
    zone_colors = {
        1: 'rgba(0, 255, 0, 0.2)',    # Green
        2: 'rgba(255, 255, 0, 0.2)',  # Yellow
        3: 'rgba(255, 165, 0, 0.2)',  # Orange
        4: 'rgba(255, 0, 0, 0.2)',    # Red
        5: 'rgba(0, 0, 255, 0.2)'     # Blue
    }

    # Add shapes for each powerzone segment
    prev_zone = None
    start_idx = None

    for idx, row in df.iterrows():
        current_zone = row['PowerZone']
        
        if prev_zone is None:
            # Initial case
            start_idx = idx
            prev_zone = current_zone
        elif current_zone != prev_zone:
            # Zone change
            fig.add_shape(
                type="rect",
                xref="x",
                yref="paper",
                x0=start_idx,
                y0=0,
                x1=idx - 1,  # End at the previous index
                y1=1,
                fillcolor=zone_colors[prev_zone],
                line=dict(width=0)
            )
            # Reset start index and previous zone
            start_idx = idx
            prev_zone = current_zone

    # Add the last segment
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=start_idx,
        y0=0,
        x1=df.index[-1],
        y1=1,
        fillcolor=zone_colors[prev_zone],
        line=dict(width=0)
    )
    # Add legend entries for the power zones
    for zone, color in zone_colors.items():
        fig.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='markers',
            marker=dict(size=10, color=color),
            legendgroup=f'Zone {zone}',
            showlegend=True,
            name=f'Zone {zone}'
        ))

    # Update layout
    fig.update_layout(
        title='Heartrate and Power with Powerzone Background',
        xaxis_title='Index',
        yaxis_title='Value',
        yaxis=dict(
            range=[0, max(df['HeartRate'].max(), df['PowerOriginal'].max()) + 10]
        )
    )

    # Diagramm zurückgeben
    return df, fig