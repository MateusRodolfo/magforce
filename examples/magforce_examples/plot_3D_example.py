# imports

from numpy import linspace, pi
from matplotlib.pyplot import show
from magpylib import Collection, displaySystem
from magpylib.source.magnet import Cylinder
from magforce import plot_3D


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


# 3D plot of B and F in a 3D space

plot_3D(xs=linspace(-10, 10, 9),
        ys=linspace(-10, 10, 9),
        zs=linspace(-20, 20, 9),
        collections={'z-20': m1,
                     'both': both},
        sample=sample,
        BF='BF',
        saveCSV=False,
        showim=True)
