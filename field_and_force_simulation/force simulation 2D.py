from numpy import linspace, array, round, zeros, sqrt, log, meshgrid
from matplotlib.pyplot import figure, show
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


#functions for plotting
def plotx(x, ys, zs, mode='q'):
    """Evaluates the value of x and plots the force in that plane
    mode should be s, q or sq for plotting streamplot or quiver"""

    POS = array([(eval(str(x)), y, z) for z in zs for y in ys])

    FOR = array([getF(c, pos) for pos in POS])

    POS = POS.reshape(len(ys), len(zs), 3)
    POSy = POS[:, :, 1]
    POSz = POS[:, :, 2]

    FOR = FOR.reshape(len(ys), len(zs), 3)
    FORy = FOR[:, :, 1]
    FORz = FOR[:, :, 2]

    if 's' in mode:
        fig_s = figure(num=f'''x = {x} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''x = {x}''')
        ax_s.streamplot(POSy, POSz, FORy, FORz, density=3)
        ax_s.set_xlabel('y')
        ax_s.set_ylabel('z')

    if 'q' in mode:
        fig_q = figure(num=f'''x = {x} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''x = {x}''')
        Fy, Fz = normal(FORy, FORz)
        ax_q.quiver(POSy, POSz, Fy, Fz, units='xy')
        ax_q.set_xlabel('y')
        ax_q.set_ylabel('z')


def ploty(xs, y, zs, mode='q'):
    """Evaluates the value of y and plots the force in that plane
    mode should be s, q or sq for plotting streamplot or quiver"""

    POS = array([(x, eval(str(y)), z) for z in zs for x in xs])

    FOR = array([getF(c, pos) for pos in POS])

    POS = POS.reshape(len(xs), len(zs), 3)
    POSx = POS[:, :, 0]
    POSz = POS[:, :, 2]

    FOR = FOR.reshape(len(xs), len(zs), 3)
    FORx = FOR[:, :, 0]
    FORz = FOR[:, :, 2]

    if 's' in mode:
        fig_s = figure(num=f'''y = {y} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''y = {y}''')
        ax_s.streamplot(POSx, POSz, FORx, FORz, density=3)
        ax_s.set_xlabel('x')
        ax_s.set_ylabel('z')

    if 'q' in mode:
        fig_q = figure(num=f'''y = {y} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''y = {y}''')
        Fx, Fz = normal(FORx, FORz)
        ax_q.quiver(POSx, POSz, Fx, Fz, units='xy')
        ax_q.set_xlabel('x')
        ax_q.set_ylabel('z')


def plotz(xs, ys, z, mode='q'):
    """Evaluates the value of z and plots the force in that plane
    mode should be s, q or sq for plotting streamplot or quiver"""

    POS = array([(x, y, eval(str(z))) for y in ys for x in xs])

    FOR = array([getF(c, pos) for pos in POS])

    POS = POS.reshape(len(xs), len(ys), 3)
    POSx = POS[:, :, 0]
    POSy = POS[:, :, 1]

    FOR = FOR.reshape(len(xs), len(ys), 3)
    FORx = FOR[:, :, 0]
    FORy = FOR[:, :, 1]

    if 's' in mode:
        fig_s = figure(num=f'''z = {z} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''z = {z}''')
        ax_s.streamplot(POSx, POSy, FORx, FORy, density=3)
        ax_s.set_xlabel('x')
        ax_s.set_ylabel('y')

    if 'q' in mode:
        fig_q = figure(num=f'''z = {z} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''z = {z}''')
        Fx, Fy = normal(FORx, FORy)
        ax_q.quiver(POSx, POSy, Fx, Fy, units='xy')
        ax_q.set_xlabel('x')
        ax_q.set_ylabel('y')


# creation of 3D space
# parts_x = 7
# parts_y = 7
# parts_z = 7
# limit_x = 10
# limit_y = 10
# limit_z = 10
xs = linspace(-10, 10, 35)
ys = linspace(-10, 10, 35)
zs = linspace(-10, 10, 35)

# plane x = 0
plotx(0, ys, zs)

# plane y = 0
ploty(xs, 0, zs, mode='sq')

# plane z = 0
plotz(xs, ys, 0, mode='q')

# plane y = x
# ploty(xs, 'x', zs, mode='q')     # equals to default

print(f'''{datetime.now() - startTime} total runtime''')
show()
