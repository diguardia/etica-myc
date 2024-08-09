from abc import ABC, abstractmethod

class BotAbstract(ABC):
    
    @property
    @abstractmethod
    def Nombre(self) -> str:
        pass
    
    @abstractmethod
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        pass

    