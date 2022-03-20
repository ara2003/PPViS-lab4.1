from random import choice

from src.Pair import pair
from src.entity.Entity import Entity
from src.world_component.WorldComponent import WorldComponent


class FieldWorldComponent(WorldComponent):
    around4 = (pair(1, 0), pair(-1, 0), pair(0, 1), pair(0, -1))
    around8 = (pair(1, 0), pair(-1, 0), pair(0, 1), pair(0, -1), pair(1, -1), pair(-1, -1), pair(1, 1), pair(-1, 1))

    def __init__(self, x: int, y: int):
        self._cells: list[list[Entity]] = None
        self._x = x
        self._y = y
        self.clear_all()

    def __iter__(self):
        return self._cells.__iter__()

    def get_has_component_around(self, x, y, t):
        f = []
        for a in FieldWorldComponent.around8:
            x0 = x + a.first
            y0 = y + a.second
            if x0 < 0:
                continue
            if y0 < 0:
                continue
            if x0 >= self.x:
                continue
            if y0 >= self.y:
                continue
            e = self.get(x0, y0)
            if e is not None:
                if e.has(t):
                    f.append(e)
        return f

    def set(self, x: int, y: int, e: Entity):
        e0 = self._cells[y][x]
        if e0 is not None:
            raise KeyError(x, y, e0, e)
        self._cells[y][x] = e

    def get(self, x: int, y: int) -> Entity:
        return self._cells[y][x]

    def get_empty_around(self, x: int, y: int) -> pair[int, int]:
        f = []
        for a in FieldWorldComponent.around8:
            x0 = x + a.first
            y0 = y + a.second
            if x0 < 0:
                continue
            if y0 < 0:
                continue
            if x0 >= self.x:
                continue
            if y0 >= self.y:
                continue
            if self.get(x0, y0) is None:
                f.append(a)

        if len(f) == 0:
            return None

        f = choice(f)
        f = pair(f.first + x, f.second + y)

        return f

    def clear_all(self):
        self._cells = [[None for _ in range(self.x)] for _ in range(self.y)]

    def clear(self, x, y):
        self._cells[y][x] = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
