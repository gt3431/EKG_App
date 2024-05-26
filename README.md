# Streamlit Heart Rate Analysis App

## Projektbeschreibung

Diese Streamlit-App ermöglicht es Ihnen, Ihre Herzfrequenzdaten und EKG-daten zu analysieren und zu visualisieren. Die Anwendung bietet folgende Funktionen:

- Eingabe der maximal gemessenen Herzfrequenz.
- Erstellung eines interaktiven Plots der Herzfrequenz- und Leistungsdaten.
- Anzeige der verbrachten Zeit in verschiedenen Herzfrequenzzonen.
- Anzeige der durchschnittlichen Leistung in jeder Herzfrequenzzone.
- Analyse der EKG-Daten

## Installation

1. **Repository klonen**

   ```bash
   git clone https://github.com/gt3431/EKG_App.git
   cd EKG_App
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
   streamlit run main_app.py
   ```

2. **Eingabe der maximalen Herzfrequenz**

   Passen sie ihre Maximale HF über die Slide Bar an.

## Projektstruktur

```
EKG_APP/
├── data/
│   └── activities/
│       └── activity.csv
├── streamlit_pages/
│   ├── interactive_plot/
│   │   ├── __init__.py
│   │   ├── create_plot.py
│   │   ├── data_analize.py
│   ├── ekg/
│   │   ├── page.py
│   │   ├── read_data.py
│   │   └── process_data.py
├── main.py
├── requirements.txt
└── README.md
```

- `data/`: Enthält die CSV-Datei mit den Aktivitäten.
- `streamlit_pages/interactive_plot/`: Enthält die Module für die Erstellung des Plots und die Datenanalyse.
  - `__init__.py`: Initialisierungsdatei für das Paket.
  - `create_plot.py`: Modul zur Erstellung des Plots.
  - `data_analize.py`: Modul zur Datenanalyse.
- `streamlit_pages/ekg/`: Enthält Module zur Verarbeitung und Darstellung von EKG-Daten.
  - `page.py`: Modul zur Darstellung der EKG-Seite.
  - `read_data.py`: Modul zum Einlesen der EKG-Daten.
  - `process_data.py`: Modul zur Verarbeitung der EKG-Daten.
- `main.py`: Startpunkt der Streamlit-App.
- `requirements.txt`: Liste der Python-Pakete, die für das Projekt benötigt werden.
- `README.md`: Diese Datei.

## Lizenz

Die verwendeten Daten wurden vom MCI bereitgestellt und der Code wurde von Tobias Gasteiger und Lucas Franke erstellt und steht zur freien verfügung.
