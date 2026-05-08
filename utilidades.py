import random


def build_deck(card_counts):
    deck = []

    for card, count in card_counts.items():
        deck += [card] * count

    return deck


def shuffle(deck):
    random.shuffle(deck)


def draw(deck, n):
    drawn = deck[:n]
    del deck[:n]
    return drawn


def has_basic(hand):

    basics = [
        "Zorua",
        "Budew",
        "Buneary",
        "Darumaka",
        "Munkidori",
        "Zekrom",
        "Reshiram",
        "Yveltal",
        "Ogerpon"
    ]

    return any(card in basics for card in hand)

def mulligan(deck):

    while True:

        shuffle(deck)

        hand = draw(deck, 7)

        if has_basic(hand):
            return hand, deck

        deck += hand