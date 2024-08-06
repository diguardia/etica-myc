from BotBueno import BotBueno
from BotRandom import BotRandom


bot_bueno = BotBueno()
bot_random = BotRandom()

from BotAbstract import BotAbstract
def Jugar(bot1: BotAbstract, bot2: BotAbstract):
    puntaje_bot1 = 0
    puntaje_bot2 = 0
    jugada_bot1 = None
    jugada_bot2 = None
    
    for i in range(10):
        jugada_bot1 = bot1.Jugar(i, jugada_bot2) 
        jugada_bot2 = bot2.Jugar(i, jugada_bot1) 

        if jugada_bot1 == "M" and jugada_bot2 == "M":
            puntaje_bot1 += 0
            puntaje_bot2 += 0
        elif jugada_bot1 == "M" and jugada_bot2 == "S":
            puntaje_bot1 += 2
            puntaje_bot2 += -1
        elif jugada_bot1 == "S" and jugada_bot2 == "S":
            puntaje_bot1 += 1
            puntaje_bot2 += 1
        elif jugada_bot1 == "S" and jugada_bot2 == "M":
            puntaje_bot1 += -1
            puntaje_bot2 += 2

        print (i, jugada_bot1, jugada_bot2, puntaje_bot1, puntaje_bot2)
    return puntaje_bot1, puntaje_bot2


puntaje_bot_bueno, puntaje_bot_random = Jugar(bot_bueno, bot_random)
print("Puntaje del BotBueno:", puntaje_bot_bueno)
print("Puntaje del BotRandom:", puntaje_bot_random)