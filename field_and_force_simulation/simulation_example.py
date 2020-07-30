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

# plotting.plot_1D_Bxyz_x(xs, y, z, my_collection)
# plotting.plot_1D_Bxyz_y(x, ys, z, my_collection)
# plotting.plot_1D_Bxyz_z(x, y, zs, my_collection)

# plotting.plot_1D_Fxyz_x(xs, y, z, my_collection, sample)
# plotting.plot_1D_Fxyz_y(x, ys, z, my_collection, sample)
# plotting.plot_1D_Fxyz_z(x, y, zs, my_collection, sample)

# Plotting 2D
xs = linspace(-30, 30, 35)
ys = linspace(-30, 30, 35)
zs = linspace(0, 30, 35)
x, y, z = (0, 0, 0)

# plotting.plot_2D_Byz_x(x, ys, zs, my_collection, modes=['stream', 'quiver'])
# plotting.plot_2D_Bxz_y(xs, y, zs, my_collection, modes=['stream', 'quiver'])
# plotting.plot_2D_Bxy_z(xs, ys, z, my_collection, modes=['stream', 'quiver'])

# plotting.plot_2D_Fyz_x(x, ys, zs, my_collection, sample, modes=['stream', 'quiver'])
# plotting.plot_2D_Fxz_y(xs, y, zs, my_collection, sample, modes=['stream', 'quiver'])
plotting.plot_2D_Fxy_z(xs, ys, z, my_collection, sample, modes=['stream', 'quiver'])

show()
