from random import randint

from src.component.AgeComponent import AgeComponent
from src.component.HPComponent import HPComponent
from src.component.HPDeadComponent import HPDeadComponent
from src.component.Plant import Plant
from src.component.PositionComponent import PositionComponent
from src.component.PrintComponent import PrintComponent
from src.system.System import *
from src.world_component.FieldWorldComponent import FieldWorldComponent


class GemmationSystem(System):

    def update(self, world: World):
        field = world.get_world_component(FieldWorldComponent)
        for e in world.getHasComponent(Plant):
            hp = e.get(HPComponent)
            pos = e.get(PositionComponent)
            if hp.hp > 30:
                pos = field.get_empty_around(pos.x, pos.y)
                if pos is None:
                    continue
                hp.hp -= 20
                ne = Entity()
                field.set(pos.first, pos.second, ne)
                world.add(ne)
                ne.add(PositionComponent(pos.first, pos.second))
                ne.add(HPComponent(10))
                ne.add(PrintComponent('p'))
                ne.add(AgeComponent())
                ne.add(Plant())
                ne.add(HPDeadComponent(3))

