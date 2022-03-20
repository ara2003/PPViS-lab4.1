from random import randint

from src.component.EatComponent import *
from src.component.HPComponent import *

from src.system.System import *
from src.world_component.FieldWorldComponent import FieldWorldComponent


class EatSystem(System):

    def update(self, world: World):
        field = world.get_world_component(FieldWorldComponent)
        for e in world.getHasComponent(EatComponent):
            hp = e.get(HPComponent)
            pos = e.get(PositionComponent)
            eat = e.get(EatComponent)

            ts = field.get_has_component_around(pos.x, pos.y, eat.target)

            for t in ts:
                thp = t.get(HPComponent)

                hp.hp -= 1

                if randint(0, 1) == 0:
                    ghp = min(5, thp.hp)
                    hp.hp += ghp
                    thp.hp -= ghp
                    break
