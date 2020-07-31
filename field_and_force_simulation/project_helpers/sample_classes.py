from numpy import pi


class Material():
    def __init__(self, material, temperature):
        if material.title() == 'Fe':
            self.M_saturation = 1.707e6  # Ms room temperature [A/m]
        if material.title() == 'Co':
            self.M_saturation = 1.400e6  # Ms room temperature [A/m]


class Shape():
    def __init__(self, shape, dim):
        """
        :param shape: str
        :param dim: list of dimensions [mm]
        """
        if shape.lower() == 'sphere':
            self.demagnetizing_factor = 1 / 3
            self.radius = dim[0] / 2                              # [mm]
            self.volume = 4 / 3 * pi * (self.radius / 1000) ** 3  # V [m3]


class Sample(Material, Shape):
    def __init__(self, material='Fe', temperature=300, shape='sphere', dim=[2]):
        """
        :param material: str | Fe, Co
        :param temperature: float
        :param shape: str | 'sphere'
        :param dim: list | len depends on shape used [mm]
        """
        Material.__init__(self, material=material, temperature=temperature)
        Shape.__init__(self, shape=shape, dim=dim)
