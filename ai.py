import random

def tah(pole, pozice, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici"

    return pole[:pozice] + symbol + pole[pozice + 1:]


def tah_pocitace(pole, symbol):
    while True:
        cislo = random.randrange(len(pole))
        if pole[cislo] == '-':
            return tah(pole, cislo, symbol)
