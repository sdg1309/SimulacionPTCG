# sim.py

import random

from utilidades import shuffle, draw, has_basic


def mulligan(deck):

    while True:

        shuffle(deck)

        hand = draw(deck, 7)

        if has_basic(hand):
            return hand, deck

        deck += hand


def evaluate_setup(hand):

    basics = sum(1 for c in hand if c in [
        "Zorua",
        "Budew",
        "Buneary",
        "Darumaka",
        "Munkidori",
        "Zekrom",
        "Reshiram",
        "Yveltal",
        "Ogerpon"
    ])

    optimalBasics = sum(1 for c in hand if c in [
        "Zorua",
        "Budew",
        "Yveltal",
        "Ogerpon"
    ])

    search = sum(1 for c in hand if c in [
        "UltraBall",
        "Poffin",
        "Pad",
        "Cyrano"
    ])

    draw_support = sum(1 for c in hand if c in [
        "Lillie"
    ])

    disruption = sum(1 for c in hand if c in [
        "Judge",
        "Unfair"
    ])

    energy = sum(1 for c in hand if c in [
        "DarknessEnergy",
        "PrismEnergy"
    ])

    setup = (
        basics >= 1
        and
        optimalBasics >= 0
        and
        energy >= 0
        and
        (search >= 1 or draw_support >= 1)
    )

    optimalSetup = (
        optimalBasics >= 1
        and
        energy >= 1
        and
        (search >= 2 or draw_support >= 1)

    )

    pressure = setup and disruption >= 1

    return setup, pressure, optimalSetup


def rocket_disruption(hand):

    new_size = random.choice([3, 4])

    return random.sample(
        hand,
        min(len(hand), new_size)
    )


def simulate_vs_rocket(deck_list):

    deck = deck_list.copy()

    hand, deck = mulligan(deck)

    setup, pressure, optimalSetup = evaluate_setup(hand)

    hand += draw(deck, 1)

    hand = rocket_disruption(hand)

    hand += draw(deck, 1)

    recovery = evaluate_setup(hand)[0]

    return setup,optimalSetup, recovery, pressure


def run(deck, n=5000):

    setup_count = 0
    optimalSetup_count = 0
    recovery_count = 0
    pressure_count = 0

    for _ in range(n):

        s, o, r, p = simulate_vs_rocket(deck)

        setup_count += s
        optimalSetup_count += o
        recovery_count += (s and r)
        pressure_count += p

    return {
        "setup_rate": setup_count / n,
        "optimalsetup_rate": optimalSetup_count / n,
        "recovery_rate": recovery_count / n,
        "pressure_rate": pressure_count / n
    }