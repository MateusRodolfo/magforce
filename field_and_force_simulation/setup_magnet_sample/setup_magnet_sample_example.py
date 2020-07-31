# made with magpylib v2.3.0b

from matplotlib.pyplot import figure

from magpylib.source.magnet import Cylinder, Sphere
from magpylib.source.current import Circular
from magpylib import Collection, displaySystem

from project_helpers.sample_classes import Sample


# Sample Definition
sample = Sample(material='Fe',
                temperature=300,
                shape='sphere',
                dim=[2])

# Magnet collection definition
m1 = Cylinder(mag=[0, 0, 1000], dim=[5, 20], pos=[0, 0, -10])
my_collection = Collection(m1)

display_collection = 0
if display_collection:
    sample_sphere = Sphere(mag=[0, 0, 1000], dim=sample.radius, pos=[0, 0, 0])
    my_collection_with_sample = Collection(my_collection, sample_sphere)

    fig = figure(num='System Display')
    ax = fig.add_subplot(projection='3d')
    displaySystem(my_collection_with_sample, direc=True, markers=[(0, 0, 0)], suppress=False, subplotAx=ax)

# sample and my_collection will be imported in simulation_example.py
