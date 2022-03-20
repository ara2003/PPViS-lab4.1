from src.component.Component import Component
from src.component.PositionComponent import PositionComponent


class Move(Component):

    @classmethod
    def required_component(cls):
        return [PositionComponent]
