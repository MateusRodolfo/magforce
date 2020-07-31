# made with magpylib v2.3.0b
from numpy import array
from matplotlib.pyplot import figure, tight_layout

from project_helpers.calculation_functions import normalize, getF


# functions for plotting 1D

def plot_1D_along_x(xs, y, z, my_collection, sample=None, BF='BF'):
    """Evaluates the value of y and z as planes and plots the values of Bx, By and Bz along the x axis"""

    POS = array([(x, eval(str(y)), eval(str(z))) for x in xs])

    bf = BF.lower()

    if 'b' in bf:
        Bfield = array([my_collection.getB(pos) for pos in POS])
        Bfieldx = Bfield[:, 0]
        Bfieldy = Bfield[:, 1]
        Bfieldz = Bfield[:, 2]

        fig_B = figure(num=f'''B for y = {y}, z = {z}''')
        ax_Bx = fig_B.add_subplot(221, title=f'''Bx along x axis, y = {y}, z = {z}''')
        ax_Bx.plot(xs, Bfieldx, 'r')
        ax_Bx.set_xlabel('x [mm]')
        ax_Bx.set_ylabel('Bx [mT]')

        ax_By = fig_B.add_subplot(222, title=f'''By along x axis, y = {y}, z = {z}''')
        ax_By.plot(xs, Bfieldy, 'g')
        ax_By.set_xlabel('x [mm]')
        ax_By.set_ylabel('By [mT]')

        ax_Bz = fig_B.add_subplot(223, title=f'''Bz along x axis, y = {y}, z = {z}''')
        ax_Bz.plot(xs, Bfieldz, 'b')
        ax_Bz.set_xlabel('x [mm]')
        ax_Bz.set_ylabel('Bz [mT]')

        ax_B_all = fig_B.add_subplot(224, title=f'''B field along x axis, y = {y}, z = {z}''')
        ax_B_all.plot(xs, Bfieldx, 'r', label='Bx')
        ax_B_all.plot(xs, Bfieldy, 'g', label='By')
        ax_B_all.plot(xs, Bfieldz, 'b', label='Bz')
        ax_B_all.set_xlabel('x [mm]')
        ax_B_all.set_ylabel('B [mT]')

        ax_B_all.legend()
        tight_layout()

    if 'f' in bf:
        FOR = array([getF(pos, my_collection, sample) for pos in POS])
        FORx = FOR[:, 0]
        FORy = FOR[:, 1]
        FORz = FOR[:, 2]

        fig_F = figure(num=f'''F for y = {y}, z = {z}''')
        ax_Fx = fig_F.add_subplot(221, title=f'''Fx along x axis, y = {y}, z = {z}''')
        ax_Fx.plot(xs, FORx, 'r')
        ax_Fx.set_xlabel('x [mm]')
        ax_Fx.set_ylabel('Fx [N]')

        ax_Fy = fig_F.add_subplot(222, title=f'''Fy along x axis, y = {y}, z = {z}''')
        ax_Fy.plot(xs, FORy, 'g')
        ax_Fy.set_xlabel('x [mm]')
        ax_Fy.set_ylabel('Fy [N]')

        ax_Fz = fig_F.add_subplot(223, title=f'''Fz along x axis, y = {y}, z = {z}''')
        ax_Fz.plot(xs, FORz, 'b')
        ax_Fz.set_xlabel('x [mm]')
        ax_Fz.set_ylabel('Fz [N]')

        ax_F_all = fig_F.add_subplot(224, title=f'''Force along x axis, y = {y}, z = {z}''')
        ax_F_all.plot(xs, FORx, 'r', label='Fx')
        ax_F_all.plot(xs, FORy, 'g', label='Fy')
        ax_F_all.plot(xs, FORz, 'b', label='Fz')
        ax_F_all.set_xlabel('x [mm]')
        ax_F_all.set_ylabel('Force [N]')

        ax_F_all.legend()
        tight_layout()


def plot_1D_along_y(x, ys, z, my_collection, sample=None, BF='BF'):
    """Evaluates the value of x and z as planes and plots the values of Bx, By and Bz along the y axis"""

    POS = array([(eval(str(x)), y, eval(str(z))) for y in ys])

    bf = BF.lower()

    if 'b' in bf:
        Bfield = array([my_collection.getB(pos) for pos in POS])
        Bfieldx = Bfield[:, 0]
        Bfieldy = Bfield[:, 1]
        Bfieldz = Bfield[:, 2]

        fig_B = figure(num=f'''B for x = {x}, z = {z}''')
        ax_Bx = fig_B.add_subplot(221, title=f'''Bx along y axis, x = {x}, z = {z}''')
        ax_Bx.plot(ys, Bfieldx, 'r')
        ax_Bx.set_xlabel('y [mm]')
        ax_Bx.set_ylabel('Bx [mT]')

        ax_By = fig_B.add_subplot(222, title=f'''By along y axis, x = {x}, z = {z}''')
        ax_By.plot(ys, Bfieldy, 'g')
        ax_By.set_xlabel('y [mm]')
        ax_By.set_ylabel('By [mT]')

        ax_Bz = fig_B.add_subplot(223, title=f'''Bz along y axis, x = {x}, z = {z}''')
        ax_Bz.plot(ys, Bfieldz, 'b')
        ax_Bz.set_xlabel('y [mm]')
        ax_Bz.set_ylabel('Bz [mT]')

        ax_B_all = fig_B.add_subplot(224, title=f'''B field along y axis, x = {x}, z = {z}''')
        ax_B_all.plot(ys, Bfieldx, 'r', label='Bx')
        ax_B_all.plot(ys, Bfieldy, 'g', label='By')
        ax_B_all.plot(ys, Bfieldz, 'b', label='Bz')
        ax_B_all.set_xlabel('y [mm]')
        ax_B_all.set_ylabel('B [mT]')

        ax_B_all.legend()
        tight_layout()

    if 'f' in bf:
        FOR = array([getF(pos, my_collection, sample) for pos in POS])
        FORx = FOR[:, 0]
        FORy = FOR[:, 1]
        FORz = FOR[:, 2]

        fig_F = figure(num=f'''F for x = {x}, z = {z}''')
        ax_Fx = fig_F.add_subplot(221, title=f'''Fx along y axis, x = {x}, z = {z}''')
        ax_Fx.plot(ys, FORx, 'r')
        ax_Fx.set_xlabel('y [mm]')
        ax_Fx.set_ylabel('Fx [N]')

        ax_Fy = fig_F.add_subplot(222, title=f'''Fy along y axis, x = {x}, z = {z}''')
        ax_Fy.plot(ys, FORy, 'g')
        ax_Fy.set_xlabel('y [mm]')
        ax_Fy.set_ylabel('Fy [N]')

        ax_Fz = fig_F.add_subplot(223, title=f'''Fz along y axis, x = {x}, z = {z}''')
        ax_Fz.plot(ys, FORz, 'b')
        ax_Fz.set_xlabel('y [mm]')
        ax_Fz.set_ylabel('Fz [N]')

        ax_F_all = fig_F.add_subplot(224, title=f'''Force along y axis, x = {x}, z = {z}''')
        ax_F_all.plot(ys, FORx, 'r', label='Fx')
        ax_F_all.plot(ys, FORy, 'g', label='Fy')
        ax_F_all.plot(ys, FORz, 'b', label='Fz')
        ax_F_all.set_xlabel('y [mm]')
        ax_F_all.set_ylabel('Force [N]')

        ax_F_all.legend()
        tight_layout()


def plot_1D_along_z(x, y, zs, my_collection, sample=None, BF='BF'):
    """Evaluates the value of x and y as planes and plots the values of Bx, By and Bz along the z axis"""

    POS = array([(eval(str(x)), eval(str(y)), z) for z in zs])

    bf = BF.lower()

    if 'b' in bf:
        Bfield = array([my_collection.getB(pos) for pos in POS])
        Bfieldx = Bfield[:, 0]
        Bfieldy = Bfield[:, 1]
        Bfieldz = Bfield[:, 2]

        fig_B = figure(num=f'''B for x = {x}, y = {y}''')
        ax_Bx = fig_B.add_subplot(221, title=f'''Bx along z axis, x = {x}, y = {y}''')
        ax_Bx.plot(zs, Bfieldx, 'r')
        ax_Bx.set_xlabel('z [mm]')
        ax_Bx.set_ylabel('Bx [mT]')

        ax_By = fig_B.add_subplot(222, title=f'''By along z axis, x = {x}, y = {y}''')
        ax_By.plot(zs, Bfieldy, 'g')
        ax_By.set_xlabel('z [mm]')
        ax_By.set_ylabel('By [mT]')

        ax_Bz = fig_B.add_subplot(223, title=f'''Bz along z axis, x = {x}, y = {y}''')
        ax_Bz.plot(zs, Bfieldz, 'b')
        ax_Bz.set_xlabel('z [mm]')
        ax_Bz.set_ylabel('Bz [mT]')

        ax_B_all = fig_B.add_subplot(224, title=f'''B field along z axis, x = {x}, y = {y}''')
        ax_B_all.plot(zs, Bfieldx, 'r', label='Bx')
        ax_B_all.plot(zs, Bfieldy, 'g', label='By')
        ax_B_all.plot(zs, Bfieldz, 'b', label='Bz')
        ax_B_all.set_xlabel('z [mm]')
        ax_B_all.set_ylabel('B [mT]')

        ax_B_all.legend()
        tight_layout()

    if 'f' in bf:
        FOR = array([getF(pos, my_collection, sample) for pos in POS])
        FORx = FOR[:, 0]
        FORy = FOR[:, 1]
        FORz = FOR[:, 2]

        fig_F = figure(num=f'''F for x = {x}, y = {y}''')
        ax_Fx = fig_F.add_subplot(221, title=f'''Fx along z axis, x = {x}, y = {y}''')
        ax_Fx.plot(zs, FORx, 'r')
        ax_Fx.set_xlabel('z [mm]')
        ax_Fx.set_ylabel('Fx [N]')

        ax_Fy = fig_F.add_subplot(222, title=f'''Fy along z axis, x = {x}, y = {y}''')
        ax_Fy.plot(zs, FORy, 'g')
        ax_Fy.set_xlabel('z [mm]')
        ax_Fy.set_ylabel('Fy [N]')

        ax_Fz = fig_F.add_subplot(223, title=f'''Fz along z axis, x = {x}, y = {y}''')
        ax_Fz.plot(zs, FORz, 'b')
        ax_Fz.set_xlabel('z [mm]')
        ax_Fz.set_ylabel('Fz [N]')

        ax_F_all = fig_F.add_subplot(224, title=f'''Force along z axis, x = {x}, y = {y}''')
        ax_F_all.plot(zs, FORx, 'r', label='Fx')
        ax_F_all.plot(zs, FORy, 'g', label='Fy')
        ax_F_all.plot(zs, FORz, 'b', label='Fz')
        ax_F_all.set_xlabel('z [mm]')
        ax_F_all.set_ylabel('Force [N]')

        ax_F_all.legend()
        tight_layout()


# functions for plotting 2D

def plot_2D_plane_x(x, ys, zs, my_collection, sample=None, modes=['stream'], BF='BF'):
    """Evaluates the value of x and plots the Bfield in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenys = len(ys)
    lenzs = len(zs)

    POS_raw = array([(eval(str(x)), y, z) for z in zs for y in ys])

    POS = POS_raw.reshape(lenys, lenzs, 3)
    POSy = POS[:, :, 1]
    POSz = POS[:, :, 2]

    bf = BF.lower()

    if 'b' in bf:
        Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

        Bfield = Bfield_raw.reshape(lenys, lenzs, 3)
        Bfieldx = Bfield[:, :, 0]
        Bfieldy = Bfield[:, :, 1]
        Bfieldz = Bfield[:, :, 2]

        if 'stream' in modes:
            fig_B_stream = figure(num=f'''B x = {x} stream''')
            ax_B_stream = fig_B_stream.add_subplot(aspect=1, title=f'''B direction, x = {x}''')
            ax_B_stream.streamplot(POSy, POSz, Bfieldy, Bfieldz, density=3)
            ax_B_stream.set_xlabel('y [mm]')
            ax_B_stream.set_ylabel('z [mm]')

        if 'quiver' in modes:
            fig_B_quiver = figure(num=f'''B x = {x} quiver''')
            ax_B_quiver = fig_B_quiver.add_subplot(aspect=1, title=f'''B direction, x = {x}''')
            ByBz_norm = array(list(map(normalize, Bfield_raw[:, [1, 2]])))
            By, Bz = ByBz_norm[:, 0], ByBz_norm[:, 1]
            POSy_raw, POSz_raw = POS_raw[:, 1], POS_raw[:, 2]
            ax_B_quiver.quiver(POSy_raw, POSz_raw, By, Bz, units='xy')
            ax_B_quiver.set_xlabel('y [mm]')
            ax_B_quiver.set_ylabel('z [mm]')

        if 'surface' in modes:
            fig_B_surface = figure(num=f'''B, x = {x} surface''')
            ax_B_surf_x = fig_B_surface.add_subplot(131, title=f'''Bx, x = {x}''', projection='3d')
            ax_B_surf_y = fig_B_surface.add_subplot(132, title=f'''By, x = {x}''', projection='3d')
            ax_B_surf_z = fig_B_surface.add_subplot(133, title=f'''Bz, x = {x}''', projection='3d')
            ax_B_surf_x.plot_surface(POSy, POSz, Bfieldx)
            ax_B_surf_x.set_xlabel('y [mm]')
            ax_B_surf_x.set_ylabel('z [mm]')
            ax_B_surf_x.set_zlabel('Bx [mT]')
            ax_B_surf_y.plot_surface(POSy, POSz, Bfieldy)
            ax_B_surf_y.set_xlabel('y [mm]')
            ax_B_surf_y.set_ylabel('z [mm]')
            ax_B_surf_y.set_zlabel('By [mT]')
            ax_B_surf_z.plot_surface(POSy, POSz, Bfieldz)
            ax_B_surf_z.set_xlabel('y [mm]')
            ax_B_surf_z.set_ylabel('z [mm]')
            ax_B_surf_z.set_zlabel('Bz [mT]')

    if 'f' in bf:
        FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

        FOR = FOR_raw.reshape(lenys, lenzs, 3)
        FORx = FOR[:, :, 0]
        FORy = FOR[:, :, 1]
        FORz = FOR[:, :, 2]

        if 'stream' in modes:
            fig_F_stream = figure(num=f'''F x = {x} stream''')
            ax_F_stream = fig_F_stream.add_subplot(aspect=1, title=f'''F direction, x = {x}''')
            ax_F_stream.streamplot(POSy, POSz, FORy, FORz, density=3)
            ax_F_stream.set_xlabel('y [mm]')
            ax_F_stream.set_ylabel('z [mm]')

        if 'quiver' in modes:
            fig_F_quiver = figure(num=f'''F x = {x} quiver''')
            ax_F_quiver = fig_F_quiver.add_subplot(aspect=1, title=f'''F direction, x = {x}''')
            FyFz_norm = array(list(map(normalize, FOR_raw[:, [1, 2]])))
            Fy, Fz = FyFz_norm[:, 0], FyFz_norm[:, 1]
            POSy_raw, POSz_raw = POS_raw[:, 1], POS_raw[:, 2]
            ax_F_quiver.quiver(POSy_raw, POSz_raw, Fy, Fz, units='xy')
            ax_F_quiver.set_xlabel('y [mm]')
            ax_F_quiver.set_ylabel('z [mm]')

        if 'surface' in modes:
            fig_F_surface = figure(num=f'''F, x = {x} surface''')
            ax_F_surf_x = fig_F_surface.add_subplot(131, title=f'''Fx, x = {x}''', projection='3d')
            ax_F_surf_y = fig_F_surface.add_subplot(132, title=f'''Fy, x = {x}''', projection='3d')
            ax_F_surf_z = fig_F_surface.add_subplot(133, title=f'''Fz, x = {x}''', projection='3d')
            ax_F_surf_x.plot_surface(POSy, POSz, FORx)
            ax_F_surf_x.set_xlabel('y [mm]')
            ax_F_surf_x.set_ylabel('z [mm]')
            ax_F_surf_x.set_zlabel('Fx [N]')
            ax_F_surf_y.plot_surface(POSy, POSz, FORy)
            ax_F_surf_y.set_xlabel('y [mm]')
            ax_F_surf_y.set_ylabel('z [mm]')
            ax_F_surf_y.set_zlabel('Fy [N]')
            ax_F_surf_z.plot_surface(POSy, POSz, FORz)
            ax_F_surf_z.set_xlabel('y [mm]')
            ax_F_surf_z.set_ylabel('z [mm]')
            ax_F_surf_z.set_zlabel('Fz [N]')


def plot_2D_plane_y(xs, y, zs, my_collection, sample=None, modes=['stream'], BF='BF'):
    """Evaluates the value of y and plots the Bfield in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenxs = len(xs)
    lenzs = len(zs)

    POS_raw = array([(x, eval(str(y)), z) for z in zs for x in xs])

    POS = POS_raw.reshape(lenxs, lenzs, 3)
    POSx = POS[:, :, 0]
    POSz = POS[:, :, 2]

    bf = BF.lower()

    if 'b' in bf:
        Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

        Bfield = Bfield_raw.reshape(lenxs, lenzs, 3)
        Bfieldx = Bfield[:, :, 0]
        Bfieldy = Bfield[:, :, 1]
        Bfieldz = Bfield[:, :, 2]

        if 'stream' in modes:
            fig_B_stream = figure(num=f'''B y = {y} stream''')
            ax_B_stream = fig_B_stream.add_subplot(aspect=1, title=f'''B direction, y = {y}''')
            ax_B_stream.streamplot(POSx, POSz, Bfieldx, Bfieldz, density=3)
            ax_B_stream.set_xlabel('x [mm]')
            ax_B_stream.set_ylabel('z [mm]')

        if 'quiver' in modes:
            fig_B_quiver = figure(num=f'''B y = {y} quiver''')
            ax_B_quiver = fig_B_quiver.add_subplot(aspect=1, title=f'''B direction, y = {y}''')
            BxBz_norm = array(list(map(normalize, Bfield_raw[:, [0, 2]])))
            Bx, Bz = BxBz_norm[:, 0], BxBz_norm[:, 1]
            POSx_raw, POSz_raw = POS_raw[:, 0], POS_raw[:, 2]
            ax_B_quiver.quiver(POSx_raw, POSz_raw, Bx, Bz, units='xy')
            ax_B_quiver.set_xlabel('x [mm]')
            ax_B_quiver.set_ylabel('z [mm]')

        if 'surface' in modes:
            fig_B_surface = figure(num=f'''B, y = {y} surface''')
            ax_B_surf_x = fig_B_surface.add_subplot(131, title=f'''Bx, y = {y}''', projection='3d')
            ax_B_surf_y = fig_B_surface.add_subplot(132, title=f'''By, y = {y}''', projection='3d')
            ax_B_surf_z = fig_B_surface.add_subplot(133, title=f'''Bz, y = {y}''', projection='3d')
            ax_B_surf_x.plot_surface(POSx, POSz, Bfieldx)
            ax_B_surf_x.set_xlabel('x [mm]')
            ax_B_surf_x.set_ylabel('z [mm]')
            ax_B_surf_x.set_zlabel('Bx [mT]')
            ax_B_surf_y.plot_surface(POSx, POSz, Bfieldy)
            ax_B_surf_y.set_xlabel('x [mm]')
            ax_B_surf_y.set_ylabel('z [mm]')
            ax_B_surf_y.set_zlabel('By [mT]')
            ax_B_surf_z.plot_surface(POSx, POSz, Bfieldz)
            ax_B_surf_z.set_xlabel('x [mm]')
            ax_B_surf_z.set_ylabel('z [mm]')
            ax_B_surf_z.set_zlabel('Bz [mT]')

    if 'f' in bf:
        FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

        FOR = FOR_raw.reshape(lenxs, lenzs, 3)
        FORx = FOR[:, :, 0]
        FORy = FOR[:, :, 1]
        FORz = FOR[:, :, 2]

        if 'stream' in modes:
            fig_F_stream = figure(num=f'''F y = {y} stream''')
            ax_F_stream = fig_F_stream.add_subplot(aspect=1, title=f'''F direction, y = {y}''')
            ax_F_stream.streamplot(POSx, POSz, FORx, FORz, density=3)
            ax_F_stream.set_xlabel('x [mm]')
            ax_F_stream.set_ylabel('z [mm]')

        if 'quiver' in modes:
            fig_F_quiver = figure(num=f'''F y = {y} quiver''')
            ax_F_quiver = fig_F_quiver.add_subplot(aspect=1, title=f'''F direction, y = {y}''')
            FxFz_norm = array(list(map(normalize, FOR_raw[:, [0, 2]])))
            Fx, Fz = FxFz_norm[:, 0], FxFz_norm[:, 1]
            POSx_raw, POSz_raw = POS_raw[:, 0], POS_raw[:, 2]
            ax_F_quiver.quiver(POSx_raw, POSz_raw, Fx, Fz, units='xy')
            ax_F_quiver.set_xlabel('x [mm]')
            ax_F_quiver.set_ylabel('z [mm]')

        if 'surface' in modes:
            fig_F_surface = figure(num=f'''F, y = {y} surface''')
            ax_F_surf_x = fig_F_surface.add_subplot(131, title=f'''Fx, y = {y}''', projection='3d')
            ax_F_surf_y = fig_F_surface.add_subplot(132, title=f'''Fy, y = {y}''', projection='3d')
            ax_F_surf_z = fig_F_surface.add_subplot(133, title=f'''Fz, y = {y}''', projection='3d')
            ax_F_surf_x.plot_surface(POSx, POSz, FORx)
            ax_F_surf_x.set_xlabel('x [mm]')
            ax_F_surf_x.set_ylabel('z [mm]')
            ax_F_surf_x.set_zlabel('Fx [N]')
            ax_F_surf_y.plot_surface(POSx, POSz, FORy)
            ax_F_surf_y.set_xlabel('x [mm]')
            ax_F_surf_y.set_ylabel('z [mm]')
            ax_F_surf_y.set_zlabel('Fy [N]')
            ax_F_surf_z.plot_surface(POSx, POSz, FORz)
            ax_F_surf_z.set_xlabel('x [mm]')
            ax_F_surf_z.set_ylabel('z [mm]')
            ax_F_surf_z.set_zlabel('Fz [N]')


def plot_2D_plane_z(xs, ys, z, my_collection, sample=None, modes=['stream'], BF='BF'):
    """Evaluates the value of z and plots the Bfield in that plane
    mode is a list with possible contents being ['quiver','stream','surface']"""

    lenxs = len(xs)
    lenys = len(ys)

    POS_raw = array([(x, y, eval(str(z))) for y in ys for x in xs])

    POS = POS_raw.reshape(lenxs, lenys, 3)
    POSx = POS[:, :, 0]
    POSy = POS[:, :, 1]

    bf = BF.lower()

    if 'b' in bf:
        Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

        Bfield = Bfield_raw.reshape(lenxs, lenys, 3)
        Bfieldx = Bfield[:, :, 0]
        Bfieldy = Bfield[:, :, 1]
        Bfieldz = Bfield[:, :, 2]

        if 'stream' in modes:
            fig_B_stream = figure(num=f'''B z = {z} stream''')
            ax_B_stream = fig_B_stream.add_subplot(aspect=1, title=f'''B direction, z = {z}''')
            ax_B_stream.streamplot(POSx, POSy, Bfieldx, Bfieldy, density=3)
            ax_B_stream.set_xlabel('x [mm]')
            ax_B_stream.set_ylabel('y [mm]')

        if 'quiver' in modes:
            fig_B_quiver = figure(num=f'''B z = {z} quiver''')
            ax_B_quiver = fig_B_quiver.add_subplot(aspect=1, title=f'''B direction, z = {z}''')
            BxBy_norm = array(list(map(normalize, Bfield_raw[:, [0, 1]])))
            Bx, By = BxBy_norm[:, 0], BxBy_norm[:, 1]
            POSx_raw, POSy_raw = POS_raw[:, 0], POS_raw[:, 1]
            ax_B_quiver.quiver(POSx_raw, POSy_raw, Bx, By, units='xy')
            ax_B_quiver.set_xlabel('x [mm]')
            ax_B_quiver.set_ylabel('y [mm]')

        if 'surface' in modes:
            fig_B_surface = figure(num=f'''B, z = {z} surface''')
            ax_B_surf_x = fig_B_surface.add_subplot(131, title=f'''Bx, z = {z}''', projection='3d')
            ax_B_surf_y = fig_B_surface.add_subplot(132, title=f'''By, z = {z}''', projection='3d')
            ax_B_surf_z = fig_B_surface.add_subplot(133, title=f'''Bz, z = {z}''', projection='3d')
            ax_B_surf_x.plot_surface(POSx, POSy, Bfieldx)
            ax_B_surf_x.set_xlabel('x [mm]')
            ax_B_surf_x.set_ylabel('y [mm]')
            ax_B_surf_x.set_zlabel('Bx [mT]')
            ax_B_surf_y.plot_surface(POSx, POSy, Bfieldy)
            ax_B_surf_y.set_xlabel('x [mm]')
            ax_B_surf_y.set_ylabel('y [mm]')
            ax_B_surf_y.set_zlabel('By [mT]')
            ax_B_surf_z.plot_surface(POSx, POSy, Bfieldz)
            ax_B_surf_z.set_xlabel('x [mm]')
            ax_B_surf_z.set_ylabel('y [mm]')
            ax_B_surf_z.set_zlabel('Bz [mT]')

    if 'f' in bf:
        FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

        FOR = FOR_raw.reshape(lenxs, lenys, 3)
        FORx = FOR[:, :, 0]
        FORy = FOR[:, :, 1]
        FORz = FOR[:, :, 2]

        if 'stream' in modes:
            fig_F_stream = figure(num=f'''F z = {z} stream''')
            ax_F_stream = fig_F_stream.add_subplot(aspect=1, title=f'''F direction, z = {z}''')
            ax_F_stream.streamplot(POSx, POSy, FORx, FORy, density=3)
            ax_F_stream.set_xlabel('x [mm]')
            ax_F_stream.set_ylabel('y [mm]')

        if 'quiver' in modes:
            fig_F_quiver = figure(num=f'''F z = {z} quiver''')
            ax_F_quiver = fig_F_quiver.add_subplot(aspect=1, title=f'''F direction, z = {z}''')
            FxFy_norm = array(list(map(normalize, FOR_raw[:, [0, 1]])))
            Fx, Fy = FxFy_norm[:, 0], FxFy_norm[:, 1]
            POSx_raw, POSy_raw = POS_raw[:, 0], POS_raw[:, 1]
            ax_F_quiver.quiver(POSx_raw, POSy_raw, Fx, Fy, units='xy')
            ax_F_quiver.set_xlabel('x [mm]')
            ax_F_quiver.set_ylabel('y [mm]')

        if 'surface' in modes:
            fig_F_surface = figure(num=f'''F, z = {z} surface''')
            ax_F_surf_x = fig_F_surface.add_subplot(131, title=f'''Fx, z = {z}''', projection='3d')
            ax_F_surf_y = fig_F_surface.add_subplot(132, title=f'''Fy, z = {z}''', projection='3d')
            ax_F_surf_z = fig_F_surface.add_subplot(133, title=f'''Fz, z = {z}''', projection='3d')
            ax_F_surf_x.plot_surface(POSx, POSy, FORx)
            ax_F_surf_x.set_xlabel('x [mm]')
            ax_F_surf_x.set_ylabel('y [mm]')
            ax_F_surf_x.set_zlabel('Fx [N]')
            ax_F_surf_y.plot_surface(POSx, POSy, FORy)
            ax_F_surf_y.set_xlabel('x [mm]')
            ax_F_surf_y.set_ylabel('y [mm]')
            ax_F_surf_y.set_zlabel('Fy [N]')
            ax_F_surf_z.plot_surface(POSx, POSy, FORz)
            ax_F_surf_z.set_xlabel('x [mm]')
            ax_F_surf_z.set_ylabel('y [mm]')
            ax_F_surf_z.set_zlabel('Fz [N]')


# functions for plotting 3D

def plot_3D(xs, ys, zs, my_collection, sample=None, BF='BF'):
    lenx = len(xs)
    leny = len(ys)
    lenz = len(zs)

    bf = BF.lower()

    POS_raw = array([(x, y, z) for x in xs for y in ys for z in zs])

    POS = POS_raw.reshape(lenx, leny, lenz, 3)
    POSx = POS[:, :, :, 0]
    POSy = POS[:, :, :, 1]
    POSz = POS[:, :, :, 2]

    if 'b' in bf:
        # calculation of B field
        Bfield_raw = array([my_collection.getB(pos) for pos in POS_raw])

        Bfield = Bfield_raw.reshape(lenx, leny, lenz, 3)
        Bfieldx = Bfield[:, :, :, 0]
        Bfieldy = Bfield[:, :, :, 1]
        Bfieldz = Bfield[:, :, :, 2]

        # plotting
        fig3d_B = figure(num='B 3D')
        ax_B = fig3d_B.add_subplot(projection='3d')
        ax_B.quiver(POSx, POSy, POSz, Bfieldx, Bfieldy, Bfieldz, normalize=True)

    if 'f' in bf:
        # calculation of force field
        FOR_raw = array([getF(pos, my_collection, sample) for pos in POS_raw])

        FOR = FOR_raw.reshape(lenx, leny, lenz, 3)
        FORx = FOR[:, :, :, 0]
        FORy = FOR[:, :, :, 1]
        FORz = FOR[:, :, :, 2]

        # plotting
        fig3d_F = figure(num='F 3D')
        ax_F = fig3d_F.add_subplot(projection='3d')
        ax_F.quiver(POSx, POSy, POSz, FORx, FORy, FORz, normalize=True)
