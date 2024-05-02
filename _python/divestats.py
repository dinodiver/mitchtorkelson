import pandas as pd

# Load your CSV file containing dive data
dive_data = pd.read_csv('/Users/mitchtork/website/assets/files/DiveLog.csv')

# Calculate total number of dives
total_dive_count = dive_data['Dive #'].max()  # Assuming Dive # is a unique identifier for each dive

# Calculate total dive time in minutes
total_dive_time_minutes = dive_data['Dive Time (min)'].sum()

# Convert total dive time to hours and remaining minutes
total_dive_time_hours = total_dive_time_minutes // 60
remaining_minutes = total_dive_time_minutes % 60

print("Total Number of Dives:", total_dive_count)
print(f"Total Dive Time: {total_dive_time_hours} hours and {remaining_minutes} minutes")
