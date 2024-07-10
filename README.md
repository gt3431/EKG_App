# Streamlit Heart Rate Analysis App

## Projektbeschreibung

Diese Streamlit-App ermöglicht es Ihnen, Ihre Herzfrequenzdaten und Aktivitätsdaten zu analysieren und zu visualisieren. Die Anwendung bietet folgende Funktionen:

1. **Auswählen der Personen und Anlegen neuer Personen**: Benutzer können vorhandene Personen auswählen und neue Personen hinzufügen.
2. **Bild und Daten der Personen**: Anzeigen und Hochladen von Bildern und persönlichen Daten der Personen.
3. **Personen bearbeiten und löschen**: Bearbeiten und Löschen von Personeninformationen.
4. **Auswahl von EKG-Tests der Personen**: Benutzer können EKG-Tests auswählen, die mit den Personen verknüpft sind.
5. **Hinzufügen neuer Tests für Personen und Löschen von Tests**: Neue EKG-Tests können hinzugefügt und bestehende Tests gelöscht werden.
6. **Anzeige des gewählten EKGs in einem frei wählbaren Zeitbereich**: Visualisierung der EKG-Daten innerhalb eines bestimmten Zeitbereichs.
7. **Analyse der EKGs**: Berechnung und Anzeige der maximalen Herzfrequenz, durchschnittlichen Herzfrequenz und Herzratenvariabilität (HRV).
8. **Auswählen der Aktivitätsdaten aller Teilnehmer**: Benutzer können die Aktivitätsdaten aller Teilnehmer anzeigen.
9. **Anzeigbar als Powercurve oder Powerzones**: Visualisierung der Aktivitätsdaten als Powercurve oder Powerzones.
10. **Analyse der Aktivitätsdaten**: Analyse der hochgeladenen Aktivitätsdaten.
11. **Hinzufügen und Löschen von Aktivitätsdaten**: Neue Aktivitätsdaten können hinzugefügt und bestehende Daten gelöscht werden.

## Webapp
**Verwendung als Webapp**
- sie können das Programm unter: https://streamboard.streamlit.app öffnen und verwenden, alternativ können sie es auch Lokal auf ihrem PC installieren:

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