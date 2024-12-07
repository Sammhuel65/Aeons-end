class Card:
  def __init__(self, name, cost, card_type, effect):
      self.name = name
      self.cost = cost
      self.card_type = card_type  # Exemple : 'gem', 'spell'
      self.effect = effect

  def activate(self):
      """Active l'effet de la carte."""
      print(f"Activating {self.name}: {self.effect}")