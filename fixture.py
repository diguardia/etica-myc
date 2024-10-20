from itertools import combinations
from typing import List, Tuple

from bot_abstract import BotAbstract
import random

class Fixture:
    def __init__(self, bots: List[BotAbstract]):
        self.bots = bots
        self.fixture = self._generate_fixture()
        self.fixture.extend([(bot, bot) for bot in self.bots])
        random.shuffle(self.fixture)

    def _generate_fixture(self) -> List[Tuple[BotAbstract, BotAbstract]]:
        return list( combinations(self.bots, 2))

    def get_fixture(self) -> List[Tuple[BotAbstract, BotAbstract]]:
        return [(bot1, bot2) for bot1, bot2 in self.fixture]
