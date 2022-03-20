from src.component.Component import Component


class PositionComponent(Component):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return 'PositionComponent ({}, {})'.format(self.x, self.y)
