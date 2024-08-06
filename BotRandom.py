import random
from BotAbstract import BotAbstract

class BotRandom(BotAbstract):
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return random.choice(['M', 'S'])
