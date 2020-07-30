from magpylib.source.magnet import Cylinder
from magpylib.source.current import Circular
from magpylib import Collection, displaySystem

# cylinder
M = [0, 0, 500]  # magnetization (Mx, My, Mz)
d = 1
H = 2
dim = [d, H]
magnet = Cylinder(mag=M, dim=dim, pos=[0, 0, 0])
c = Collection(magnet)

# one coil
# dim = 10 # coils diameter
# num = 5 # coil turns
# coil = Circular(curr=10,dim=dim,pos=[0,0,0])
# c = Collection(coil)

# one coil
# dim = 10 # coils diametre
# H = 20 # hieght
# num = 5 # coil turns
# coil = [Circular(curr=10,dim=dim,pos=[0,0,z]) for z in np.linspace( -H/2,H/2,num)]
# c = Collection(coil)