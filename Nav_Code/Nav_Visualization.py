import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd

df = pd.read_csv("../data/Merged10yrdata.csv")
subset = df[['Longitude ', 'Latitude']].dropna()

longitudes = subset['Longitude '].tolist()
latitudes = subset['Latitude'].tolist()

fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

ax.scatter(longitudes, latitudes, color='red', marker='o', 
           transform=ccrs.PlateCarree(), s=10, alpha=0.7)
ax.gridlines(draw_labels=True)
plt.title('Flight Incidents: Longitude vs Latitude')
plt.savefig('world_map_with_points.png', dpi=300, bbox_inches='tight')
