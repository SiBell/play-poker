""" Make poker hands
"""

import random

VALUES = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
SUITS = 'Hearts Diamonds Clubs Spades'.split()


def make_new_deck():
    cards = []
    for suit in SUITS:
        for value in VALUES:
            card = value + ' of ' + suit
            cards.append(card)
    return cards


def test_new_deck():
    # We will test the `make_new_deck` function
    deck = make_new_deck()
    assert len(deck) == 52
    first_card = deck[0]
    assert first_card == '2 of Hearts'
    assert deck[-1] == 'Ace of Spades'
    assert len(set(deck)) == len(deck)
    assert deck[12] == 'Ace of Hearts'


def shuffled(deck):
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)
    return shuffled_deck


def test_shuffled():
    ordered_deck = make_new_deck()
    shuffled_deck = shuffled(ordered_deck)
    # Check they still have the same unique cards
    assert set(shuffled_deck) == set(ordered_deck)
    assert shuffled_deck != ordered_deck
    decks = []
    decks.append(make_new_deck())
    for i in range(1000):
        deck = make_new_deck()
        shuffled_deck = shuffled(deck)
        # Compare this deck to all previous ones.  Do any match?
        assert shuffled_deck not in decks
        decks.append(shuffled_deck)    


if __name__ == "__main__":
    print("Running tests")
    test_new_deck()
    print("Finished")
