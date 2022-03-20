from src.entity.World import *
from abc import ABC, abstractmethod


class System(ABC):

    @abstractmethod
    def update(self, world: World):
        pass
