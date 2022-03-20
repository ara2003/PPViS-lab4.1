from builtins import isinstance
from typing import final

from src.entity.Entity import *
from src.world_component.WorldComponent import *


@final
class World:

    WC = TypeVar('WC')

    def __init__(self):
        self._entities: list[Entity] = []
        self._components: list[WorldComponent] = []

    def get_world_component(self, cls: type[WC]) -> WC:
        for wc in self._components:
            if isinstance(wc, cls):
                return wc

    def add_world_component(self, wc: WorldComponent):
        self._components.append(wc)

    def getHasComponent(self, cls):
        res = []
        for e in self:
            if e.has(cls):
                res.append(e)
        return res

    def getHasComponents(self, clses):
        res = []
        for e in self:
            f = True
            for c in clses:
                if not e.has(c):
                    f = False
                    break
            if f:
                res.append(e)
        return res

    def add(self, entity: Entity):
        self._entities.append(entity)

    def remove(self, entity: Entity):
        self._entities.remove(entity)

    def __iter__(self) -> tuple[Entity]:
        return self._entities.__iter__()

    def __str__(self) -> str:
        res = ''
        for e in self:
            res += e.__str__()
            res += ' '

        return res
