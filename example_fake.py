#!/usr/bin/env python

from datetime import datetime, timedelta

from readers import reader_basemap_landmask
from readers import reader_ArtificialOceanEddy
from models.oceandrift import OceanDrift

o = OceanDrift(loglevel=0)  # Set loglevel to 0 for debug information

fake_eddy = reader_ArtificialOceanEddy.Reader(2, 62)


reader_basemap = reader_basemap_landmask.Reader(llcrnrlon=-1.5, llcrnrlat=59,
                    urcrnrlon=7, urcrnrlat=64, resolution='h')

o.add_reader([fake_eddy, reader_basemap])

o.use_block = False
o.config['runge_kutta'] = False

# Seeding some particles
lon = 2.0; lat = 63.0; # Close to Station M
o.seed_point(lon, lat, radius=10000, number=10, time=datetime(2015,1,1))

# Running model (until end of driver data)
o.run(steps=100)

# Print and plot results
print o
o.plot(buffer=.5)
print o.history.shape