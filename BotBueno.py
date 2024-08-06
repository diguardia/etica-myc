from BotAbstract import BotAbstract

class BotBueno(BotAbstract):
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        return 'S'