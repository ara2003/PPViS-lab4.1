from random import randint

from src.component.AgeComponent import AgeComponent
from src.system.System import *


class SubAgeSystem(System):

    def update(self, world: World):
        for e in world.getHasComponent(AgeComponent):
            if randint(1, 4) == 1:
                age = e.get(AgeComponent)
                age.age -= 1
