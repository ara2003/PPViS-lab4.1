from src.component.Component import Component


class HPComponent(Component):

    def __init__(self, hp: int) -> None:
        self.hp = hp
        if self.is_dead():
            raise ValueError()

    def is_dead(self) -> bool:
        return self.hp <= 0

    def __str__(self):
        return 'HPComponent ({})'.format(self.hp)
