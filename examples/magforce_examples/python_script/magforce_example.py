#!/usr/bin/env python
# coding: utf-8

# * user should install dependencies (with pip, conda, whatever you're using)
#     * magforce
#     * magpylib
#     * numpy
#     * matplotlib

# * importing packages

from numpy import linspace, pi
from matplotlib.pyplot import show, figure
from magpylib.source.magnet import Cylinder
from magpylib import Collection, displaySystem

from magforce import plot_1D_along_x, plot_1D_along_y, plot_1D_along_z
from magforce import plot_2D_plane_x, plot_2D_plane_y, plot_2D_plane_z
from magforce import plot_3D


# * defining a cobalt spherical sample, with 4mm diameter, Ms of 1.4e6 A/m and demagnetizing factor of 1/3
# 
# * the sample variable needs to be a dictionary for magforce's functions to work, and it must include the 'demagnetizing_factor', 'volume' and 'M_saturation' keys

demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]

sample = {'demagnetizing_factor': demagnetizing_factor, 
          'volume': volume, 
          'M_saturation': M_saturation}


# * defining a magnet collection
#     * it consists of a single cylinder with a 5mm diameter and 20mm height
#     * its top surface is at z = 0
#     * the my_collection is a magpylib.Collection instance (see [magpylib](https://magpylib.readthedocs.io/en/latest/) for more information)

m1 = Cylinder(mag=[0, 0, 1000],
              dim=[5, 20], 
              pos=[0, 0, -10])

my_collection = Collection(m1)


# * displaying the collection

collection_fig = figure(num='System Display')
collection_ax = collection_fig.add_subplot(projection='3d')

# displaySystem(my_collection,
#               direc=True,
#               markers=[(0, 0, 0)],
#               suppress=False,
#               subplotAx=collection_ax)


# * plotting 1D along x
#   * x from -30 to 30 , 1000 points
#   * y = 0
#   * z = 0

# plot_1D_along_x(xs = linspace(-30, 30, 1000),
#                 y = 0,
#                 z = 0,
#                 collection = my_collection,
#                 sample = sample,
#                 BF = 'BF',
#                 saveCSV = False)


# * plotting 1D along y
#   * x = 0
#   * y from -30 to 30 , 1000 points
#   * z = 0

# plot_1D_along_y(x = 0,
#                 ys = linspace(-30, 30, 1000),
#                 z = 0,
#                 collection = my_collection,
#                 sample = sample,
#                 BF = 'BF',
#                 saveCSV = False)


# * plotting 1D along z
#   * x = 0
#   * y = 0
#   * z from 0 to 30 , 1000 points

# plot_1D_along_z(x = 0,
#                 y = 0,
#                 zs = linspace(0, 30, 1000),
#                 collection = my_collection,
#                 sample = sample,
#                 BF = 'BF',
#                 saveCSV = False)


# * plotting 2D on x plane
#   * x = 0
#   * y from -30 to 30 , 35 points
#   * z from 0 to 30 , 35 points

# plot_2D_plane_x(x = 0,
#                 ys = linspace(-30, 30, 35),
#                 zs = linspace(0, 30, 35),
#                 collection = my_collection,
#                 sample = sample,
#                 modes = ['stream', 'quiver', 'surface'],
#                 BF = 'BF',
#                 saveCSV = False)


# * plotting 2D on y plane
#   * x from -30 to 30 , 35 points
#   * y = 0
#   * z from 0 to 30 , 35 points

# plot_2D_plane_y(xs = linspace(-30, 30, 35),
#                 y = 0,
#                 zs = linspace(0, 30, 35),
#                 collection = my_collection,
#                 sample = sample,
#                 modes = ['stream', 'quiver', 'surface'],
#                 BF = 'BF',
#                 saveCSV = False)


# * plotting 2D on z plane
#   * x from -30 to 30 , 35 points
#   * y from -30 to 30 , 35 points
#   * z = 0

# plot_2D_plane_z(xs = linspace(-30, 30, 35),
#                 ys = linspace(-30, 30, 35),
#                 z = 0,
#                 collection = my_collection,
#                 sample = sample,
#                 modes = ['stream', 'quiver', 'surface'],
#                 BF = 'BF',
#                 saveCSV = False)


# * plotting 3D
#   * x from -30 to 30 , 7 points
#   * y from -30 to 30 , 7 points
#   * z from 0 to 30 , 7 points

# plot_3D(xs = linspace(-30, 30, 7),
#         ys = linspace(-30, 30, 7),
#         zs = linspace(0, 30, 7),
#         collection = my_collection,
#         sample = sample,
#         BF = 'BF',
#         saveCSV = False)

show()