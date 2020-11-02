from Obstacles import *
from Obstacle import Obstacle
from Line import Line
import ServerOperations
import Saved
from Trick import *

"""
kickflip = FlatTrick("Kickflip", 0, -1, 0)
ollie = FlatTrick("Ollie", 0, 0, 0)
heelflip = FlatTrick("Heelflip", 0, 1, 0)
backside180 = FlatTrick("Backside 180", 1, 0, 1)
frontside180 = FlatTrick("Frontside 180", -1, 0, -1)
backsidebigspin = FlatTrick("Backside Bigspin", 2, 0, 1)
frontsidebigspin = FlatTrick("Frontside Bigspin", -2, 0, 1)
grind5050 = GrindTrick("50-50")
treflip = FlatTrick("360 Flip", 2, -1, 0)
CrookedGrind = GrindTrick("Crooked Grind")
"""



for x in Saved.tricks:
    print(Saved.tricks[x].type)


