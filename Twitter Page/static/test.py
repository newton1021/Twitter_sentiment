
import numpy

import random

deck = list(range(0,52))
random.shuffle(deck)

Suits = {0: "Club",
         1: "Spade",
         2: "Diamonds",
         3: "Heart"}

Ranks = {1: "A",
         2: "2",
         3: "3",
         4: "4",
         5: "5",
         6: "6",
         7: "7",
         8: "8",
         9: "9",
         10: "10",
         11: "J",
         12: "Q",
         13: "K"}


for card in deck:
    suit = int(card / 13)
    rank = card % 13

    print(f"{Ranks[rank + 1]:2} {Suits[suit]}")
