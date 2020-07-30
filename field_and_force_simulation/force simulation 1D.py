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

# creation of 1D space
x = 0.1
y = 0
z = 0
axis_values = linspace(1, 10, 1001)

POS = array([(x,y,var) for var in axis_values])

FOR = array([getF(c, pos) for pos in POS])
FORx = FOR[:,0]
FORy = FOR[:,1]
FORz = FOR[:,2]

# plotting
fig = figure(num='Fx')
ax = fig.add_subplot(title=f'''Fx along z axis, x = {x}, y = {y}''')
ax.plot(axis_values,FORx,'r', label='Fx')
ax.set_ylabel('Fx []')
ax.set_xlabel('z []')
fig.legend()

fig = figure(num='Fy')
ax = fig.add_subplot(title=f'''Fy along z axis, x = {x}, y = {y}''')
ax.plot(axis_values,FORy,'g', label='Fy')
ax.set_ylabel('Fy []')
ax.set_xlabel('z []')
fig.legend()

fig = figure(num='Fz')
ax = fig.add_subplot(title=f'''Fz along z axis, x = {x}, y = {y}''')
ax.plot(axis_values,FORz,'b', label='Fz')
ax.set_ylabel('Fz []')
ax.set_xlabel('z []')
fig.legend()

fig = figure(num='Fx, Fy, Fz')
ax = fig.add_subplot(title=f'''Force along z axis, x = {x}, y = {y}''')
ax.plot(axis_values,FORx,'r', label='Fx')
ax.plot(axis_values,FORy,'g', label='Fy')
ax.plot(axis_values,FORz,'b', label='Fz')
ax.set_ylabel('Force []')
ax.set_xlabel('z []')
fig.legend()

print(f'''{datetime.now() - startTime} total runtime''')
show()
