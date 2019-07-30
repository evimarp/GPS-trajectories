# GPS-trajectories
Cartographic projection of 1-year GPS data of 3 migration birds.

## Introduction
The GPS (Global Positioning System) data is everywhere, each GPS coordinate consists of 2 values, latitude and longitude, which represent a point on the globe. Now, the globe is spherical and we find the same problem that the ancient cartographers had.

- What is the best way to draw a sphere in a 2D plane?

A map is a projection of the spherical world on a 2D surface, call it a paper or your phone screen. The earth has latitude, longitude, and shape. When projecting the earth on a 2D surface, one of these 3 dimensions will be necessarily lost. This is another subject, that's out from the scope of this humble repository.

The [Mercator projection (1569)](https://en.wikipedia.org/wiki/Mercator_projection) is the most widely map known and is used to show you the differences of directly plotting GPS data VS a more precise location on a map.

Thanks to Cartopy for allow us to project the migration trajectories into a map.

Graphs:  

- [Direct Plot of GPS trajectories](https://github.com/evimarp/GPS-trajectories/direct_trajectories.pdf)
- [GPS Trajectories using a cartographic projection](https://github.com/evimarp/GPS-trajectories/cartographic_trajectories.pdf)
- [Speed Distribution of each bird](https://github.com/evimarp/GPS-trajectories/Speed%20Distributions.pdf)

You can find the code here: [gps_plot.py](https://github.com/evimarp/GPS-trajectories/gps_plot.py)
