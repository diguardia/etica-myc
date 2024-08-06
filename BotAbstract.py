from abc import ABC, abstractmethod

class BotAbstract(ABC):
    
    @abstractmethod
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        pass