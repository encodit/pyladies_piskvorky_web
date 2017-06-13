from flask import Flask, render_template, redirect, url_for

# Doplň vlastní Piškvorky!
from ai import tah_pocitace
from util import tah

# Vytvoření aplikace. To __name__ i jméno proměnné "app" jsou důležité.
app = Flask(__name__)


# Hlavní stránka. Je na ní odkaz na začátek hry.
@app.route('/')
def index():
    return render_template('index.html')


# `view` pro zobrazení pole.
# např. http://piskvorky.example.cz/--xxo-------
# zobrazí pole `--xxo-------`
@app.route('/piskvorky/<pole>')
def piskvorky(pole):
    return render_template('piskvorky.html', pole=pole)


# `view` pro tah
# např. adresa http://piskvorky.example.cz/--xxo-------/10
# znamená že z pole `--xxo-------` hráč hraje na 10. pozici
@app.route('/piskvorky/<pole>/<int:pozice>')
def piskvorky_tah(pole, pozice):

    # Hraje hráč
    pole = tah(pole, pozice, 'x')

    if 'xxx' in pole:
        # Hrač vyhrál!

        # Přesměrování na hlavní stránku. Lepší by byla stránka
        # s gratulací
        return redirect(url_for('index'))

    # Hraje počítač
    pole = tah_pocitace(pole, 'o')

    if 'ooo' in pole:
        # Poičítač vyhrál :(

        # Přesměrování na hlavní stránku. Lepší by byla stránka
        # s nějakou utěšující zprávou
        return redirect(url_for('index'))

    # Zatím nevyhrál nikdo. Přesměrování na stránku s hrou.
    return redirect(url_for('piskvorky', pole=pole))
