from numpy import array, savetxt, vstack, hstack, round, pi, linspace
from matplotlib.pyplot import figure, show
from mpl_toolkits.mplot3d import axes3d
from datetime import datetime
from os import mkdir
from magpylib.source.magnet import Box

demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]
sample = {'demagnetizing_factor': demagnetizing_factor, 'volume': volume, 'M_saturation': M_saturation}

m1 = Box(mag=(0,0,100),
         pos=(0,0,0),
         dim=(2,2,2))

xs=linspace(-10,10,30)
ys=linspace(-10,10,30)
z=0
collections={'m1':m1}
sample=sample
modes=['stream']
BF='B'
rounding=5
showim=True

# get array length to reshape B or F array correctly
lenxs = len(xs)
lenys = len(ys)

# generate points for B and F calculation, no reshape done yet, raw array
POS_raw = array([(x, y, z) for y in ys for x in xs])

# reshaping and splitting needed for matplotlib.pyplot.streamplot and plot_surface
POS = POS_raw.reshape(lenxs, lenys, 3)
POSx = POS[:, :, 0]
POSy = POS[:, :, 1]

for i, pair in enumerate(collections.items()):
    name, collection = pair

    # calculate B in mT, no reshape done yet, raw array
    B_field_raw = array([collection.getB(pos) for pos in POS_raw])

    # rounding
    if rounding != None:
        B_field_raw = round(B_field_raw, rounding)

    # reshaping and splitting needed for matplotlib.pyplot.streamplot and plot_surface
    B_field = B_field_raw.reshape(lenxs, lenys, 3)
    Bx = B_field[:, :, 0]
    By = B_field[:, :, 1]
    Bz = B_field[:, :, 2]

    # if user wants stream plotting
    if 'stream' in modes:
        # creation of figure to host the plot
        fig_B_stream = figure(num=f'''B z = {z} stream; {name}''')
        ax_B_stream = fig_B_stream.add_subplot(aspect=1, title=f'''B direction, z = {z}; {name}''')

        ax_B_stream.streamplot(POSx, POSy, Bx, By, density=3)
        ax_B_stream.set_xlabel('x [mm]')
        ax_B_stream.set_ylabel('y [mm]')

if showim:
    show()