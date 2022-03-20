from src.component.AgeComponent import AgeComponent
from src.component.HPComponent import HPComponent
from src.component.HPDeadComponent import HPDeadComponent
from src.component.Move import Move
from src.component.Plant import Plant
from src.component.PositionComponent import PositionComponent
from src.component.PrintComponent import PrintComponent
from src.component.Reproduction import Reproduction
from src.entity.Entity import Entity
from src.entity.World import World
from src.system.System import System
from src.world_component.FieldWorldComponent import FieldWorldComponent


class ReproductionSystem(System):

    def update(self, world: World):
        field = world.get_world_component(FieldWorldComponent)
        for e in world.getHasComponent(Reproduction):
            ehp = e.get(HPComponent)
            pos = e.get(PositionComponent)
            r = e.get(Reproduction)

            empty = field.get_empty_around(pos.x, pos.y)
            if empty is None:
                continue

            ts = field.get_has_component_around(pos.x, pos.y, r.target)
            for t in ts:
                thp = t.get(HPComponent)
                if thp.hp < 20:
                    continue
                if ehp.hp < 20:
                    continue

                thp.hp -= 15
                ehp.hp -= 15

                ne = Entity()
                field.set(empty.first, empty.second, ne)
                world.add(ne)
                ne.add(PositionComponent(empty.first, empty.second))
                ne.add(HPComponent(20))
                ne.add(e.get(PrintComponent))
                ne.add(AgeComponent())
                ne.add(Move())
                ne.add(r)
                ne.add(r.target)
                ne.add(HPDeadComponent(3))

                break



