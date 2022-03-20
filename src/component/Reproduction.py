from src.component.Component import Component
from src.component.HPComponent import HPComponent
from src.component.Move import Move
from src.component.PositionComponent import PositionComponent


class Reproduction(Component):

    def __init__(self, target: type):
        self._target = target
        if Reproduction not in target.required_component():
            raise ValueError(target, target.required_component())

    @property
    def target(self):
        return self._target

    @classmethod
    def required_component(cls):
        return [HPComponent, PositionComponent, Move]