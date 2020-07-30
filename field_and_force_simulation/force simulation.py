from numpy import linspace, array, round, zeros, sqrt
from matplotlib.pyplot import figure, show
from matplotlib.patches import Rectangle, Circle
from datetime import datetime
from magnet_collection import c

# start timer
startTime = datetime.now()
print(f'''{datetime.now()} : starting simulation\n''')

# functions
def normal(Fx, Fy):
    """Normalizes the vectors size for 2D plotting
    Accepts 1D arrays as input"""

    Fxn = Fx / sqrt(Fx ** 2 + Fy ** 2)
    Fyn = Fy / sqrt(Fx ** 2 + Fy ** 2)

    return Fxn, Fyn


def jacB(collection, x, y, z):
    """from a point xyz and the collection of magnets returns a 3x3 jacobian matrix on that point
    works with 6 auxiliar points, in x,y,z +- infinitesimal"""

    delta = 0.0000001                          # infinitesimal

    dd = zeros((3, 3))                         # creation of 3x3 matrix of zeros, to have values replaced

    fxm = collection.getB([x - delta, y, z])   # point x - delta
    fxp = collection.getB([x + delta, y, z])   # point x + delta
    fym = collection.getB([x, y - delta, z])   # point y - delta
    fyp = collection.getB([x, y + delta, z])   # point y + delta
    fzm = collection.getB([x, y, z - delta])   # point z - delta
    fzp = collection.getB([x, y, z + delta])   # point z + delta

    # derivative using central difference formula

    delta2 = 2*delta

    dd[0, 0] = (fxp[0] - fxm[0]) / delta2  # dUdx
    dd[1, 0] = (fxp[1] - fxm[1]) / delta2  # dVdx
    dd[2, 0] = (fxp[2] - fxm[2]) / delta2  # dWdx

    dd[0, 1] = (fyp[0] - fym[0]) / delta2  # dUdy
    dd[1, 1] = (fyp[1] - fym[1]) / delta2  # dVdy
    dd[2, 1] = (fyp[2] - fym[2]) / delta2  # dWdy

    dd[0, 2] = (fzp[0] - fzm[0]) / delta2  # dUdz
    dd[1, 2] = (fzp[1] - fzm[1]) / delta2  # dVdz
    dd[2, 2] = (fzp[2] - fzm[2]) / delta2  # dWdz

    dd = round(dd, 5)

    return dd


def getF(collection, point):
    """gets the magnetic force"""
    x, y, z = point

    B = collection.getB([x, y, z])
    M = B
    Mx, My, Mz = M

    dd = jacB(collection, x, y, z)

    dUdx = dd[0, 0]
    dUdy = dd[0, 1]
    dUdz = dd[0, 2]

    dVdx = dd[1, 0]
    dVdy = dd[1, 1]
    dVdz = dd[1, 2]

    dWdx = dd[2, 0]
    dWdy = dd[2, 1]
    dWdz = dd[2, 2]

    Fx = Mx * dUdx + My * dVdx + Mz * dWdx
    Fy = Mx * dUdy + My * dVdy + Mz * dWdy
    Fz = Mx * dUdz + My * dVdz + Mz * dWdz

    return array([Fx, Fy, Fz])

# creation of 3D space
print(f'''{datetime.now()} : creating 3D space\n''')
parts_x = 25
parts_y = 25
parts_z = 25
limit_x = 10
limit_y = 10
limit_z = 10
xs = linspace(-limit_x, limit_x, parts_x)
ys = linspace(-limit_y, limit_y, parts_y)
zs = linspace(-limit_z, limit_z, parts_z)
POS = array([(x, y, z) for x in xs for y in ys for z in zs])

# calculation of force field
print(f'''{datetime.now()} : calculating force field\n''')
FOR = array([getF(c, pos) for pos in POS])

POS = POS.reshape(parts_x, parts_y, parts_z, 3)
POSx = POS[:, :, :, 0]
POSy = POS[:, :, :, 1]
POSz = POS[:, :, :, 2]

FOR = FOR.reshape(parts_x, parts_y, parts_z, 3)
FORx = FOR[:, :, :, 0]
FORy = FOR[:, :, :, 1]
FORz = FOR[:, :, :, 2]

# plotting
print(f'''{datetime.now()} : plotting\n''')

# 3D
# fig3d = figure(num='3D')
# ax = fig3d.add_subplot(projection='3d')
# ax.quiver(POSx, POSy, POSz, FORx, FORy, FORz, normalize=True)

# 2D
# x = 0
fig2d = figure(num='x = 0')
ax = fig2d.add_subplot(aspect=1, title='x = 0')
p = int(parts_x / 2)
Py, Pz = POSy[p, :, :], POSz[p, :, :]
Fy, Fz = normal(FORy[p, :, :], FORz[p, :, :])
ax.quiver(Py, Pz, Fy, Fz, units='xy')
# ax.add_artist(Rectangle((-d/2, -H/2), d, H, color='magenta', alpha=1, fill=False))

# y = 0
fig2d = figure(num='y = 0')
ax = fig2d.add_subplot(aspect=1, title='y = 0')
p = int(parts_x / 2)
Px, Pz = POSx[:, p, :], POSz[:, p, :]
Fx, Fz = normal(FORx[:, p, :], FORz[:, p, :])
ax.quiver(Px, Pz, Fx, Fz, units='xy')
# ax.add_artist(Rectangle((-d/2, -H/2), d, H, color='magenta', alpha=1, fill=False))

# z = 0
fig2d = figure(num='z = 0')
ax = fig2d.add_subplot(aspect=1, title='z = 0')
p = int(parts_x / 2)
Px, Py = POSx[:, :, p], POSy[:, :, p]
Fx, Fy = normal(FORx[:, :, p], FORy[:, :, p])
ax.quiver(Px, Py, Fx, Fy, units='xy')
# ax.add_artist(Circle((0, 0), d/2, color='magenta', alpha=1, fill=False))

print(f'''{datetime.now()} : finish\n''')
print(f'''{datetime.now() - startTime} total runtime''')
show()
