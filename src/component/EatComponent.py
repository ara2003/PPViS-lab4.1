from src.component.Component import Component
from src.component.HPComponent import HPComponent
from src.component.PositionComponent import PositionComponent


class EatComponent(Component):

    def __init__(self, target: type):
        self._target = target
        if HPComponent not in target.required_component():
            raise ValueError(target, target.required_component())

    @property
    def target(self):
        return self._target

    @classmethod
    def required_component(cls):
        return [PositionComponent, HPComponent]
