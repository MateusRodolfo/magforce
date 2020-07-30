from numpy import linspace, meshgrid, array, gradient, round, zeros, sqrt
from magpylib.source.magnet import Cylinder
from magpylib import Collection, displaySystem
from matplotlib.pyplot import figure, show
from matplotlib.patches import Rectangle, Circle

from datetime import datetime

startTime = datetime.now()


def normal(Fx, Fy):
    Fxn = Fx / sqrt(Fx ** 2 + Fy ** 2)
    Fyn = Fy / sqrt(Fx ** 2 + Fy ** 2)

    return Fxn, Fyn


def getBmesh(collection, X, Y, Z):  # Example vector field
    I, J, K = X.shape
    BX = zeros((I, J, K))
    BY = zeros((I, J, K))
    BZ = zeros((I, J, K))
    for k in range(K):
        for j in range(J):
            for i in range(I):
                x, y, z = X[i, j, k], Y[i, j, k], Z[i, j, k]
                Bx, By, Bz = collection.getB([x, y, z])
                BX[i, j, k] = Bx
                BY[i, j, k] = By
                BZ[i, j, k] = Bz
    return array([BX, BY, BZ])


def jacB(collection, x, y, z):
    delta = 0.01
    xs = linspace(x - delta, x + delta, 3)
    ys = linspace(y - delta, y + delta, 3)
    zs = linspace(z - delta, z + delta, 3)

    dd = zeros((3, 3))

    fp0 = collection.getB([x, y, z])
    fxm = collection.getB([x - delta, y, z])
    fxp = collection.getB([x + delta, y, z])
    fym = collection.getB([x, y - delta, z])
    fyp = collection.getB([x, y + delta, z])
    fzm = collection.getB([x, y, z - delta])
    fzp = collection.getB([x, y, z + delta])

    dx = array([fxm, fp0, fxp])
    dd[0, 0] = gradient(dx[:, 0], xs)[1]  # dUdx
    dd[1, 0] = gradient(dx[:, 1], xs)[1]  # dVdx
    dd[2, 0] = gradient(dx[:, 2], xs)[1]  # dWdx

    dy = array([fym, fp0, fyp])
    dd[0, 1] = gradient(dy[:, 0], ys)[1]  # dUdy
    dd[1, 1] = gradient(dy[:, 1], ys)[1]  # dVdy
    dd[2, 1] = gradient(dy[:, 2], ys)[1]  # dWdy

    dz = array([fzm, fp0, fzp])
    dd[0, 2] = gradient(dz[:, 0], zs)[1]  # dUdz
    dd[1, 2] = gradient(dz[:, 1], zs)[1]  # dVdz
    dd[2, 2] = gradient(dz[:, 2], zs)[1]  # dWdz

    dd = round(dd, 5)

    return dd


def getF(collection, point):
    x, y, z = point

    M = collection.getB([x, y, z])
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


# fixed magnet parameters
M = [0, 0, 500]  # magnetization (Mx, My, Mz)
d = 1
H = 2
dim = [d, H]
magnet = Cylinder(mag=M, dim=dim, pos=[0, 0, 0])
c = Collection(magnet)

from magnet_collection import c

# creation of 3D space
parts = 25
limit = 10
xs = linspace(-limit, limit, parts)
ys = linspace(-limit, limit, parts)
zs = linspace(-limit, limit, parts)

POS = array([(x, y, z) for x in xs for y in ys for z in zs])
FOR = array([getF(c, pos) for pos in POS])

POS = POS.reshape(parts, parts, parts, 3)
FOR = FOR.reshape(parts, parts, parts, 3)

POSx = POS[:, :, :, 0]
POSy = POS[:, :, :, 1]
POSz = POS[:, :, :, 2]

FORx = FOR[:, :, :, 0]
FORy = FOR[:, :, :, 1]
FORz = FOR[:, :, :, 2]

# plotting
# fig3d = figure(num='3D')
# ax = fig3d.add_subplot(projection='3d')
# ax.quiver(POSx, POSy, POSz, FORx, FORy, FORz, normalize=True)

fig2d = figure(num='x = 0')
ax = fig2d.add_subplot(aspect=1, title='x = 0')
p = int(parts / 2)
Py, Pz = POSy[p, :, :], POSz[p, :, :]
Fy, Fz = normal(FORy[p, :, :], FORz[p, :, :])
ax.quiver(Py, Pz, Fy, Fz)
ax.add_artist(Rectangle((-d/2, -H/2), d, H, color='magenta', alpha=1, fill=False))

fig2d = figure(num='y = 0')
ax = fig2d.add_subplot(aspect=1, title='y = 0')
p = int(parts / 2)
Px, Pz = POSx[:, p, :], POSz[:, p, :]
Fx, Fz = normal(FORx[:, p, :], FORz[:, p, :])
ax.quiver(Px, Pz, Fx, Fz)
ax.add_artist(Rectangle((-d/2, -H/2), d, H, color='magenta', alpha=1, fill=False))

fig2d = figure(num='z = 0')
ax = fig2d.add_subplot(aspect=1, title='z = 0')
p = int(parts / 2)
Px, Py = POSx[:, :, p], POSy[:, :, p]
Fx, Fy = normal(FORx[:, :, p], FORy[:, :, p])
ax.quiver(Px, Py, Fx, Fy)
ax.add_artist(Circle((0, 0), d/2, color='magenta', alpha=1, fill=False))

print(datetime.now() - startTime)
show()
