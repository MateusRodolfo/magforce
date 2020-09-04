# imports

from numpy import linspace, pi
from matplotlib.pyplot import show
from magpylib import Collection, displaySystem
from magpylib.source.magnet import Cylinder
from magforce import plot_1D_along_x, plot_1D_along_y, plot_1D_along_z


# sample definition

demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]

sample = {'demagnetizing_factor': demagnetizing_factor,
          'volume': volume,
          'M_saturation': M_saturation}


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


# simple study of B along x axis

plot_1D_along_x(xs=linspace(-10, 10, 500),
                y=0,
                z=0,
                collections={'both': both},
                BF='B')


# simple study of F along y axis

plot_1D_along_y(x=0,
                ys=linspace(-5, 5, 500),
                z=0,
                collections={'up': m2},
                sample=sample,
                BF='F')


# using all variables in the plot function for z direction

plot_1D_along_z(x=1,
                y=2,
                zs=linspace(-5, 5, 500),
                collections={'down': m1,
                             'up': m2,
                             'both': both},
                sample=sample,
                BF='BF',
                saveCSV=False,
                showim=True)


# show everything

show()
