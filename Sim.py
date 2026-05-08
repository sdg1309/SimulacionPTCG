import random

# =========================
# UTILIDADES
# =========================

def build_deck(card_counts):
    deck = []
    for card, count in card_counts.items():
        deck += [card] * count
    return deck


def draw(deck, n):
    drawn = deck[:n]
    del deck[:n]
    return drawn


def shuffle(deck):
    random.shuffle(deck)


# =========================
# DEFINICIÓN DE MAZOS
# =========================

lopunny_deck = build_deck({
    # Pokémon
    "Zorua": 4, "Zoroark": 4, "Munkidori": 2,
    "Darumaka": 1, "Darmanitan": 1,
    "Buneary": 1, "Lopunny": 1,
    "Zekrom": 2, "Reshiram": 1,
    "Fezandipiti": 1, "Pecharunt": 1, "Yveltal": 1,

    # Trainers clave
    "Lillie": 4, "Cyrano": 2, "Boss": 2,
    "Judge": 1, "Pad": 3, "Poffin": 3,
    "UltraBall": 2,

    # Otros
    "Other": 33 - (4+2+2+1+3+3+2+1),

    # Energía
    "Energy": 7
})


ogerpon_deck = build_deck({
    "Zorua": 4, "Zoroark": 4, "Zekrom": 2,
    "Budew": 2, "Munkidori": 2,
    "Darumaka": 1, "Darmanitan": 1,
    "Reshiram": 1, "Ogerpon": 1,
    "Fezandipiti": 1, "Pecharunt": 1, "Yveltal": 1,

    "Lillie": 3, "Cyrano": 3, "Boss": 2,
    "Pad": 2, "Poffin": 3, "UltraBall": 2,

    "Other": 30 - (3+3+2+2+3+2),

    "Energy": 9
})


# =========================
# LÓGICA DE JUEGO
# =========================

def has_basic(hand):
    basics = ["Zorua", "Budew", "Buneary", "Darumaka"]
    return any(card in basics for card in hand)


def mulligan(deck):
    while True:
        shuffle(deck)
        hand = draw(deck, 7)
        if has_basic(hand):
            return hand, deck
        deck += hand  # devolver y reshuffle


def evaluate_setup(hand):
    basics = sum(1 for c in hand if c in ["Zorua", "Budew", "Buneary"])
    search = sum(1 for c in hand if c in ["UltraBall", "Poffin"])
    draw_support = sum(1 for c in hand if c in ["Lillie", "Cyrano"])

    return (basics >= 1) and (search >= 1 or draw_support >= 1)


def rocket_disruption(hand):
    # Simula Proton/Judge/etc
    new_size = random.choice([3, 4])
    return random.sample(hand, min(len(hand), new_size))


def simulate_vs_rocket(deck_list):
    deck = deck_list.copy()

    # Mano inicial
    hand, deck = mulligan(deck)

    setup = evaluate_setup(hand)

    # Turno 1 robo
    hand += draw(deck, 1)

    # Rocket rompe mano
    hand = rocket_disruption(hand)

    # Turno 2 robo
    hand += draw(deck, 1)

    recovery = evaluate_setup(hand)

    return setup, recovery


# =========================
# SIMULACIÓN
# =========================

def run(deck, n=5000):
    setup_count = 0
    recovery_count = 0

    for _ in range(n):
        s, r = simulate_vs_rocket(deck)
        setup_count += s
        recovery_count += (s and r)

    return {
        "setup_rate": setup_count / n,
        "recovery_rate": recovery_count / n
    }


# =========================
# RESULTADOS
# =========================

lopunny_results = run(lopunny_deck)
ogerpon_results = run(ogerpon_deck)

print("Lopunny:", lopunny_results)
print("Ogerpon:", ogerpon_results)