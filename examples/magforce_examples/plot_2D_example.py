# imports

from numpy import linspace, pi
from matplotlib.pyplot import show
from magpylib import Collection, displaySystem
from magpylib.source.magnet import Cylinder
from magforce import plot_2D_plane_x, plot_2D_plane_y, plot_2D_plane_z


# sample Definition

demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]
sample = {'demagnetizing_factor': demagnetizing_factor, 'volume': volume, 'M_saturation': M_saturation}


# magnet collection definition

m1 = Cylinder(mag=[0, 0, 1300],  # 1300mT of magnetization along z axis
              dim=[10, 20],      # 10mm diameter, 20mm height
              pos=[0, 0, -20])   # center is at z = -20mm

m2 = Cylinder(mag=[0, 0, 1300],  # 1300mT of magnetization along z axis
              dim=[10, 20],      # 10mm diameter, 20mm height
              pos=[0, 0, 20])    # center is at z = 20mm

both = Collection(m1, m2)        # arrangement with both magnets


# magnet collection visualisation

displaySystem(both, suppress=True)


# simple study of B along x plane

plot_2D_plane_x(x=0,
                ys=linspace(-10, 10, 30),
                zs=linspace(-5, 5, 30),
                collections={'both': both},
                BF='B')


# simple study of F along y plane

plot_2D_plane_y(xs=linspace(-10, 10, 30),
                y=0,
                zs=linspace(-5, 5, 30),
                collections={'up': m2},
                sample=sample,
                modes=['surface'],
                BF='F')


# using all variables in the plot function for z plane

plot_2D_plane_z(xs=linspace(-10, 10, 30),
                ys=linspace(-10, 10, 30),
                z=0,
                collections={'down': m1,
                             'both': both},
                sample=sample,
                modes=['surface', 'stream'],
                BF='F',
                saveCSV=False,
                showim=True)
