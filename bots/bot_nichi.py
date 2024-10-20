from bot_abstract import BotAbstract

class BotNichii(BotAbstract):
    
    def __init__(self):
        self.turno = 0  # Contador de turnos específico para cada combate
    
    @property
    def Nombre(self) -> str:
        return "Bot Nichii Estratégico"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        # Jugar "Sapo" en los turnos 15 y 17
        if jugada_numero == 15 or jugada_numero == 17:
            return 'S'
        else:
            # En otros turnos, aplicar la estrategia estándar
            if jugada_previa_oponente == 'S':
                return 'M'  # Murciélago gana a Sapo (2 a -2)
            else:
                return 'M'  # Empate si ambos juegan Murciélago (0 a 0)
