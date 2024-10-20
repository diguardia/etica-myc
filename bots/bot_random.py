import random
from bot_abstract import BotAbstract

class BotRandom(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Random"

    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return random.choice(['M', 'S'])
