from src.component.Component import Component


class PrintComponent(Component):

    def __init__(self, text: str):
        self._text = text

    @property
    def text(self):
        return self._text
