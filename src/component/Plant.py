from src.component.Component import Component

from src.component.LeafMatiralComponent import *
from src.component.HPComponent import *
from src.component.PositionComponent import PositionComponent


class Plant(Component):

    @classmethod
    def required_component(cls):
        return [LeafMaterialComponent, HPComponent, PositionComponent]
