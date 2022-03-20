from src.component.AgeComponent import AgeComponent
from src.component.HPComponent import HPComponent
from src.world_component.FieldWorldComponent import FieldWorldComponent
from src.system.System import *
from src.component.PositionComponent import *
from src.component.PrintComponent import *


class UpdateFieldSystem(System):

    def update(self, world: World):
        field = world.get_world_component(FieldWorldComponent)
        field.clear_all()
        for e in world.getHasComponent(PositionComponent):
            pos = e.get(PositionComponent)
            field.set(pos.x, pos.y, e)
