from src.component.HPComponent import *


class AgeComponent(Component):

    def __init__(self, age: int = 40):
        self.age = age

    def is_dead(self):
        return self.age <= 0

    @classmethod
    def required_component(cls):
        return [HPComponent]
