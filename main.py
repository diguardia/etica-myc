import time
from arena import Arena
from bot_bueno import BotBueno
from bot_random import BotRandom
from fixture import Fixture


bots = [BotBueno(), BotRandom(), BotRandom()]
fixture = Fixture(bots)
partidos = fixture.get_fixture()

tabla_posiciones = {}
for bot in bots:
    tabla_posiciones[bot] = 0

numeroDePartido = 1
for bot1, bot2 in partidos:
    print("\nPartido", numeroDePartido)
    print("Combate entre ", bot1.Nombre, bot2.Nombre)
    time.sleep(2)

    puntaje_bot1, puntaje_bot2 = Arena.Jugar(bot1, bot2)
    tabla_posiciones[bot1] += puntaje_bot1
    tabla_posiciones[bot2] += puntaje_bot2


    print("\n\nTabla de Posiciones:")
    sorted_posiciones = sorted(tabla_posiciones.items(), key=lambda x: x[1], reverse=True)
    for bot, puntos in sorted_posiciones:
        print(bot.Nombre, puntos, sep="\t|\t")

