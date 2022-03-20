from src.component.HPComponent import HPComponent
from src.component.MatiralComponent import MaterialComponent


class MeatMaterialComponent(MaterialComponent):

    @classmethod
    def required_component(cls):
        return [HPComponent]
