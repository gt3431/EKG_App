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
   python -m venv .venv
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
   streamlit run main.py
   ```

## Lizenz

Die verwendeten Daten wurden vom MCI bereitgestellt und der Code wurde von Tobias Gasteiger und Lucas Franke erstellt und steht zur freien verfügung.