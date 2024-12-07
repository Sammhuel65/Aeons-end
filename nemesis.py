class Nemesis:
  def __init__(self, name, health):
      self.name = name
      self.health = health
      self.deck = ["Attack 1", "Attack 2"]  # Exemple de cartes Némésis

  def play_card(self):
      """Le Némésis joue une carte."""
      if self.deck:
          card = self.deck.pop(0)
          print(f"{self.name} plays {card}.")