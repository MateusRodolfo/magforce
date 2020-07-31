# made with magpylib v2.3.0b

from numpy import linspace
from matplotlib.pyplot import show

from setup_magnet_sample.setup_magnet_example import sample, my_collection
import project_helpers.plotting_functions as plotting


# Plotting 1D
xs = linspace(-30, 30, 1000)
ys = linspace(-30, 30, 1000)
zs = linspace(0, 30, 1000)
x, y, z = (0, 0, 0)

# plotting.plot_1D_along_x(xs, y, z, my_collection, sample=sample, BF='BF')
# plotting.plot_1D_along_y(x, ys, z, my_collection, sample=sample, BF='BF')
# plotting.plot_1D_along_z(x, y, zs, my_collection, sample=sample, BF='BF')


# Plotting 2D
xs = linspace(-30, 30, 35)
ys = linspace(-30, 30, 35)
zs = linspace(0, 30, 35)
x, y, z = (0, 0, 0)

# plotting.plot_2D_plane_x(x, ys, zs, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF')
# plotting.plot_2D_plane_y(xs, y, zs, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF')
# plotting.plot_2D_plane_z(xs, ys, z, my_collection, sample=sample, modes=['stream', 'quiver', 'surface'], BF='BF')

# Plotting 3D
xs = linspace(-30, 30, 7)
ys = linspace(-30, 30, 7)
zs = linspace(0, 30, 7)

plotting.plot_3D(xs, ys, zs, my_collection, sample=sample, BF='BF')

show()
