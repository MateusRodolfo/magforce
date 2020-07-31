# made with magpylib v2.3.0b
from numpy import array, round, zeros, pi, linalg


def normalize(vector):
    norm = linalg.norm(vector)

    if norm != 0:
        return vector/norm
    else:
        return array(vector)


def jac(foo, x, y, z):
    """
    From a point xyz and function returns a 3x3 jacobian matrix of that function on that point
    works with 6 auxiliar points, in x,y,z +- infinitesimal
    function foo takes as argument a 1d array like [x, y, z]
    
    jac uses central difference derivatives
    
    returns a 3x3 array like
    [[dUdx, dUdy, dUdz]
     [dVdx, dVdy, dVdz]
     [dWdx, dWdy, dWdz]]

    >>> def foo(point):
    ...     x, y, z = point
    ...     u = x*y*z
    ...     v = y**2 - x**2
    ...     w = z**2 - x*y
    ...     result = (u, v, w)
    ...     return result
    ...

    >>> foo([1,-2,3])
    (-6, 3, 11)

    >>> jac(foo,1,-2,3)
    array([[-6.,  3., -2.],
           [-2., -4.,  0.],
           [ 2., -1.,  6.]])
    """

    delta = 0.0000001                            # infinitesimal

    fxm = foo([x - delta, y, z])                 # point x - delta
    fxp = foo([x + delta, y, z])                 # point x + delta
    fym = foo([x, y - delta, z])                 # point y - delta
    fyp = foo([x, y + delta, z])                 # point y + delta
    fzm = foo([x, y, z - delta])                 # point z - delta
    fzp = foo([x, y, z + delta])                 # point z + delta

    # derivative using central difference formula

    dd = zeros((3, 3))                           # creation of 3x3 matrix of zeros, to have values replaced

    double_delta = 2 * delta

    dd[0, 0] = (fxp[0] - fxm[0]) / double_delta  # dUdx
    dd[1, 0] = (fxp[1] - fxm[1]) / double_delta  # dVdx
    dd[2, 0] = (fxp[2] - fxm[2]) / double_delta  # dWdx

    dd[0, 1] = (fyp[0] - fym[0]) / double_delta  # dUdy
    dd[1, 1] = (fyp[1] - fym[1]) / double_delta  # dVdy
    dd[2, 1] = (fyp[2] - fym[2]) / double_delta  # dWdy

    dd[0, 2] = (fzp[0] - fzm[0]) / double_delta  # dUdz
    dd[1, 2] = (fzp[1] - fzm[1]) / double_delta  # dVdz
    dd[2, 2] = (fzp[2] - fzm[2]) / double_delta  # dWdz

    dd = round(dd, 5)                            # rounding result

    return dd


def getM(point, my_collection, sample):
    mu0 = 4*pi*(10**(-7))                      # vacuum permeability in H/m

    n = sample.demagnetizing_factor            # coefficient de champ démagnétisant
    M_saturation = sample.M_saturation         # Ms in T

    B = my_collection.getB(point) / 1000       # B comes in mT, /1000 for T

    H = B / mu0                                # transform B in H
    M = H / n                                  # formule Beaugnon

    if linalg.norm(M) > M_saturation:
        M = normalize(M) * M_saturation

    return M


def getF(point, my_collection, sample):
    """
    Gets the magnetic force in a point xyz given in mm for a ferromagnetic sphere

    >>> getF([0,0,0])
    array([0., 0., 0.])
    """
    x, y, z = point

    V = sample.volume                          # vol in m3, 1mm radius

    Mx, My, Mz = getM(point, my_collection, sample)

    dd = jac(my_collection.getB, x, y, z)

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

    result = round(array([Fx, Fy, Fz]) * V, 10)

    return result
