import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

import matplotlib.font_manager as font_manager

# Add every font at the specified location
font_dir = ['Raleway']
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)

# Set font family globally
rcParams['font.family'] = 'Raleway'

gdf = gpd.read_file('ne_110m_admin_1_states_provinces/ne_110m_admin_1_states_provinces.shp')

print(gdf.columns)

df = pd.read_csv('Business Cost Index - Sheet1.csv')

merged = gdf.merge(df, left_on='name', right_on='State', how='outer')

plt.style.use('dark_background')
merged.plot(column='Business cost affordability score / 10', cmap='YlOrRd', legend=True, legend_kwds={'location': 'bottom'})

plt.title('Business Cost Index (out of 10) by State', fontweight="bold")

plt.xticks([])
plt.yticks([])
plt.savefig('Business Cost Index graph.png', transparent=True)


