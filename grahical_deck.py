import random
from tkinter import Tk, Canvas, PhotoImage

class Card:
  """Represents a single playing card."""
  suits = ["spades", "hearts", "diamonds", "clubs"]
  ranks = ["ace_of", "2_of", "3_of", "4_of", "5_of", "6_of", "7_of", "8_of", "9_of", "10_of", "jack_of", "queen_of", "king_of"]

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def get_image_path(self):
    """Returns the file path for the card image based on rank and suit."""
    return f"cards/{self.rank}_{self.suit}.png"

class Deck:
  """Represents a deck of cards."""
  def __init__(self, num_decks=1, jokers=2):
    self.cards = []
    for _ in range(num_decks):
      for suit in Card.suits:
        for rank in Card.ranks:
          self.cards.append(Card(rank, suit))
      for _ in range(jokers):
        self.cards.append(Card("joker", ""))
    random.shuffle(self.cards)

  def draw_card(self):
    """Removes and returns the top card from the deck."""
    if self.cards:
      return self.cards.pop()
    return None

class CardGUI(Tk):
  """Represents the GUI application for displaying cards."""
  def __init__(self):
    super().__init__()
    self.title("Shuffled Deck")
    self.geometry("800x600")
    self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
    self.canvas.pack(fill="both", expand=True)
    self.deck = Deck()
    self.card_images = {}  # Dictionary to store loaded card images
    self.display_cards()

  def load_card_image(self, card):
    """Loads the image for a specific card and stores it in the dictionary."""
    image_path = card.get_image_path()
    if image_path not in self.card_images:
      self.card_images[image_path] = PhotoImage(file=image_path)
    return self.card_images[image_path]

  def display_cards(self, num_cards=5):
    """Displays a specified number of cards on the canvas."""
    self.canvas.delete("all")  # Clear any existing cards before redrawing
    card_width = 100
    card_height = 150 
    x_offset = 50
    y_offset = 50
    for i in range(num_cards):
      card = self.deck.draw_card()  # Draw a card from the deck
      if card:
        card_image = self.load_card_image(card)
        self.canvas.create_image(x_offset + i * card_width, y_offset, image=card_image, anchor="nw")

# Run the GUI application
app = CardGUI()
app.mainloop()
