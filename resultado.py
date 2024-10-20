from rich.console import Console
from rich.table import Table

class Resultado:
    def __init__(self):
        self.resultados = []

    def agregar_resultado(self, bot1, bot2, puntaje_bot1, puntaje_bot2):
        self.resultados.append({
            "bot1": bot1.Nombre,
            "bot2": bot2.Nombre,
            "puntaje_bot1": puntaje_bot1,
            "puntaje_bot2": puntaje_bot2
        })

    def imprimir_tabla(self):
        console = Console()
        table = Table(title="Resultados de los Partidos")

        table.add_column("Partido", justify="center")
        table.add_column("Bot 1", justify="center")
        table.add_column("Puntaje Bot 1", justify="center")
        table.add_column("Bot 2", justify="center")
        table.add_column("Puntaje Bot 2", justify="center")

        for i, resultado in enumerate(self.resultados, start=1):
            table.add_row(
                str(i),
                resultado["bot1"],
                str(resultado["puntaje_bot1"]),
                resultado["bot2"],
                str(resultado["puntaje_bot2"])
            )

        console.print(table)