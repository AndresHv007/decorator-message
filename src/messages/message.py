from abc import ABC, abstractmethod
class Message(ABC):
    @abstractmethod
    def render(self) -> str: raise NotImplementedError
