from src.component.HPComponent import *
from src.component.MeatMatiralComponent import MeatMaterialComponent
from src.component.Move import Move
from src.component.PositionComponent import PositionComponent
from src.component.Reproduction import Reproduction


class Wolf(Component):

    @classmethod
    def required_component(cls):
        return [MeatMaterialComponent, PositionComponent, Reproduction, Move]
