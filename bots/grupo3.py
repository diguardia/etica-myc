from bot_abstract import BotAbstract

class armagedon(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Armagedon"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return 'M'
    



