import json
from abc import *


class JSONSerializable(ABC):

    @abstractmethod
    def serializable(self) -> json:
        pass

    @abstractmethod
    def deserializable(self) -> json:
        pass
