from numpy import linspace, array, round, zeros, sqrt
from matplotlib.pyplot import figure, show, tight_layout
from matplotlib.patches import Rectangle, Circle
from datetime import datetime
from magnet_collection import c

# start timer
startTime = datetime.now()
print(f'''{datetime.now()} : starting simulation\n''')


# functions for calculations
def normal(Fx, Fy):
    """Normalizes the vectors size for 2D plotting
    Accepts 1D arrays as input"""

    Fxn = Fx / sqrt(Fx ** 2 + Fy ** 2)
    Fyn = Fy / sqrt(Fx ** 2 + Fy ** 2)

    return Fxn, Fyn


def jac(foo, x, y, z):
    """from a point xyz and the collection of magnets returns a 3x3 jacobian matrix on that point
    works with 6 auxiliar points, in x,y,z +- infinitesimal
    function foo takes as argument an 1d array like [x, y, z]"""

    delta = 0.0000001  # infinitesimal

    dd = zeros((3, 3))  # creation of 3x3 matrix of zeros, to have values replaced

    fxm = foo([x - delta, y, z])  # point x - delta
    fxp = foo([x + delta, y, z])  # point x + delta
    fym = foo([x, y - delta, z])  # point y - delta
    fyp = foo([x, y + delta, z])  # point y + delta
    fzm = foo([x, y, z - delta])  # point z - delta
    fzp = foo([x, y, z + delta])  # point z + delta

    # derivative using central difference formula

    delta2 = 2 * delta

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

    dd = jac(collection.getB, x, y, z)

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


# functions for plotting
def plotx(xs, y, z):
    """Evaluates the value of y and z as planes and plots the values of Fx, Fy and Fz along the x axis"""

    POS = array([(x, eval(str(y)), eval(str(z))) for x in xs])

    FOR = array([getF(c, pos) for pos in POS])
    FORx = FOR[:, 0]
    FORy = FOR[:, 1]
    FORz = FOR[:, 2]

    fig = figure(num=f'''F for y = {y}, z = {z}''')
    ax_Fx = fig.add_subplot(221, title=f'''Fx along x axis, y = {y}, z = {z}''')
    ax_Fx.plot(zs, FORx, 'r')
    ax_Fx.set_xlabel('x []')
    ax_Fx.set_ylabel('Fx []')

    ax_Fy = fig.add_subplot(222, title=f'''Fy along x axis, y = {y}, z = {z}''')
    ax_Fy.plot(zs, FORy, 'g')
    ax_Fy.set_xlabel('x []')
    ax_Fy.set_ylabel('Fy []')

    ax_Fz = fig.add_subplot(223, title=f'''Fz along x axis, y = {y}, z = {z}''')
    ax_Fz.plot(zs, FORz, 'b')
    ax_Fz.set_xlabel('x []')
    ax_Fz.set_ylabel('Fz []')

    ax_all = fig.add_subplot(224, title=f'''Force along x axis, y = {y}, z = {z}''')
    ax_all.plot(zs, FORx, 'r', label='Fx')
    ax_all.plot(zs, FORy, 'g', label='Fy')
    ax_all.plot(zs, FORz, 'b', label='Fz')
    ax_all.set_xlabel('x []')
    ax_all.set_ylabel('Force []')

    ax_all.legend()
    tight_layout()


def ploty(x, ys, z):
    """Evaluates the value of x and z as planes and plots the values of Fx, Fy and Fz along the y axis"""

    POS = array([(eval(str(x)), ys, eval(str(z))) for y in ys])

    FOR = array([getF(c, pos) for pos in POS])
    FORx = FOR[:, 0]
    FORy = FOR[:, 1]
    FORz = FOR[:, 2]

    fig = figure(num=f'''F for x = {x}, z = {z}''')
    ax_Fx = fig.add_subplot(221, title=f'''Fx along y axis, x = {x}, z = {z}''')
    ax_Fx.plot(zs, FORx, 'r')
    ax_Fx.set_xlabel('y []')
    ax_Fx.set_ylabel('Fx []')

    ax_Fy = fig.add_subplot(222, title=f'''Fy along y axis, x = {x}, z = {z}''')
    ax_Fy.plot(zs, FORy, 'g')
    ax_Fy.set_xlabel('y []')
    ax_Fy.set_ylabel('Fy []')

    ax_Fz = fig.add_subplot(223, title=f'''Fz along y axis, x = {x}, z = {z}''')
    ax_Fz.plot(zs, FORz, 'b')
    ax_Fz.set_xlabel('y []')
    ax_Fz.set_ylabel('Fz []')

    ax_all = fig.add_subplot(224, title=f'''Force along y axis, x = {x}, z = {z}''')
    ax_all.plot(zs, FORx, 'r', label='Fx')
    ax_all.plot(zs, FORy, 'g', label='Fy')
    ax_all.plot(zs, FORz, 'b', label='Fz')
    ax_all.set_xlabel('y []')
    ax_all.set_ylabel('Force []')

    ax_all.legend()
    tight_layout()


def plotz(x, y, zs):
    """Evaluates the value of x and y as planes and plots the values of Fx, Fy and Fz along the z axis"""

    POS = array([(eval(str(x)), eval(str(y)), z) for z in zs])

    FOR = array([getF(c, pos) for pos in POS])
    FORx = FOR[:, 0]
    FORy = FOR[:, 1]
    FORz = FOR[:, 2]

    fig = figure(num=f'''F for x = {x}, y = {y}''')
    ax_Fx = fig.add_subplot(221, title=f'''Fx along z axis, x = {x}, y = {y}''')
    ax_Fx.plot(zs, FORx, 'r')
    ax_Fx.set_xlabel('z []')
    ax_Fx.set_ylabel('Fx []')

    ax_Fy = fig.add_subplot(222, title=f'''Fy along z axis, x = {x}, y = {y}''')
    ax_Fy.plot(zs, FORy, 'g')
    ax_Fy.set_xlabel('z []')
    ax_Fy.set_ylabel('Fy []')

    ax_Fz = fig.add_subplot(223, title=f'''Fz along z axis, x = {x}, y = {y}''')
    ax_Fz.plot(zs, FORz, 'b')
    ax_Fz.set_xlabel('z []')
    ax_Fz.set_ylabel('Fz []')

    ax_all = fig.add_subplot(224, title=f'''Force along z axis, x = {x}, y = {y}''')
    ax_all.plot(zs, FORx, 'r', label='Fx')
    ax_all.plot(zs, FORy, 'g', label='Fy')
    ax_all.plot(zs, FORz, 'b', label='Fz')
    ax_all.set_xlabel('z []')
    ax_all.set_ylabel('Force []')

    ax_all.legend()
    tight_layout()


# x = 0 y = 0

x, y = 0, 0
zs = linspace(0, 10, 1000)
plotz(x, y, zs)

# x = 0 y = 1

x, y = 0, 1
zs = linspace(0, 10, 1000)
plotz(x, y, zs)

# y = 0 z = 0

y, z = 0, 0
xs = linspace(0, 10, 1000)
plotx(xs, y, z)

print(f'''{datetime.now() - startTime} total runtime''')
show()
