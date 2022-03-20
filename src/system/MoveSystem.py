
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


class MoveSystem(System):

    def update(self, world: World):
        field = world.get_world_component(FieldWorldComponent)
        for e in world.getHasComponent(Move):
            pos = e.get(PositionComponent)

            empty = field.get_empty_around(pos.x, pos.y)
            if empty is None:
                continue

            field.clear(pos.x, pos.y)
            pos.x = empty.first
            pos.y = empty.second
            field.set(pos.x, pos.y, e)
