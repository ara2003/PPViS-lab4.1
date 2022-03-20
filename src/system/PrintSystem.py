from src.component.AgeComponent import AgeComponent
from src.component.HPComponent import HPComponent
from src.world_component.FieldWorldComponent import FieldWorldComponent
from src.system.System import *
from src.component.PositionComponent import *
from src.component.PrintComponent import *


class PrintSystem(System):

    def update(self, world: World):
        r = ''
        for line in world.get_world_component(FieldWorldComponent):
            for e in line:
                if e is None:
                    r += '_'
                else:
                    c = e.get(PrintComponent)
                    if c is None:
                        r += str(e)
                    else:
                        r += c.text
            r += '\n'
        print(r)
