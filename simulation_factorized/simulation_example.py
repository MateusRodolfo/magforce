# made with magpylib v2.3.0b

from numpy import linspace
from matplotlib.pyplot import show

from setup_magnet_sample.setup_magnet_sample_example import sample, my_collection
import project_helpers.plotting_functions as pf


# Plotting 1D
xs = linspace(-30, 30, 1000)
y, z = (0, 0)
# pf.plot_1D_along_x(xs, y, z, my_collection, sample=sample, BF='BF', saveCSV=False)

ys = linspace(-30, 30, 1000)
x, z = (0, 0)
# pf.plot_1D_along_y(x, ys, z, my_collection, sample=sample, BF='BF', saveCSV=False)

zs = linspace(0, 30, 1000)
y, z = (0, 0)
# pf.plot_1D_along_z(x, y, zs, my_collection, sample=sample, BF='BF', saveCSV=False)


# Plotting 2D
ys = linspace(-30, 30, 35)
zs = linspace(0, 30, 35)
x = 0
# pf.plot_2D_plane_x(x, ys, zs, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF', saveCSV=False)

xs = linspace(-30, 30, 35)
zs = linspace(0, 30, 35)
y = 0
# pf.plot_2D_plane_y(xs, y, zs, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF', saveCSV=False)

xs = linspace(-30, 30, 35)
ys = linspace(-30, 30, 35)
z = 0
# pf.plot_2D_plane_z(xs, ys, z, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF', saveCSV=False)

# Plotting 3D
xs = linspace(-30, 30, 7)
ys = linspace(-30, 30, 7)
zs = linspace(0, 30, 7)

# pf.plot_3D(xs, ys, zs, my_collection, sample=sample, BF='BF', saveCSV=False)

show()
