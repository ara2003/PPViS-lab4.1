from src.component.DeadComponent import DeadComponent


class HPDeadComponent(DeadComponent):

    def __init__(self, hp: int):
        self._hp = hp

    @property
    def hp(self):
        return self._hp

    def __str__(self):
        return 'HPDeadComponent({})'.format(self._hp)
