# Streamlit Heart Rate Analysis App

## Projektbeschreibung

Diese Streamlit-App ermöglicht es Ihnen, Ihre Herzfrequenzdaten zu analysieren und zu visualisieren. Die Anwendung bietet folgende Funktionen:

- Eingabe der maximal gemessenen Herzfrequenz.
- Erstellung eines interaktiven Plots der Herzfrequenz- und Leistungsdaten.
- Anzeige der verbrachten Zeit in verschiedenen Herzfrequenzzonen.
- Anzeige der durchschnittlichen Leistung in jeder Herzfrequenzzone.

## Installation

1. **Repository klonen**

   ```bash
   git clone https://github.com/dein-benutzername/dein-repo.git
   cd dein-repo
   ```

2. **Virtuelle Umgebung erstellen**

   Erstelle eine virtuelle Umgebung, um Abhängigkeiten zu isolieren.

   ```bash
   python -m venv venv
   ```

3. **Virtuelle Umgebung aktivieren**

   - **Windows**

     ```bash
     .\venv\Scripts\activate
     ```

   - **macOS/Linux**

     ```bash
     source venv/bin/activate
     ```

4. **Abhängigkeiten installieren**

   Stelle sicher, dass `pip` auf dem neuesten Stand ist und installiere die erforderlichen Pakete.

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Verwendung

1. **Starten der Streamlit-App**

   ```bash
   streamlit run path/to/your/main_app.py
   ```

2. **Eingabe der maximalen Herzfrequenz**

   Geben Sie die maximale gemessene Herzfrequenz in das Eingabefeld ein und sehen Sie sich die Analyse und die Visualisierungen an.

## Projektstruktur

```
streamlit-heart-rate-analysis/
├── data/
│   └── activities/
│       └── activity.csv
├── streamlit_pages/
│   ├── interactive_plot/
│   │   ├── create_plot.py
│   │   ├── data_analize.py
│   │   └── page.py
├── main_app.py
├── requirements.txt
└── README.md
```

- `data/`: Enthält die CSV-Datei mit den Aktivitäten.
- `streamlit_pages/interactive_plot/`: Enthält die Module für die Erstellung des Plots und die Datenanalyse.
- `main_app.py`: Startpunkt der Streamlit-App.
- `requirements.txt`: Liste der Python-Pakete, die für das Projekt benötigt werden.
- `README.md`: Diese Datei.

## Anforderungen

Stelle sicher, dass folgende Pakete in der `requirements.txt` enthalten sind:

```
streamlit
pandas
plotly
```

## Beispiel-Code

### `main_app.py`

```python
import streamlit as st
import streamlit_pages.interactive_plot.create_plot as cp
from streamlit_pages.interactive_plot.data_analize import analyze_data

def page():
    # Eingabefeld für eine Zahl
    input_max_heartrate = st.number_input('Geben Sie ihre maximal gemessene Herzfrequenz ein:', min_value=0, max_value=300, value=180)

    # Erstellen des Plots und DataFrames
    df, fig = cp.create_plot("data/activities/activity.csv", input_max_heartrate)
    
    st.markdown('#### Graph')
    st.plotly_chart(fig)

    st.markdown('#### Messwerte')
    # Erstelle zwei Spalten
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.metric(label="Mittelwert Leistung", value=f"{int(df['PowerOriginal'].mean())} W")
        st.metric(label="Maximalwert Leistung", value=f"{int(df['PowerOriginal'].max())} W")
    
    with col2:
        combined_df = analyze_data(df)
        combined_df.set_index('PowerZone', inplace=True)
        selected_columns = combined_df[['Time', 'Average Power']]
        st.table(selected_columns)

if __name__ == "__main__":
    page()
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der LICENSE-Datei.

---

Passe die README-Datei nach Bedarf an, insbesondere den Abschnitt "Projektbeschreibung" und "Projektstruktur", um sicherzustellen, dass alle relevanten Informationen und Dateipfade korrekt sind.