# Importamos la funcion Random
import random
# Importamos el modulo bot_abstract.py
from bot_abstract import BotAbstract

# Creamos una clase llamada Bot_las_Chicas_Super_Poderosas que seguira lo dictado en BotAbstract  
class Bot_las_Chicas_Super_Poderosas(BotAbstract):
    @property
    def Nombre(self) -> str:
        return "Las Chicas Super Poderosas"
    
    # Creamos una funcion para que las jugadas del oponente se guarden en una lista
    def __init__(self):
        self.historial_oponente = []
    
    # Con la funcion de Jugar vamos ir agregando las jugadas del oponente dentro de la lista
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_previa_oponente:
            self.historial_oponente.append(jugada_previa_oponente)

        # Vamos a contar los elementos y vamos a trabajar con el ultimo y el penultimo
        if len(self.historial_oponente) > 1:
            ultima_jugada = self.historial_oponente[-1]
            penultima_jugada = self.historial_oponente[-2]

            # Si el oponente juega "Sapo" en su ultima y penultima jugada
            if ultima_jugada == 'S' and penultima_jugada == 'S':
                return 'M' #Entonces retorna Murcielago
            # Si el oponente juega "Murciélago" en sus ultimas 2 partidas
            elif ultima_jugada == 'M' and penultima_jugada == 'M':
                return 'S' #Entonces retorna Sapo
            else:
                # Si ninguna de las 2 condiciones se cumple entonces introduce aleatoriedad
                return random.choice(['M', 'S'])
        else:
            # Y bueno la primera jugada al no tener registros de jugadas anteriores la vamos eligir aleatoriamente
            return random.choice(['M', 'S'])









