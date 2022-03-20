
from typing import TypeVar

from src.component.Component import Component


class Entity:
    C = TypeVar('C')

    def __init__(self):
        self._components = {}

    def __str__(self):
        return self.__repr__()

    def components(self):
        return set(self._components.values())

    def __repr__(self):
        return 'Entity ' + str(self.components())

    def add(self, component: Component) -> None:
        self.__add(component, type(component))

        for rct in component.required_component():
            if not self.has(rct):
                c = rct()
                self.add(c)

    def __add(self, component, cls):
        if cls == Component:
            return

        if not issubclass(cls, Component):
            return

        if self.has(cls):
            raise ValueError(cls)

        self._components[cls] = component

        for s in cls.mro()[1::]:
            self.__add(component, s)

    def has(self, cls: type) -> bool:
        return cls in self._components

    def get(self, cls: type[C]) -> C:
        return self._components.setdefault(cls, None)

    def __iter__(self):
        return self.components().__iter__()

    def remove_class(self, cls: type[C]) -> C:
        self._components.pop(cls)

    def remove(self, component: Component):
        return self.remove_class(type(component))

