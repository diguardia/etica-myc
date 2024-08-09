from arbitro import Arbitro
from bot_bueno import BotBueno
from bot_random import BotRandom


bot_bueno = BotBueno()
bot_random = BotRandom()
bot_random2 = BotRandom()

from bot_abstract import BotAbstract
def Jugar(bot1: BotAbstract, bot2: BotAbstract):
    puntaje_bot1 = 0
    puntaje_bot2 = 0
    jugada_previa_bot1 = None
    jugada_previa_bot2 = None
    
    for i in range(20):
        jugada_bot1 = bot1.Jugar(i, jugada_previa_bot2) 
        jugada_bot2 = bot2.Jugar(i, jugada_previa_bot1) 

        jugada_previa_bot1 = jugada_bot1
        jugada_previa_bot2 = jugada_bot2

        
        puntos_bot1, puntos_bot2 = Arbitro.calcular_puntaje_jugada(jugada_bot1, jugada_bot2)

        puntaje_bot1 += puntos_bot1
        puntaje_bot2 += puntos_bot2 

        print (i , jugada_bot1, jugada_bot2, puntaje_bot1, puntaje_bot2, sep='\t')
    return puntaje_bot1, puntaje_bot2



puntaje_bot_bueno, puntaje_bot_random = Jugar(bot_random2, bot_random)

print("Puntaje del BotBueno:", puntaje_bot_bueno)
print("Puntaje del BotRandom:", puntaje_bot_random)