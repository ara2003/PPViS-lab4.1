from src.component.Component import Component
from src.component.HPComponent import HPComponent
from src.component.MatiralComponent import MaterialComponent


class LeafMaterialComponent(MaterialComponent):

    @classmethod
    def required_component(cls):
        return [HPComponent]


