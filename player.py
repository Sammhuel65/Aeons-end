class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.deck = ["Crystal", "Spark"]  # Exemple de cartes initiales
        self.hand = []
        self.discard_pile = []

    def draw(self, num_cards=5):
        """Pioche des cartes depuis le deck."""
        for _ in range(num_cards):
            if not self.deck:
                self.deck = self.discard_pile
                self.discard_pile = []
            if self.deck:
                self.hand.append(self.deck.pop())
        print(f"{self.name} draws {len(self.hand)} cards.")