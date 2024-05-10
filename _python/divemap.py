import pandas as pd
import folium
from folium.plugins import MarkerCluster
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle

# OAuth and Sheets setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = 'your_spreadsheet_id'
RANGE_NAME = 'Sheet1!A:Z'  # Adjust range as needed

def get_google_sheet_data():
    creds = None
    try:
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    except FileNotFoundError:
        pass

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'path_to_your_credentials_file.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    return values

# Convert to DataFrame
data = get_google_sheet_data()
dive_data = pd.DataFrame(data, columns=['Dive #', 'Location', 'Dive Time (min)', 'lat', 'lon'])  # Adjust columns as per your Google Sheet

# Data processing
dive_data['Dive #'] = pd.to_numeric(dive_data['Dive #'], errors='coerce')
dive_data['Dive Time (min)'] = pd.to_numeric(dive_data['Dive Time (min)'], errors='coerce')
dive_data['lat'] = pd.to_numeric(dive_data['lat'], errors='coerce')
dive_data['lon'] = pd.to_numeric(dive_data['lon'], errors='coerce')

# Map creation
mean_lat = dive_data['lat'].mean()
mean_lon = dive_data['lon'].mean()
map_dive_locations = folium.Map(location=[mean_lat, mean_lon], zoom_start=4)
marker_cluster = MarkerCluster().add_to(map_dive_locations)
for index, row in dive_data.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"Dive #{row['Dive #']}: {row['Location']}<br>Time: {row['Dive Time (min)']} minutes",
        icon=folium.Icon(icon='tint')
    ).add_to(marker_cluster)

# Add HTML with dive stats
total_dive_count = dive_data['Dive #'].max()
total_dive_time_minutes = dive_data['Dive Time (min)'].sum()
total_dive_time_hours = total_dive_time_minutes // 60
remaining_minutes = total_dive_time_minutes % 60
html = f"""
<div id="dive-stats" style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
            width: auto; padding: 10px 20px; background: rgba(0, 0, 0, 0.85); 
            border-radius: 10px; border: 1px solid #0078A8; box-shadow: 0 2px 4px rgba(0,0,0,0.5);
            z-index: 9999; color: white; font-size: 16px; font-family: Arial, sans-serif;
            text-align: center;">
    <strong>Dive Stats:</strong> {total_dive_count} Dives | {total_dive_time_hours}h {remaining_minutes}m Underwater
    <button onclick="document.getElementById('dive-stats').style.display='none'" 
            style="float: right; border: none; background: none; color: white; font-size: 20px; cursor: pointer;">&times;</button>
</div>
"""
map_dive_locations.get_root().html.add_child(folium.Element(html))

# Save the map
map_dive_locations.save('/path_to_your_directory/DiveLog.html')
