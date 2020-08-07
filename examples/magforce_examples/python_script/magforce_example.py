from numpy import linspace, pi
from matplotlib.pyplot import show, figure
from magpylib.source.magnet import Cylinder
from magpylib import Collection, displaySystem

import magforce as mgf

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


# Plotting 1D along x, y, z

xs = linspace(-30, 30, 1000)
y = 0
z = 0
# mgf.plot_1D_along_x(xs, y, z, my_collection, sample=sample, BF='BF', saveCSV=False)

x = 0
ys = linspace(-30, 30, 1000)
z = 0
# mgf.plot_1D_along_y(x, ys, z, my_collection, sample=sample, BF='BF', saveCSV=False)

x = 0
y = 0
zs = linspace(0, 30, 1000)
# mgf.plot_1D_along_z(x, y, zs, my_collection, sample=sample, BF='BF', saveCSV=False)


# Plotting 2D on x, y, z plane

x = 0
ys = linspace(-30, 30, 35)
zs = linspace(0, 30, 35)
# mgf.plot_2D_plane_x(x, ys, zs, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF', saveCSV=False)

xs = linspace(-30, 30, 35)
y = 0
zs = linspace(0, 30, 35)
# mgf.plot_2D_plane_y(xs, y, zs, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF', saveCSV=False)

xs = linspace(-30, 30, 35)
ys = linspace(-30, 30, 35)
z = 0
# mgf.plot_2D_plane_z(xs, ys, z, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF', saveCSV=False)


# Plotting 3D

xs = linspace(-30, 30, 7)
ys = linspace(-30, 30, 7)
zs = linspace(0, 30, 7)
# mgf.plot_3D(xs, ys, zs, my_collection, sample=sample, BF='BF', saveCSV=False)

show()
