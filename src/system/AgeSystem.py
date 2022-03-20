
from src.component.AgeComponent import AgeComponent
from src.component.HPComponent import *

from src.system.System import *


class AgeSystem(System):

    def update(self, world: World):
        for e in world.getHasComponent(AgeComponent):
            age = e.get(AgeComponent)
            hp = e.get(HPComponent)
            hp.hp = min(hp.hp, age.age)
