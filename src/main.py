from time import sleep

from src.Pair import *
from src.component.EatComponent import EatComponent

from src.component.HPDeadComponent import *
from src.component.Herbivore import Herbivore
from src.component.Move import Move
from src.component.Plant import *
from src.component.Reproduction import Reproduction
from src.component.Wolf import Wolf
from src.system.AgeSystem import *
from src.system.EatSystem import EatSystem
from src.system.GemmationSystem import GemmationSystem
from src.system.MoveSystem import MoveSystem
from src.system.PhotosynthesisSystem import *
from src.system.ReproductionSystem import ReproductionSystem
from src.system.SubAgeSystem import *
from src.system.DeadSystem import *
from src.system.PrintSystem import *
from src.system.System import *
from src.entity.World import *
from src.system.UpdateFieldSystem import UpdateFieldSystem

world = World()
systems: list[System] = []

def add_entity(name: str, x: int, y: int):
    e = Entity()
    world.add(e)
    e.add(HPComponent(20))
    e.add(PositionComponent(x, y))
    e.add(PrintComponent(name))
    e.add(AgeComponent())
    e.add(HPDeadComponent(3))
    return e


def add_plant(p):
    e = add_entity('p', int(p[0]), int(p[1]))
    e.add(Plant())


def add_wolf(p):
    e = add_entity('w', int(p[0]), int(p[1]))
    e.add(EatComponent(MeatMaterialComponent))
    e.add(Reproduction(Wolf))
    e.add(Wolf())


def add_herbivore(p):
    e = add_entity('h', int(p[0]), int(p[1]))
    e.add(EatComponent(LeafMaterialComponent))
    e.add(Reproduction(Herbivore))
    e.add(Herbivore())


def step_c(c: int):
    for _ in range(c):
        for system in systems:
            system.update(world)


def step(p):
    if len(p) > 0:
        step_c(int(p[0]))
    else:
        step_c(1)

if __name__ == "__main__":
    world.add_world_component(FieldWorldComponent(10, 10))

    systems.append(UpdateFieldSystem())
    systems.append(PrintSystem())
    systems.append(SubAgeSystem())
    systems.append(EatSystem())
    systems.append(PhotosynthesisSystem())
    systems.append(AgeSystem())
    systems.append(DeadSystem())
    systems.append(GemmationSystem())
    systems.append(ReproductionSystem())
    systems.append(MoveSystem())

    add_plant([5, 5])
    add_wolf([5, 4])
    add_wolf([4, 5])
    add_herbivore([1, 2])
    add_herbivore([1, 4])

    commands = {'exit': lambda params: exit(0), 'add_p': add_plant, 'add_h': add_herbivore, 'add_w': add_wolf, 's': step}

    for f in (step, add_wolf, add_plant, add_herbivore):
        commands[f.__name__] = f

    while True:
        s = input().split()
        try:
            c = commands[s[0]]
        except KeyError:
            print('unknown command ' + s[0])
            continue

        if len(s) > 1:
            c(s[1::])
        else:
            c([])
