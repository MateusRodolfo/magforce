# made with magpylib v2.3.0b

from matplotlib.pyplot import figure
from numpy import pi

from magpylib.source.magnet import Cylinder
from magpylib import Collection, displaySystem

# Sample Definition
demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]
sample = {'demagnetizing_factor': demagnetizing_factor, 'volume': volume, 'M_saturation': M_saturation}

# Magnet collection definition
m1 = Cylinder(mag=[0, 0, 1000], dim=[5, 20], pos=[0, 0, -10])
my_collection = Collection(m1)

display_collection = 0
if display_collection:
    fig = figure(num='System Display')
    ax = fig.add_subplot(projection='3d')
    displaySystem(my_collection, direc=True, markers=[(0, 0, 0)], suppress=False, subplotAx=ax)


# sample and my_collection will be imported in simulation_unfactorized_example.py
