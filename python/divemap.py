import pandas as pd
import folium

# Load your CSV file containing dive data
dive_data = pd.read_csv('/Users/mitchtork/website/assets/files/DiveLog.csv')

# Calculate total number of dives and dive time
total_dive_count = dive_data['Dive #'].max()
total_dive_time_minutes = dive_data['Dive Time (min)'].sum()
total_dive_time_hours = total_dive_time_minutes // 60
remaining_minutes = total_dive_time_minutes % 60

# Create a base map, potentially adjusting the initial centering point
map_dive_locations = folium.Map(location=[0, 0], zoom_start=2, tiles=None)  # Set tiles=None if Esri Ocean Basemap is primary

# Add Esri Ocean Basemap
esri_ocean = folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Esri Ocean Basemap',
    overlay=False,
    control=True
)
esri_ocean.add_to(map_dive_locations)

# HTML to display stats
html = f"""
<div style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
            width: auto; padding: 10px 20px; background: rgba(0, 0, 0, 0.85); 
            border-radius: 10px; border: 1px solid #0078A8; box-shadow: 0 2px 4px rgba(0,0,0,0.5);
            z-index: 9999; color: white; font-size: 16px; font-family: Arial, sans-serif;
            text-align: center;">
    <strong>Dive Stats:</strong> {total_dive_count} Dives | {total_dive_time_hours}h {remaining_minutes}m Underwater
</div>
"""

# Add this HTML to the map using folium
map_dive_locations.get_root().html.add_child(folium.Element(html))


# Save the map
map_dive_locations.save('/Users/mitchtork/website/assets/files/DiveLog.html')
