
from src.component.Plant import *

from src.system.System import *


class PhotosynthesisSystem(System):


    def update(self, world: World):
        for e in world.getHasComponent(Plant):
            hp = e.get(HPComponent)
            hp.hp += 1
