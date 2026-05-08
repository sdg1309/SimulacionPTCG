# sim.py

import random

from utilidades import shuffle, draw, mulligan


def evaluate_setup(hand, going_first):

    basics = sum(1 for c in hand if c in [
        "Zorua",
        "Budew",
        "Buneary",
        "Darumaka",
        "Munkidori",
        "Zekrom",
        "Reshiram",
        "Yveltal",
        "Ogerpon",
        "Fezandipiti",
        "Pecharunt"
    ])

    optimalBasics = sum(1 for c in hand if c in [
        "Zorua",
        "Budew",
        "Yveltal",
        "Ogerpon"
    ])

    searchItem = sum(1 for c in hand if c in [
        "UltraBall",
        "Poffin",
        "Pad"
    ])

    searchSupport = sum(1 for c in hand if c in [
        "Cyrano",
        "Ciphermaniac"
    ])

    drawSupport = sum(1 for c in hand if c in [
        "Lillie"
    ])

    disruption = sum(1 for c in hand if c in [
        "Judge",
        "Unfair",
        "Boss"
    ])

    energy = sum(1 for c in hand if c in [
        "DarknessEnergy",
        "PrismEnergy"
    ])

    if going_first == True:

        setup = (   
            basics >= 1
            and
            energy >= 1
            and
            searchItem >= 1
        )

        optimalSetup = (
            optimalBasics >= 1
            and
            energy >= 1
            and
            searchItem >= 2 
            and
            drawSupport >= 1

        )

        pressure = setup and disruption >= 1

        return setup, pressure, optimalSetup
    

    else:

        setup = (
            basics >= 1
            and
            energy >= 1
            and
            (searchItem >= 1 or drawSupport >= 1)
        )

        optimalSetup = (
            optimalBasics >= 1
            and
            energy >= 1
            and
            searchItem >= 2 
            and
            (drawSupport >= 1 or searchSupport >=1)

        )

        pressure = setup and disruption >= 1

        return setup, pressure, optimalSetup


def apply_disruption(hand, min_cards=3, max_cards=4):

    new_size = random.randint(min_cards, max_cards)

    return random.sample(
        hand,
        min(len(hand), new_size)
    )

def simulate_game(deck_list, disruption=False, disruption_range=(3, 4)):

    deck = deck_list.copy()

    going_first = random.choice([True, False])

    hand, deck = mulligan(deck)

    setup_if_first, pressure_if_first, optimalSetup_if_first = evaluate_setup(hand, True)
    setup_if_second, pressure_if_second, optimalSetup_if_second = evaluate_setup(hand, False)

    setup, pressure, optimalSetup = evaluate_setup(hand, going_first)

    hand += draw(deck, 1)

    if disruption:

        hand = apply_disruption(
            hand,
            disruption_range[0],
            disruption_range[1]
        )

    hand += draw(deck, 1)

    recovery_if_first = evaluate_setup(hand, True)[0]
    recovery_if_second = evaluate_setup(hand, False)[0]
    recovery = evaluate_setup(hand, going_first)[0]  # Actual recovery based on going_first

    return {
        "setup": setup,
        "optimal_setup": optimalSetup,
        "recovery": recovery,
        "pressure": pressure,
        "going_first": going_first,
        "setup_if_first": setup_if_first,
        "pressure_if_first": pressure_if_first,
        "optimal_setup_if_first": optimalSetup_if_first,
        "recovery_if_first": recovery_if_first,
        "setup_if_second": setup_if_second,
        "pressure_if_second": pressure_if_second,
        "optimal_setup_if_second": optimalSetup_if_second,
        "recovery_if_second": recovery_if_second,
    }