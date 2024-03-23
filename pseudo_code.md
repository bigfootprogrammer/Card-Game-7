Using python 3  shuffle 3 full decks of 54 cards, having two jokers in each deck.

import random

def create_deck():
  """Creates a single deck of cards with two jokers."""
  suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
  ranks = [str(x) for x in range(1, 11)] + ["Jack", "Queen", "King", "Ace"]
  deck = []
  for suit in suits:
    for rank in ranks:
      deck.append((rank, suit))
  deck.extend(["Joker", "Joker"])  # Add two jokers
  return deck

def shuffle_decks(num_decks):
  """Shuffles the combined cards from multiple decks."""
  all_cards = []
  for _ in range(num_decks):
    all_cards.extend(create_deck())
  random.shuffle(all_cards)
  return all_cards

# Create and shuffle 3 decks of cards
shuffled_deck = shuffle_decks(3)

# Print the first 5 cards (optional)
for card in shuffled_deck[:5]:
  print(card[0], "of", card[1])

 