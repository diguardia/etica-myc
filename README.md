# Sapos y Murciélagos

## Descripción
Este proyecto de la materia "Ética y Deontología" contiene BOTs que jugarán el juego "Sapos y Murciélagos" visto en clase. 

## Clases Principales

### Arbitro
La clase `Arbitro` es responsable de calcular los puntajes de las jugadas realizadas por los bots. Contiene el método estático `calcular_puntaje_jugada` que toma las jugadas de ambos bots y devuelve los puntajes correspondientes.

### BotAbstract
Todos los BOTs "heredan" de Bot Abstract. Es decir, todos los bots que hagamos tendrán que respetar lo definido en esta clase. Por ejemplo, todos los BOTs tendrá un nombre y sabrán jugar.

## Clase BotRandom
La clase `BotRandom` es una implementación de un bot que juega de forma aleatoria. No sigue ninguna estrategia específica y simplemente elige sus jugadas al azar.

## Clase BotBueno
La clase `BotBueno` es una implementación de un bot que juega siempre "Sapo".

## main.py
En este archivo, se encuentra la ejecución principal del programa


