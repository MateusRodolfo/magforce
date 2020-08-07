from numpy import array, round, zeros, pi, linalg


def normalize(vector):
    """
    -----------
    DESCRIPTION
    -----------

    Transforms a vector into unitary

    ----------
    PARAMETERS
    ----------

    :param vector: numpy.array | input vector, any dimension
    :return: numpy.array | output vector, same dimension as input but norm 1

    -------
    EXAMPLE
    -------
    >>> from numpy import array

    >>> vector3d = array([0,0,2])
    >>> normalize(vector3d)
    array([0., 0., 1.])

    >>> vector2d = array([1,1])
    >>> normalize(vector2d)
    array([0.70710678, 0.70710678])
    """
    norm = linalg.norm(vector)

    if norm != 0:
        return vector/norm
    else:
        return array(vector)


def jac(foo, x, y, z):
    """
    -----------
    DESCRIPTION
    -----------

    From a point xyz and function returns a 3x3 jacobian matrix of that function on that point
    works with 6 auxiliar points, in x,y,z +- infinitesimal
    function foo takes as argument a 1d array like [x, y, z] and returns

    jac uses central difference derivatives

    ----------
    PARAMETERS
    ----------

    :param foo: function | needs to return
    :param x: float
    :param y: float
    :param z: float
    :return: 3x3 array like
                [[dUdx, dUdy, dUdz]
                [dVdx, dVdy, dVdz]
                [dWdx, dWdy, dWdz]]

    -------
    EXAMPLE
    -------

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


def getM(point, collection, sample):
    """
    -----------
    DESCRIPTION
    -----------

    Gets the magnetization of a sample if it would to be put on the point point around a collection of magnets

    ----------
    PARAMETERS
    ----------

    :param point: numpy.array [mm]
    :param collection: magpylib.Collection
    :param sample: dict | keys 'demagnetizing_factor' [], 'volume' [m3] and 'M_saturation' [A/m]
    :return: numpy.array [A/m]

    -------
    EXAMPLE
    -------

    >>> # imports
    >>> from numpy import linspace, pi
    >>> from magpylib.source.magnet import Cylinder
    >>> from magpylib import Collection
    >>> import magforce as mgf

    >>> # Sample Definition
    >>> demagnetizing_factor = 1/3             # sphere
    >>> volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
    >>> M_saturation = 1.400e6                 # Ms Co room temperature [A/m]
    >>> sample = {'demagnetizing_factor': demagnetizing_factor, 'volume': volume, 'M_saturation': M_saturation}

    >>> # Magnet collection definition
    >>> m1 = Cylinder(mag=[0, 0, 1000], dim=[5, 20], pos=[0, 0, -10])
    >>> my_collection = Collection(m1)

    >>> # creation of space
    >>> point = (0,0,1)

    >>> getM(point,my_collection,sample)
    array([     0.        ,      0.        , 741977.47732813])

    """
    mu0 = 4*pi*(10**(-7))                      # vacuum permeability in H/m

    n = sample['demagnetizing_factor']         # demagnetizing factor
    M_saturation = sample['M_saturation']      # Ms in A/m

    B = collection.getB(point) / 1000          # magpylib getB returns B in mT, /1000 for T

    H = B / mu0                                # transform B[T] in H[A/m]
    M = H / n                                  # simplification for getting M out of H in ferromagnetic

    if linalg.norm(M) > M_saturation:          # check if M surpasses the saturation
        M = normalize(M) * M_saturation

    return M                                   # returns (Mx, My, Mz) in [A/m]


def getF(point, collection, sample):
    """
    -----------
    DESCRIPTION
    -----------

    Gets the magnetic force in a point xyz given in mm for a ferromagnetic sphere

    ----------
    PARAMETERS
    ----------

    :param point: numpy.array
    :param collection: magpylib.Collection
    :param sample: dict | keys 'demagnetizing_factor' [], 'volume' [m3] and 'M_saturation' [A/m]
    :return: numpy.array [N]

    -------
    EXAMPLE
    -------

    >>> # imports
    >>> from numpy import linspace, pi
    >>> from magpylib.source.magnet import Cylinder
    >>> from magpylib import Collection
    >>> import magforce as mgf

    >>> # Sample Definition
    >>> demagnetizing_factor = 1/3             # sphere
    >>> volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
    >>> M_saturation = 1.400e6                 # Ms Co room temperature [A/m]
    >>> sample = {'demagnetizing_factor': demagnetizing_factor, 'volume': volume, 'M_saturation': M_saturation}

    >>> # Magnet collection definition
    >>> m1 = Cylinder(mag=[0, 0, 1000], dim=[5, 20], pos=[0, 0, -10])
    >>> my_collection = Collection(m1)

    >>> # creation of space
    >>> point=(0,0,1)

    >>> getF(point,my_collection,sample)
    array([  0.        ,   0.        , -31.77642724])
    """
    x, y, z = point

    V = sample['volume']                           # sample volume [m3]

    Mx, My, Mz = getM(point, collection, sample)   # sample magnetization [A/m]

    dd = jac(collection.getB, x, y, z)             # jacobian of B field in given point

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

    return result                                 # returns (Fx, Fy, Fz) in N
