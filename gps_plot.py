""" This code plot the trayectories of 3 bird
The GPS coordinates will have distortions because is 2D representation
of spheric GPS information
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

trajectories = pd.read_csv('data/bird_tracking.csv')

bird_names = trajectories.bird_name.unique()

plt.figure(figsize=(7, 7))

for bird_name in bird_names:
    tracks = trajectories.bird_name == bird_name
    x = trajectories[tracks].longitude
    y = trajectories[tracks].latitude
    plt.plot(x, y, '.', label=bird_name)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc="lower right")
plt.title('GPS Trajectories of 3 birds with distortions')
plt.savefig("direct_trajectories.pdf")

# Now same data but into a cartographic projection
plt.figure(figsize=(10, 10))
projection = ccrs.Mercator()
ax = plt.axes(projection=projection)
ax.set_extent((-25, 20, 52, 10))

# add the maps elements
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.RIVERS)

for bird_name in bird_names:
    tracks = trajectories.bird_name == bird_name
    x = trajectories[tracks].longitude
    y = trajectories[tracks].latitude
    ax.plot(x, y, '.', label=bird_name, transform=ccrs.Geodetic())
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc="upper left")
plt.title('Cartographic GPS Trajectories of 3 birds')
plt.savefig("cartographic_trajectories.pdf")


# Distribution of velocities
len_birds = len(bird_names)
fig, axes = plt.subplots(nrows=1, ncols=len_birds, figsize=(8, 5))
for i in range(len_birds):
    bird_name = bird_names[i]
    ax = axes[i]
    tracks = trajectories.bird_name == bird_name
    speed = trajectories.speed_2d[tracks]
    # Remove nans
    speed = speed[-speed.isna()]
    ax.hist(speed,
            bins=np.linspace(0, 20, 15),
            density=True)
    ax.set_xlabel('2D speed (m/s)')
    ax.set_ylabel('Frequency')
    ax.set_title('{}\'s speed'.format(bird_name))
    ax.set_ylim(0, 0.43)

plt.savefig('Speed Distributions.pdf')