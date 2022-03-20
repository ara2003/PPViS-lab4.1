from src.component.Component import Component
from src.component.HPComponent import HPComponent


class DeadComponent(Component):

    @classmethod
    def required_component(cls):
        return [HPComponent]
