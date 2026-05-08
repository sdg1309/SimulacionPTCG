# main.py

from listas import (
    lopunny_deck_lillie,
    lopunny_deck_poffin,
    ogerpon_deck
)

from run import run, print_analysis

print_analysis("Lopunny Lillie", run(lopunny_deck_lillie))
print_analysis("Lopunny Poffin", run(lopunny_deck_poffin))
print_analysis("Ogerpon", run(ogerpon_deck))