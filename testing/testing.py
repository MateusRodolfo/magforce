from magpylib.source.magnet import Box
from magforce import plot_2D_plane_x,plot_2D_plane_y ,plot_2D_plane_z
from magpylib import Collection, displaySystem
from numpy import linspace, pi

m1 = Box(mag=(0,0,100),
         pos=(0,0,0),
         dim=(2,2,2),
         axis=(0,0,1))

demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]
sample = {'demagnetizing_factor': demagnetizing_factor, 'volume': volume, 'M_saturation': M_saturation}

displaySystem(m1, direc=True)

# plot_2D_plane_x(x=0,
#                 ys=linspace(-5,5,30),
#                 zs=linspace(-5,5,30),
#                 collections={'collection': m1},
#                 sample=sample,
#                 modes=['stream'],
#                 BF='B',
#                 rounding=10,
#                 saveCSV=False,
#                 showim=True)

plot_2D_plane_y(xs=linspace(-5,5,30),
                y=0,
                zs=linspace(-5,5,30),
                collections={'collection': m1},
                sample=sample,
                modes=['stream'],
                BF='B',
                rounding=10,
                saveCSV=False,
                showim=True)

# plot_2D_plane_z(xs=linspace(-5,5,30),
#                 ys=linspace(-5,5,30),
#                 z=0,
#                 collections={'collection': m1},
#                 sample=sample,
#                 modes=['stream'],
#                 BF='B',
#                 rounding=10,
#                 saveCSV=False,
#                 showim=True)

