import pandas as pd
import folium
from folium import IFrame
from folium.plugins import MarkerCluster

# Load your CSV file containing dive data
dive_data = pd.read_csv('/Users/mitchtork/website/assets/files/DiveLog.csv')

# Calculate total number of dives and dive time
total_dive_count = dive_data['Dive #'].max()
total_dive_time_minutes = dive_data['Dive Time (min)'].sum()
total_dive_time_hours = total_dive_time_minutes // 60
remaining_minutes = total_dive_time_minutes % 60
total_dive_time_days = total_dive_time_hours // 24
remaining_hours = total_dive_time_hours % 24

# Calculate mean latitude and longitude for map centering
mean_lat = dive_data['lat'].mean()
mean_lon = dive_data['lon'].mean()

# Create a base map, centering on the mean location
map_dive_locations = folium.Map(location=[mean_lat, mean_lon], zoom_start=4)

# Add the Stamen Terrain tiles with proper attribution
folium.TileLayer('Stamen Watercolor', attr='Map data © OpenStreetMap contributors, CC-BY-SA, Imagery © Stamen Design').add_to(map_dive_locations)

marker_cluster = MarkerCluster().add_to(map_dive_locations)
for index, row in dive_data.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"Dive #{row['Dive #']}: {row['Location']}<br>Time: {row['Dive Time (min)']} minutes",
        icon=folium.Icon(icon='tint')
    ).add_to(marker_cluster)

# HTML to display stats with close button
html = f"""
<div id="dive-stats" style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
            width: auto; padding: 10px 20px; background: rgba(0, 0, 0, 0.85); 
            border-radius: 10px; border: 1px solid #0078A8; box-shadow: 0 2px 4px rgba(0,0,0,0.5);
            z-index: 9999; color: white; font-size: 16px; font-family: Arial, sans-serif;
            text-align: center;">
    <strong>Dive Stats:</strong> {total_dive_count} Dives | {total_dive_time_days}d {remaining_hours}h {remaining_minutes}m Underwater
    <button onclick="document.getElementById('dive-stats').style.display='none'" 
            style="float: right; border: none; background: none; color: white; font-size: 20px; cursor: pointer;">&times;</button>
</div>
"""

# Add this HTML to the map
map_dive_locations.get_root().html.add_child(folium.Element(html))

# Save the map
map_dive_locations.save('/Users/mitchtork/website/assets/files/DiveLog.html')