# main.py

from listas import (
    lopunny_deck_lillie,
    lopunny_deck_poffin,
    ogerpon_deck
)

from sim import run


print("=== Lopunny lillie ===")
print(run(lopunny_deck_lillie))

print("\n=== Lopunny poffin ===")
print(run(lopunny_deck_poffin))

print("\n=== Ogerpon ===")
print(run(ogerpon_deck))