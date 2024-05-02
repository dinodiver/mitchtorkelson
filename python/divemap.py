import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium import IFrame

# Load your CSV file containing dive data
dive_data = pd.read_csv('/Users/mitchtork/website/assets/files/DiveLog.csv')

# Calculate total number of dives and dive time
total_dive_count = dive_data['Dive #'].max()  # Assuming Dive # is a unique identifier for each dive
total_dive_time_minutes = dive_data['Dive Time (min)'].sum()
total_dive_time_hours = total_dive_time_minutes // 60
remaining_minutes = total_dive_time_minutes % 60

# Aggregate the data by location and count the number of dives
location_counts = dive_data.groupby(['Location', 'lat', 'lon']).size().reset_index(name='counts')

# Create a base map
map_dive_locations = folium.Map(location=[0, 0], zoom_start=2)

# Marker cluster
marker_cluster = MarkerCluster().add_to(map_dive_locations)

# Maximum number of dives for scaling
max_dives = location_counts['counts'].max()

# Loop through the aggregated data and add each location as a marker on the map
for idx, row in location_counts.iterrows():
    # Define color based on the number of dives
    color = f"#{int((1 - row['counts'] / max_dives) * 255):02x}0000ff"
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=7,  # Constant size
        popup=(
            f"<strong>Location:</strong> {row['Location']}<br>"
            f"<strong>Dives:</strong> {row['counts']}"
        ),
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=row['counts'] / max_dives
    ).add_to(marker_cluster)

# Prepare the HTML for the dive stats
html = f"""
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 300px; height: 100px; 
            background: white; border-radius: 8px; padding: 10px; 
            box-shadow: 3px 3px 3px rgba(0,0,0,0.2);">
    <h4>Dive Stats</h4>
    <ul>
        <li>Total Dives: {total_dive_count}</li>
        <li>Total Time Underwater: {total_dive_time_hours} hours and {remaining_minutes} minutes</li>
    </ul>
</div>
"""

# Create an IFrame and add it to the map
iframe = IFrame(html=html, width=350+20, height=130+20)
popup = folium.Popup(iframe, max_width=2650)
folium.Marker([0, 0], icon=folium.Icon(icon="info-sign")).add_child(popup).add_to(map_dive_locations)

# Save the map to an HTML file
map_dive_locations.save('/Users/mitchtork/website/assets/files/DiveLog.html')
