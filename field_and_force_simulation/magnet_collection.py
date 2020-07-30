from magpylib.source.magnet import Cylinder
from magpylib.source.current import Circular
from magpylib import Collection, displaySystem
from matplotlib.pyplot import figure

# one cylinder

# M = [0, 0, 500]  # magnetization (Mx, My, Mz)
# d = 1
# H = 2
# dim = [d, H]
# magnet = Cylinder(mag=M, dim=dim, pos=[0, 0, 0])

# c = Collection(magnet)

# 4 cylinders pointing center

# M = [0, 0, 500]  # magnetization
# D = [1, 2]  # dimension
#
# m1 = Cylinder(mag=M, dim=D, pos=[0, -5, 0], angle=-90, axis=[1, 0, 0])
# m2 = Cylinder(mag=M, dim=D, pos=[0, -5, 0], angle=-90, axis=[1, 0, 0])
# m3 = Cylinder(mag=M, dim=D, pos=[0, -5, 0], angle=-90, axis=[1, 0, 0])
# m4 = Cylinder(mag=M, dim=D, pos=[0, -5, 0], angle=-90, axis=[1, 0, 0])
#
# m2.rotate(90, [0, 0, 1], [0, 0, 0])
# m3.rotate(180, [0, 0, 1], [0, 0, 0])
# m4.rotate(270, [0, 0, 1], [0, 0, 0])
#
# c = Collection(m1, m2, m3, m4)

# 2 cylinders pointing up

# M = [0, 0, 500]  # magnetization
# D = [1, 2]  # dimension
#
# m1 = Cylinder(mag=M, dim=D, pos=[0, 0, -5], angle=0, axis=[1, 0, 0])
# m2 = Cylinder(mag=M, dim=D, pos=[0, 0, +5], angle=0, axis=[1, 0, 0])
#
# c = Collection(m1, m2)

# one turn coil

dim = 5 # coils diameter
coil = Circular(curr=10,dim=dim,pos=[0,0,0])
c = Collection(coil)

# multiple turns coil

# dim = 10 # coils diametre
# H = 20 # hieght
# num = 5 # coil turns
# coil = [Circular(curr=10,dim=dim,pos=[0,0,z]) for z in np.linspace( -H/2,H/2,num)]

# c = Collection(coil)

display = 0
if display:
    fig = figure(num='System Display')
    ax = fig.add_subplot(projection='3d')
    displaySystem(c, direc=True, markers=[(0, 0, 0)], suppress=False, subplotAx=ax)