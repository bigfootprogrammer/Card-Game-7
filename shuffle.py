# Here's the Python 3 code to shuffle 3 full decks of 54 cards, having two jokers in each deck: 

#python
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


'''

**Explanation:**

1. **`create_deck` function:**
   - Defines four suits and card ranks (1-10, Jack, Queen, King, Ace).
   - Creates an empty list `deck`.
   - Loops through suits and ranks, adding a tuple of `(rank, suit)` to the deck.
   - Appends two "Joker" strings to the deck.

2. **`shuffle_decks` function:**
   - Takes the number of decks (`num_decks`) as input.
   - Creates an empty list `all_cards`.
   - Loops through `num_decks`, calling `create_deck` to generate cards for each deck and appending them to `all_cards`.
   - Uses `random.shuffle` to shuffle the combined cards in `all_cards`.
   - Returns the shuffled deck.

3. **Main program:**
   - Calls `shuffle_decks(3)` to create and shuffle 3 decks.
   - Stores the shuffled deck in `shuffled_deck`.
   - Uncomment the loop to print the first 5 cards for demonstration (optional).

This code defines functions to create a single deck with jokers and then shuffles cards from multiple decks. You can modify it to suit your needs, such as printing the entire deck or dealing specific numbers of cards.

'''