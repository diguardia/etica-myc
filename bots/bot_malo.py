from bot_abstract import BotAbstract

class BotMalo(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Malo"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return 'M'
    
    