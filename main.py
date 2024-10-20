import sys
import time
from arena import Arena
from bots.bot_bueno import BotBueno
from bots.bot_bueno_y_rencoroso import BotBuenoYRencoroso
from bots.bot_grupo1 import BotGrupo1
from bots.bot_messi import BotMessi
from bots.bot_nichi import BotNichii
from bots.bot_poderosa import Bot_las_Chicas_Super_Poderosas
from bots.bot_random import BotRandom
from bots.bot_malo import BotMalo
from bots.bot_desconocido import Botdesconocido
from bots.grupo3 import armagedon

from fixture import Fixture
from rich.console import Console
from rich.table import Table

from resultado import Resultado

resultado = Resultado()

bots = [BotMessi(), armagedon(), Bot_las_Chicas_Super_Poderosas(), BotNichii()
        , BotGrupo1(), BotBuenoYRencoroso(), Botdesconocido()]
#bots = [BotBueno(), BotMalo()]
fixture = Fixture(bots)
partidos = fixture.get_fixture()

table = Table(title="Fixture")
table.add_column("#")
table.add_column("Bot 1")
table.add_column("Bot 2")

for i, (bot1, bot2) in enumerate(partidos, start=1):
    table.add_row(str(i), bot1.Nombre, bot2.Nombre)

console = Console()
console.print(table)
time.sleep(10)

tabla_posiciones = {}
partidos_jugados = {}

for bot in bots:
    tabla_posiciones[bot] = 0
    partidos_jugados[bot] = 0

numeroDePartido = 1
for bot1, bot2 in partidos:
    print("\nPartido #" + str(numeroDePartido) + ": " + bot1.Nombre + " vs " + bot2.Nombre)
    time.sleep(2)

    bot1Juego = bot1.__class__()
    bot2Juego = bot2.__class__()
    
    puntaje_bot1, puntaje_bot2 = Arena.Jugar(bot1Juego, bot2Juego)
    tabla_posiciones[bot1] += puntaje_bot1
    tabla_posiciones[bot2] += puntaje_bot2

    partidos_jugados[bot1] += 1
    partidos_jugados[bot2] += 1

    print("\n\n")
    sorted_posiciones = sorted(tabla_posiciones.items(), key=lambda x: x[1], reverse=True)
    table = Table(title="Tabla de posiciones")
    table.add_column("#")
    table.add_column("Bot")
    table.add_column("PJ")
    table.add_column("Puntos")

    console = Console()
    posicion = 1
    for bot, puntos in sorted_posiciones:
        table.add_row(str(posicion), bot.Nombre, str(partidos_jugados[bot]), str(puntos))
        posicion += 1
    
    console.print(table)

    resultado.agregar_resultado(bot1, bot2, puntaje_bot1, puntaje_bot2)

    numeroDePartido += 1
    if len(sys.argv) > 1 and sys.argv[1] == "fast":
        continue
    else:
        time.sleep(4)


resultado.imprimir_tabla()
