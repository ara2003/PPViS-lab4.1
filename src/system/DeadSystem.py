from src.component.DeadComponent import DeadComponent
from src.component.HPComponent import *
from src.component.HPDeadComponent import HPDeadComponent
from src.component.LeafMatiralComponent import *
from src.component.MeatMatiralComponent import *
from src.component.PrintComponent import PrintComponent

from src.system.System import *
from src.component.PositionComponent import *
from src.component.AgeComponent import *


class DeadSystem(System):

    def update(self, world: World):
        for e in world.getHasComponent(DeadComponent):
            hp = e.get(HPComponent)
            if hp.is_dead():
                world.remove(e)
                pos = e.get(PositionComponent)
                leaf = e.get(LeafMaterialComponent)
                hp = hp.hp
                d = e.get(HPDeadComponent)
                if d is not None:
                    hp += d.hp
                if hp <= 0:
                    return
                if leaf is not None:
                    ne = Entity()
                    ne.add(pos)
                    ne.add(HPComponent(hp))
                    ne.add(AgeComponent(10))
                    ne.add(DeadComponent())
                    ne.add(leaf)
                    ne.add(PrintComponent('l'))
                    world.add(ne)
                else:
                    meat = e.get(MeatMaterialComponent)
                    if meat is not None:
                        ne = Entity()
                        ne.add(pos)
                        ne.add(HPComponent(hp))
                        ne.add(meat)
                        ne.add(AgeComponent(10))
                        ne.add(DeadComponent())
                        ne.add(PrintComponent('m'))
                        world.add(ne)
