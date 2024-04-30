import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load your CSV file containing dive data
dive_data = pd.read_csv('/Users/mitchtork/website/assets/files/DiveLog.csv')

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
# Save the map to an HTML file
map_dive_locations.save('/Users/mitchtork/website/assets/files/DiveLog.html')
