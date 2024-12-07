import random

class Game:
    def __init__(self, players, nemesis):
        self.players = players
        self.nemesis = nemesis
        self.turn_order = []

    def setup_turn_order(self):
        """Détermine un ordre de tour aléatoire."""
        self.turn_order = self.players + [self.nemesis]
        random.shuffle(self.turn_order)

    def play(self):
        """Boucle principale du jeu."""
        self.setup_turn_order()
        print("Game starts!")

        while self.nemesis.health > 0 and any(player.health > 0 for player in self.players):
            for entity in self.turn_order:
                if isinstance(entity, Player):
                    print(f"{entity.name}'s turn.")
                    entity.draw()
                elif isinstance(entity, Nemesis):
                    print(f"{entity.name}'s turn.")
                    entity.play_card()

        print("Game Over!")