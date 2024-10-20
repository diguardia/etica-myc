from bot_abstract import BotAbstract

class BotMessi(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Messi"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return 'M'  # Y sino muestro
