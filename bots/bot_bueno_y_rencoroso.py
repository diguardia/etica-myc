from bot_abstract import BotAbstract

class BotBuenoYRencoroso(BotAbstract):
    recibioAlgunMurcielago = False

    @property
    def Nombre(self) -> str:
        return "Bueno y Rencoroso"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_previa_oponente == 'M':
            self.recibioAlgunMurcielago = True
        
        if self.recibioAlgunMurcielago:
            return 'M'
        else:
            return 'S'
    
    