import random
from bot_abstract import BotAbstract

class BotGrupo1(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Grupo1"

    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        opciones = ['M', 'S']
        probalidades = [0.88, 0.12]
        return random.choices(opciones, weights=probalidades, k=1) [0]