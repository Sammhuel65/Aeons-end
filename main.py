from game import Game
from player import Player
from nemesis import Nemesis

if __name__ == "__main__":
    # Création des joueurs
    players = [Player("Player 1", 10), Player("Player 2", 10)]

    # Création du Némésis
    nemesis = Nemesis("Rageborn", 70)

    # Initialisation et démarrage du jeu
    game = Game(players, nemesis)
    game.play()