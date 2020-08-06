# taken from https://magpylib.readthedocs.io/en/latest/_pages/2_guideExamples/

from magpylib.source.magnet import Cylinder

s = Cylinder( mag = [0,0,350], dim = [4,5])

print(s.getB([4,4,4]))