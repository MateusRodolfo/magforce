# made with magpylib v2.3.0b
from numpy import array, column_stack
from matplotlib.pyplot import figure, tight_layout, cm

from project_helpers.calculation_functions import normalize, getF


# functions for plotting B 1D

def plot_1D_Bxyz_x(xs, y, z, my_collection):
    """Evaluates the value of y and z as planes and plots the values of Bx, By and Bz along the x axis"""

    POS = array([(x, eval(str(y)), eval(str(z))) for x in xs])

    Bfield = array([my_collection.getB(pos) for pos in POS])
    Bfieldx = Bfield[:, 0]
    Bfieldy = Bfield[:, 1]
    Bfieldz = Bfield[:, 2]

    fig = figure(num=f'''B for y = {y}, z = {z}''')
    ax_Fx = fig.add_subplot(221, title=f'''Bx along x axis, y = {y}, z = {z}''')
    ax_Fx.plot(xs, Bfieldx, 'r')
    ax_Fx.set_xlabel('x [mm]')
    ax_Fx.set_ylabel('Bx [mT]')

    ax_Fy = fig.add_subplot(222, title=f'''By along x axis, y = {y}, z = {z}''')
    ax_Fy.plot(xs, Bfieldy, 'g')
    ax_Fy.set_xlabel('x [mm]')
    ax_Fy.set_ylabel('By [mT]')

    ax_Fz = fig.add_subplot(223, title=f'''Bz along x axis, y = {y}, z = {z}''')
    ax_Fz.plot(xs, Bfieldz, 'b')
    ax_Fz.set_xlabel('x [mm]')
    ax_Fz.set_ylabel('Bz [mT]')

    ax_all = fig.add_subplot(224, title=f'''B field along x axis, y = {y}, z = {z}''')
    ax_all.plot(xs, Bfieldx, 'r', label='Bx')
    ax_all.plot(xs, Bfieldy, 'g', label='By')
    ax_all.plot(xs, Bfieldz, 'b', label='Bz')
    ax_all.set_xlabel('x [mm]')
    ax_all.set_ylabel('B [mT]')

    ax_all.legend()
    tight_layout()


def plot_1D_Bxyz_y(x, ys, z, my_collection):
    """Evaluates the value of x and z as planes and plots the values of Bx, By and Bz along the y axis"""

    POS = array([(eval(str(x)), y, eval(str(z))) for y in ys])

    Bfield = array([my_collection.getB(pos) for pos in POS])
    Bfieldx = Bfield[:, 0]
    Bfieldy = Bfield[:, 1]
    Bfieldz = Bfield[:, 2]

    fig = figure(num=f'''B for x = {x}, z = {z}''')
    ax_Fx = fig.add_subplot(221, title=f'''Bx along y axis, x = {x}, z = {z}''')
    ax_Fx.plot(ys, Bfieldx, 'r')
    ax_Fx.set_xlabel('y [mm]')
    ax_Fx.set_ylabel('Bx [mT]')

    ax_Fy = fig.add_subplot(222, title=f'''By along y axis, x = {x}, z = {z}''')
    ax_Fy.plot(ys, Bfieldy, 'g')
    ax_Fy.set_xlabel('y [mm]')
    ax_Fy.set_ylabel('By [mT]')

    ax_Fz = fig.add_subplot(223, title=f'''Bz along y axis, x = {x}, z = {z}''')
    ax_Fz.plot(ys, Bfieldz, 'b')
    ax_Fz.set_xlabel('y [mm]')
    ax_Fz.set_ylabel('Bz [mT]')

    ax_all = fig.add_subplot(224, title=f'''B field along y axis, x = {x}, z = {z}''')
    ax_all.plot(ys, Bfieldx, 'r', label='Bx')
    ax_all.plot(ys, Bfieldy, 'g', label='By')
    ax_all.plot(ys, Bfieldz, 'b', label='Bz')
    ax_all.set_xlabel('y [mm]')
    ax_all.set_ylabel('B [mT]')

    ax_all.legend()
    tight_layout()


def plot_1D_Bxyz_z(x, y, zs, my_collection):
    """Evaluates the value of x and y as planes and plots the values of Bx, By and Bz along the z axis"""

    POS = array([(eval(str(x)), eval(str(y)), z) for z in zs])

    Bfield = array([my_collection.getB(pos) for pos in POS])
    Bfieldx = Bfield[:, 0]
    Bfieldy = Bfield[:, 1]
    Bfieldz = Bfield[:, 2]

    fig = figure(num=f'''B for x = {x}, y = {y}''')
    ax_Fx = fig.add_subplot(221, title=f'''Bx along z axis, x = {x}, y = {y}''')
    ax_Fx.plot(zs, Bfieldx, 'r')
    ax_Fx.set_xlabel('z [mm]')
    ax_Fx.set_ylabel('Bx [mT]')

    ax_Fy = fig.add_subplot(222, title=f'''By along z axis, x = {x}, y = {y}''')
    ax_Fy.plot(zs, Bfieldy, 'g')
    ax_Fy.set_xlabel('z [mm]')
    ax_Fy.set_ylabel('By [mT]')

    ax_Fz = fig.add_subplot(223, title=f'''Bz along z axis, x = {x}, y = {y}''')
    ax_Fz.plot(zs, Bfieldz, 'b')
    ax_Fz.set_xlabel('z [mm]')
    ax_Fz.set_ylabel('Bz [mT]')

    ax_all = fig.add_subplot(224, title=f'''B field along z axis, x = {x}, y = {y}''')
    ax_all.plot(zs, Bfieldx, 'r', label='Bx')
    ax_all.plot(zs, Bfieldy, 'g', label='By')
    ax_all.plot(zs, Bfieldz, 'b', label='Bz')
    ax_all.set_xlabel('z [mm]')
    ax_all.set_ylabel('B [mT]')

    ax_all.legend()
    tight_layout()


# functions for plotting B 2D

def plot_2D_Byz_x(x, ys, zs, my_collection, modes=['stream']):
    """Evaluates the value of x and plots the Bfield in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenys = len(ys)
    lenzs = len(zs)

    POS_raw = array([(eval(str(x)), y, z) for z in zs for y in ys])

    Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

    POS = POS_raw.reshape(lenys, lenzs, 3)
    POSy = POS[:, :, 1]
    POSz = POS[:, :, 2]

    Bfield = Bfield_raw.reshape(lenys, lenzs, 3)
    Bfieldx = Bfield[:, :, 0]
    Bfieldy = Bfield[:, :, 1]
    Bfieldz = Bfield[:, :, 2]

    if 'stream' in modes:
        fig_s = figure(num=f'''B x = {x} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''B direction, x = {x}''')
        ax_s.streamplot(POSy, POSz, Bfieldy, Bfieldz, density=3)
        ax_s.set_xlabel('y [mm]')
        ax_s.set_ylabel('z [mm]')

    if 'quiver' in modes:
        fig_q = figure(num=f'''B x = {x} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''B direction, x = {x}''')
        ByBz_norm = array(list(map(normalize, Bfield_raw[:, [1, 2]])))
        By, Bz = ByBz_norm[:, 0], ByBz_norm[:, 1]
        POSy_raw, POSz_raw = POS_raw[:, 1], POS_raw[:, 2]
        ax_q.quiver(POSy_raw, POSz_raw, By, Bz, units='xy')
        ax_q.set_xlabel('y [mm]')
        ax_q.set_ylabel('z [mm]')

    if 'surface' in modes:
        fig_surface = figure(num=f'''B, x = {x} surface''')
        ax_s_x = fig_surface.add_subplot(131, title=f'''Bx, x = {x}''', projection='3d')
        ax_s_y = fig_surface.add_subplot(132, title=f'''By, x = {x}''', projection='3d')
        ax_s_z = fig_surface.add_subplot(133, title=f'''Bz, x = {x}''', projection='3d')
        ax_s_x.plot_surface(POSy, POSz, Bfieldx)
        ax_s_x.set_xlabel('y [mm]')
        ax_s_x.set_ylabel('z [mm]')
        ax_s_x.set_zlabel('Bx [mT]')
        ax_s_y.plot_surface(POSy, POSz, Bfieldy)
        ax_s_y.set_xlabel('y [mm]')
        ax_s_y.set_ylabel('z [mm]')
        ax_s_y.set_zlabel('By [mT]')
        ax_s_z.plot_surface(POSy, POSz, Bfieldz)
        ax_s_z.set_xlabel('y [mm]')
        ax_s_z.set_ylabel('z [mm]')
        ax_s_z.set_zlabel('Bz [mT]')


def plot_2D_Bxz_y(xs, y, zs, my_collection, modes=['stream']):
    """Evaluates the value of y and plots the Bfield in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenxs = len(xs)
    lenzs = len(zs)

    POS_raw = array([(x, eval(str(y)), z) for z in zs for x in xs])

    Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

    POS = POS_raw.reshape(lenxs, lenzs, 3)
    POSx = POS[:, :, 0]
    POSz = POS[:, :, 2]

    Bfield = Bfield_raw.reshape(lenxs, lenzs, 3)
    Bfieldx = Bfield[:, :, 0]
    Bfieldy = Bfield[:, :, 1]
    Bfieldz = Bfield[:, :, 2]

    if 'stream' in modes:
        fig_s = figure(num=f'''B y = {y} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''B direction, y = {y}''')
        ax_s.streamplot(POSx, POSz, Bfieldx, Bfieldz, density=3)
        ax_s.set_xlabel('x [mm]')
        ax_s.set_ylabel('z [mm]')

    if 'quiver' in modes:
        fig_q = figure(num=f'''B y = {y} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''B direction, y = {y}''')
        BxBz_norm = array(list(map(normalize, Bfield_raw[:, [0, 2]])))
        Bx, Bz = BxBz_norm[:, 0], BxBz_norm[:, 1]
        POSx_raw, POSz_raw = POS_raw[:, 0], POS_raw[:, 2]
        ax_q.quiver(POSx_raw, POSz_raw, Bx, Bz, units='xy')
        ax_q.set_xlabel('x [mm]')
        ax_q.set_ylabel('z [mm]')

    if 'surface' in modes:
        fig_surface = figure(num=f'''B, y = {y} surface''')
        ax_s_x = fig_surface.add_subplot(131, title=f'''Bx, y = {y}''', projection='3d')
        ax_s_y = fig_surface.add_subplot(132, title=f'''By, y = {y}''', projection='3d')
        ax_s_z = fig_surface.add_subplot(133, title=f'''Bz, y = {y}''', projection='3d')
        ax_s_x.plot_surface(POSx, POSz, Bfieldx)
        ax_s_x.set_xlabel('x [mm]')
        ax_s_x.set_ylabel('z [mm]')
        ax_s_x.set_zlabel('Bx [mT]')
        ax_s_y.plot_surface(POSx, POSz, Bfieldy)
        ax_s_y.set_xlabel('x [mm]')
        ax_s_y.set_ylabel('z [mm]')
        ax_s_y.set_zlabel('By [mT]')
        ax_s_z.plot_surface(POSx, POSz, Bfieldz)
        ax_s_z.set_xlabel('x [mm]')
        ax_s_z.set_ylabel('z [mm]')
        ax_s_z.set_zlabel('Bz [mT]')


def plot_2D_Bxy_z(xs, ys, z, my_collection, modes=['stream']):
    """Evaluates the value of z and plots the Bfield in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenxs = len(xs)
    lenys = len(ys)

    POS_raw = array([(x, y, eval(str(z))) for y in ys for x in xs])

    Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

    POS = POS_raw.reshape(lenxs, lenys, 3)
    POSx = POS[:, :, 0]
    POSy = POS[:, :, 1]

    Bfield = Bfield_raw.reshape(lenxs, lenys, 3)
    Bfieldx = Bfield[:, :, 0]
    Bfieldy = Bfield[:, :, 1]
    Bfieldz = Bfield[:, :, 2]

    if 'stream' in modes:
        fig_stream = figure(num=f'''B z = {z} stream''')
        ax_s = fig_stream.add_subplot(aspect=1, title=f'''B direction, z = {z}''')
        ax_s.streamplot(POSx, POSy, Bfieldx, Bfieldy, density=3)
        ax_s.set_xlabel('x [mm]')
        ax_s.set_ylabel('y [mm]')

    if 'quiver' in modes:
        fig_q = figure(num=f'''B z = {z} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''B direction, z = {z}''')
        BxBy_norm = array(list(map(normalize, Bfield_raw[:, [0, 1]])))
        Bx, By = BxBy_norm[:, 0], BxBy_norm[:, 1]
        POSx_raw, POSy_raw = POS_raw[:, 0], POS_raw[:, 1]
        ax_q.quiver(POSx_raw, POSy_raw, Bx, By, units='xy')
        ax_q.set_xlabel('x [mm]')
        ax_q.set_ylabel('y [mm]')

    if 'surface' in modes:
        fig_surface = figure(num=f'''B, z = {z} surface''')
        ax_s_x = fig_surface.add_subplot(131, title=f'''Bx, z = {z}''', projection='3d')
        ax_s_y = fig_surface.add_subplot(132, title=f'''By, z = {z}''', projection='3d')
        ax_s_z = fig_surface.add_subplot(133, title=f'''Bz, z = {z}''', projection='3d')
        ax_s_x.plot_surface(POSx, POSy, Bfieldx)
        ax_s_x.set_xlabel('x [mm]')
        ax_s_x.set_ylabel('y [mm]')
        ax_s_x.set_zlabel('Bx [mT]')
        ax_s_y.plot_surface(POSx, POSy, Bfieldy)
        ax_s_y.set_xlabel('x [mm]')
        ax_s_y.set_ylabel('y [mm]')
        ax_s_y.set_zlabel('By [mT]')
        ax_s_z.plot_surface(POSx, POSy, Bfieldz)
        ax_s_z.set_xlabel('x [mm]')
        ax_s_z.set_ylabel('y [mm]')
        ax_s_z.set_zlabel('Bz [mT]')


# functions for plotting B 3D

def plot_3D_Bxyz(xs, ys, zs, my_collection):
    lenx = len(xs)
    leny = len(ys)
    lenz = len(zs)

    POS = array([(x, y, z) for x in xs for y in ys for z in zs])

    # calculation of force field
    Bfield = array([my_collection.getB(pos) for pos in POS])

    POS = POS.reshape(lenx, leny, lenz, 3)
    POSx = POS[:, :, :, 0]
    POSy = POS[:, :, :, 1]
    POSz = POS[:, :, :, 2]

    Bfield = Bfield.reshape(lenx, leny, lenz, 3)
    Bfieldx = Bfield[:, :, :, 0]
    Bfieldy = Bfield[:, :, :, 1]
    Bfieldz = Bfield[:, :, :, 2]

    # plotting
    fig3d_B = figure(num='B 3D')
    ax = fig3d_B.add_subplot(projection='3d')
    ax.quiver(POSx, POSy, POSz, Bfieldx, Bfieldy, Bfieldz, normalize=True)


# functions for plotting F 1D

def plot_1D_Fxyz_x(xs, y, z, my_collection, sample):
    """Evaluates the value of y and z as planes and plots the values of Fx, Fy and Fz along the x axis"""

    POS = array([(x, eval(str(y)), eval(str(z))) for x in xs])

    FOR = array([getF(pos, my_collection, sample) for pos in POS])
    FORx = FOR[:, 0]
    FORy = FOR[:, 1]
    FORz = FOR[:, 2]

    fig = figure(num=f'''F for y = {y}, z = {z}''')
    ax_Fx = fig.add_subplot(221, title=f'''Fx along x axis, y = {y}, z = {z}''')
    ax_Fx.plot(xs, FORx, 'r')
    ax_Fx.set_xlabel('x [mm]')
    ax_Fx.set_ylabel('Fx [N]')

    ax_Fy = fig.add_subplot(222, title=f'''Fy along x axis, y = {y}, z = {z}''')
    ax_Fy.plot(xs, FORy, 'g')
    ax_Fy.set_xlabel('x [mm]')
    ax_Fy.set_ylabel('Fy [N]')

    ax_Fz = fig.add_subplot(223, title=f'''Fz along x axis, y = {y}, z = {z}''')
    ax_Fz.plot(xs, FORz, 'b')
    ax_Fz.set_xlabel('x [mm]')
    ax_Fz.set_ylabel('Fz [N]')

    ax_all = fig.add_subplot(224, title=f'''Force along x axis, y = {y}, z = {z}''')
    ax_all.plot(xs, FORx, 'r', label='Fx')
    ax_all.plot(xs, FORy, 'g', label='Fy')
    ax_all.plot(xs, FORz, 'b', label='Fz')
    ax_all.set_xlabel('x [mm]')
    ax_all.set_ylabel('Force [N]')

    ax_all.legend()
    tight_layout()


def plot_1D_Fxyz_y(x, ys, z, my_collection, sample):
    """Evaluates the value of x and z as planes and plots the values of Fx, Fy and Fz along the y axis"""

    POS = array([(eval(str(x)), y, eval(str(z))) for y in ys])

    FOR = array([getF(pos, my_collection, sample) for pos in POS])
    FORx = FOR[:, 0]
    FORy = FOR[:, 1]
    FORz = FOR[:, 2]

    fig = figure(num=f'''F for x = {x}, z = {z}''')
    ax_Fx = fig.add_subplot(221, title=f'''Fx along y axis, x = {x}, z = {z}''')
    ax_Fx.plot(ys, FORx, 'r')
    ax_Fx.set_xlabel('y [mm]')
    ax_Fx.set_ylabel('Fx [N]')

    ax_Fy = fig.add_subplot(222, title=f'''Fy along y axis, x = {x}, z = {z}''')
    ax_Fy.plot(ys, FORy, 'g')
    ax_Fy.set_xlabel('y [mm]')
    ax_Fy.set_ylabel('Fy [N]')

    ax_Fz = fig.add_subplot(223, title=f'''Fz along y axis, x = {x}, z = {z}''')
    ax_Fz.plot(ys, FORz, 'b')
    ax_Fz.set_xlabel('y [mm]')
    ax_Fz.set_ylabel('Fz [N]')

    ax_all = fig.add_subplot(224, title=f'''Force along y axis, x = {x}, z = {z}''')
    ax_all.plot(ys, FORx, 'r', label='Fx')
    ax_all.plot(ys, FORy, 'g', label='Fy')
    ax_all.plot(ys, FORz, 'b', label='Fz')
    ax_all.set_xlabel('y [mm]')
    ax_all.set_ylabel('Force [N]')

    ax_all.legend()
    tight_layout()


def plot_1D_Fxyz_z(x, y, zs, my_collection, sample):
    """Evaluates the value of x and y as planes and plots the values of Fx, Fy and Fz along the z axis"""

    POS = array([(eval(str(x)), eval(str(y)), z) for z in zs])

    FOR = array([getF(pos, my_collection, sample) for pos in POS])
    FORx = FOR[:, 0]
    FORy = FOR[:, 1]
    FORz = FOR[:, 2]

    fig = figure(num=f'''F for x = {x}, y = {y}''')
    ax_Fx = fig.add_subplot(221, title=f'''Fx along z axis, x = {x}, y = {y}''')
    ax_Fx.plot(zs, FORx, 'r')
    ax_Fx.set_xlabel('z [mm]')
    ax_Fx.set_ylabel('Fx [N]')

    ax_Fy = fig.add_subplot(222, title=f'''Fy along z axis, x = {x}, y = {y}''')
    ax_Fy.plot(zs, FORy, 'g')
    ax_Fy.set_xlabel('z [mm]')
    ax_Fy.set_ylabel('Fy [N]')

    ax_Fz = fig.add_subplot(223, title=f'''Fz along z axis, x = {x}, y = {y}''')
    ax_Fz.plot(zs, FORz, 'b')
    ax_Fz.set_xlabel('z [mm]')
    ax_Fz.set_ylabel('Fz [N]')

    ax_all = fig.add_subplot(224, title=f'''Force along z axis, x = {x}, y = {y}''')
    ax_all.plot(zs, FORx, 'r', label='Fx')
    ax_all.plot(zs, FORy, 'g', label='Fy')
    ax_all.plot(zs, FORz, 'b', label='Fz')
    ax_all.set_xlabel('z [mm]')
    ax_all.set_ylabel('Force [N]')

    ax_all.legend()
    tight_layout()


# functions for plotting F 2D

def plot_2D_Fyz_x(x, ys, zs, my_collection, sample, modes=['stream']):
    """Evaluates the value of x and plots the force in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenys = len(ys)
    lenzs = len(zs)

    POS_raw = array([(eval(str(x)), y, z) for z in zs for y in ys])

    FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

    POS = POS_raw.reshape(lenys, lenzs, 3)
    POSy = POS[:, :, 1]
    POSz = POS[:, :, 2]

    FOR = FOR_raw.reshape(lenys, lenzs, 3)
    FORx = FOR[:, :, 0]
    FORy = FOR[:, :, 1]
    FORz = FOR[:, :, 2]

    if 'stream' in modes:
        fig_s = figure(num=f'''F x = {x} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''F direction, x = {x}''')
        ax_s.streamplot(POSy, POSz, FORy, FORz, density=3)
        ax_s.set_xlabel('y [mm]')
        ax_s.set_ylabel('z [mm]')

    if 'quiver' in modes:
        fig_q = figure(num=f'''F x = {x} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''F direction, x = {x}''')
        FyFz_norm = array(list(map(normalize, FOR_raw[:, [1, 2]])))
        Fy, Fz = FyFz_norm[:, 0], FyFz_norm[:, 1]
        POSy_raw, POSz_raw = POS_raw[:, 1], POS_raw[:, 2]
        ax_q.quiver(POSy_raw, POSz_raw, Fy, Fz, units='xy')
        ax_q.set_xlabel('y [mm]')
        ax_q.set_ylabel('z [mm]')

    if 'surface' in modes:
        fig_surface = figure(num=f'''F, x = {x} surface''')
        ax_s_x = fig_surface.add_subplot(131, title=f'''Fx, x = {x}''', projection='3d')
        ax_s_y = fig_surface.add_subplot(132, title=f'''Fy, x = {x}''', projection='3d')
        ax_s_z = fig_surface.add_subplot(133, title=f'''Fz, x = {x}''', projection='3d')
        ax_s_x.plot_surface(POSy, POSz, FORx)
        ax_s_x.set_xlabel('y [mm]')
        ax_s_x.set_ylabel('z [mm]')
        ax_s_x.set_zlabel('Fx [N]')
        ax_s_y.plot_surface(POSy, POSz, FORy)
        ax_s_y.set_xlabel('y [mm]')
        ax_s_y.set_ylabel('z [mm]')
        ax_s_y.set_zlabel('Fy [N]')
        ax_s_z.plot_surface(POSy, POSz, FORz)
        ax_s_z.set_xlabel('y [mm]')
        ax_s_z.set_ylabel('z [mm]')
        ax_s_z.set_zlabel('Fz [N]')


def plot_2D_Fxz_y(xs, y, zs, my_collection, sample, modes=['stream']):
    """Evaluates the value of y and plots the force in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenxs = len(xs)
    lenzs = len(zs)

    POS_raw = array([(x, eval(str(y)), z) for z in zs for x in xs])

    FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

    POS = POS_raw.reshape(lenxs, lenzs, 3)
    POSx = POS[:, :, 0]
    POSz = POS[:, :, 2]

    FOR = FOR_raw.reshape(lenxs, lenzs, 3)
    FORx = FOR[:, :, 0]
    FORy = FOR[:, :, 1]
    FORz = FOR[:, :, 2]

    if 'stream' in modes:
        fig_s = figure(num=f'''F y = {y} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''F direction, y = {y}''')
        ax_s.streamplot(POSx, POSz, FORx, FORz, density=3)
        ax_s.set_xlabel('x [mm]')
        ax_s.set_ylabel('z [mm]')

    if 'quiver' in modes:
        fig_q = figure(num=f'''F y = {y} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''F direction, y = {y}''')
        FxFz_norm = array(list(map(normalize, FOR_raw[:, [0, 2]])))
        Fx, Fz = FxFz_norm[:, 0], FxFz_norm[:, 1]
        POSx_raw, POSz_raw = POS_raw[:, 0], POS_raw[:, 2]
        ax_q.quiver(POSx_raw, POSz_raw, Fx, Fz, units='xy')
        ax_q.set_xlabel('x [mm]')
        ax_q.set_ylabel('z [mm]')

    if 'surface' in modes:
        fig_surface = figure(num=f'''F, y = {y} surface''')
        ax_s_x = fig_surface.add_subplot(131, title=f'''Fx, y = {y}''', projection='3d')
        ax_s_y = fig_surface.add_subplot(132, title=f'''Fy, y = {y}''', projection='3d')
        ax_s_z = fig_surface.add_subplot(133, title=f'''Fz, y = {y}''', projection='3d')
        ax_s_x.plot_surface(POSx, POSz, FORx)
        ax_s_x.set_xlabel('x [mm]')
        ax_s_x.set_ylabel('z [mm]')
        ax_s_x.set_zlabel('Fx [N]')
        ax_s_y.plot_surface(POSx, POSz, FORy)
        ax_s_y.set_xlabel('x [mm]')
        ax_s_y.set_ylabel('z [mm]')
        ax_s_y.set_zlabel('Fy [N]')
        ax_s_z.plot_surface(POSx, POSz, FORz)
        ax_s_z.set_xlabel('x [mm]')
        ax_s_z.set_ylabel('z [mm]')
        ax_s_z.set_zlabel('Fz [N]')


def plot_2D_Fxy_z(xs, ys, z, my_collection, sample, modes=['stream']):
    """Evaluates the value of z and plots the force in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenxs = len(xs)
    lenys = len(ys)

    POS_raw = array([(x, y, eval(str(z))) for y in ys for x in xs])

    FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

    POS = POS_raw.reshape(lenxs, lenys, 3)
    POSx = POS[:, :, 0]
    POSy = POS[:, :, 1]

    FOR = FOR_raw.reshape(lenxs, lenys, 3)
    FORx = FOR[:, :, 0]
    FORy = FOR[:, :, 1]
    FORz = FOR[:, :, 2]

    if 'stream' in modes:
        fig_s = figure(num=f'''F z = {z} stream''')
        ax_s = fig_s.add_subplot(aspect=1, title=f'''F direction, z = {z}''')
        ax_s.streamplot(POSx, POSy, FORx, FORy, density=3)
        ax_s.set_xlabel('x [mm]')
        ax_s.set_ylabel('y [mm]')

    if 'quiver' in modes:
        fig_q = figure(num=f'''F z = {z} quiver''')
        ax_q = fig_q.add_subplot(aspect=1, title=f'''F direction, z = {z}''')
        FxFy_norm = array(list(map(normalize, FOR_raw[:, [0, 1]])))
        Fx, Fy = FxFy_norm[:, 0], FxFy_norm[:, 1]
        POSx_raw, POSy_raw = POS_raw[:, 0], POS_raw[:, 1]
        ax_q.quiver(POSx_raw, POSy_raw, Fx, Fy, units='xy')
        ax_q.set_xlabel('x [mm]')
        ax_q.set_ylabel('y [mm]')

    if 'surface' in modes:
        fig_surface = figure(num=f'''F, z = {z} surface''')
        ax_s_x = fig_surface.add_subplot(131, title=f'''Fx, z = {z}''', projection='3d')
        ax_s_y = fig_surface.add_subplot(132, title=f'''Fy, z = {z}''', projection='3d')
        ax_s_z = fig_surface.add_subplot(133, title=f'''Fz, z = {z}''', projection='3d')
        ax_s_x.plot_surface(POSx, POSy, FORx)
        ax_s_x.set_xlabel('x [mm]')
        ax_s_x.set_ylabel('y [mm]')
        ax_s_x.set_zlabel('Fx [N]')
        ax_s_y.plot_surface(POSx, POSy, FORy)
        ax_s_y.set_xlabel('x [mm]')
        ax_s_y.set_ylabel('y [mm]')
        ax_s_y.set_zlabel('Fy [N]')
        ax_s_z.plot_surface(POSx, POSy, FORz)
        ax_s_z.set_xlabel('x [mm]')
        ax_s_z.set_ylabel('y [mm]')
        ax_s_z.set_zlabel('Fz [N]')


# functions for plotting B 3D

def plot_3D_Fxyz(xs, ys, zs, my_collection, sample):
    lenx = len(xs)
    leny = len(ys)
    lenz = len(zs)

    POS = array([(x, y, z) for x in xs for y in ys for z in zs])

    # calculation of force field
    FOR = array([getF(pos, my_collection, sample) for pos in POS])

    POS = POS.reshape(lenx, leny, lenz, 3)
    POSx = POS[:, :, :, 0]
    POSy = POS[:, :, :, 1]
    POSz = POS[:, :, :, 2]

    FOR = FOR.reshape(lenx, leny, lenz, 3)
    FORx = FOR[:, :, :, 0]
    FORy = FOR[:, :, :, 1]
    FORz = FOR[:, :, :, 2]

    # plotting
    fig3d_F = figure(num='F 3D')
    ax = fig3d_F.add_subplot(projection='3d')
    ax.quiver(POSx, POSy, POSz, FORx, FORy, FORz, normalize=True)

