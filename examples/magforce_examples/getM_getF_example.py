# imports

from numpy import linspace, pi
from matplotlib.pyplot import show
from magpylib import Collection, displaySystem
from magpylib.source.magnet import Cylinder
from magforce import getM, getF


# sample definition

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


# calculate magnetization imposed in the sample if its center was on a given point

point = (0, 0, 0)

M_000_m1 = getM(point, m1, sample)
print(f'M_000_m1 = {M_000_m1}')

M_000_m2 = getM(point, m2, sample)
print(f'M_000_m2 = {M_000_m2}')

M_000_both = getM(point, both, sample)
print(f'M_000_both = {M_000_both}')


# calculate force imposed in the sample if its center was on a given point

point = (0, 0, 0)

F_000_m1 = getF(point, m1, sample)
print(f'F_000_m1 = {F_000_m1}')

F_000_m2 = getF(point, m2, sample)
print(f'F_000_m2 = {F_000_m2}')

F_000_both = getF(point, both, sample)
print(f'F_000_both = {F_000_both}')


# display collection

show()
