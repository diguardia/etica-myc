class Arbitro:
    @staticmethod
    def calcular_puntaje_jugada(jugada_bot1, jugada_bot2):
        if jugada_bot1 == "M" and jugada_bot2 == "M":
            puntos_bot1 = 0
            puntos_bot2 = 0
        elif jugada_bot1 == "M" and jugada_bot2 == "S":
            puntos_bot1 = 2
            puntos_bot2 = -1
        elif jugada_bot1 == "S" and jugada_bot2 == "S":
            puntos_bot1 = 1
            puntos_bot2 = 1
        elif jugada_bot1 == "S" and jugada_bot2 == "M":
            puntos_bot1 = -1
            puntos_bot2 = 2
        return puntos_bot1, puntos_bot2
