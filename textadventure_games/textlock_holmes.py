# Aufgabe 3-2 Text Adventure Game


# Imports
import numpy as np


# --- Haupthandlung
def maingame(s):
    """Startet das Hauptspiel mit den ersten Optionen."""
    prompt0 = 'The Game is on!'
    prompt1 = (
        'Du befindest dich im London des 21. Jahrhunderts. '
        'Du stehst auf einer dunklen, menschenleeren Straße. '
        'Leichter Nieselregen setzt sich auf deinem Mantel ab '
        'und du spürst eine Windbrise durch dein Haar streichen.'
        'Du siehst dich um. Alles um dich herum ist dunkel. '
        'Alles? Alles, bis auf ein einzelnes Fenster im ersten Stock'
        'Es sieht aus, als würde jemand mit einer Taschenlampe '
        'durch das Zimmer laufen'
        'eines etwas heruntergekommenen Backsteinhauses zu deiner Rechten.'
        'Du näherst dich, sorgsam darauf bedacht, deine Schritte nicht zu '
        'laut werden zu lassen.Beim Vorgarten angekommen bemerkst du, '
        'dass die Eingangstüre des Hauses einen Spalt breit offen steht.'
    )
    prompt2 = '**Willst du hineingehen?** [1/2/3]'
    prompt3 = (
        '1 = Nein. \n'
        '2 = Mh, ich rufe lieber erstmal Inspector Lestrade an.\n'
        '3 = Ja, sofort! \n'
        )

    print(prompt0)
    print(prompt1)
    print(prompt2)
    print(prompt3)

    ans2 = input('')

    if ans2 == 1:
        return gesicht_am_fenster(s)
    elif ans2 == 2:
        return call_lestrade(s)
    elif ans2 == 3:
        return inside_house(s)
    else:
        prompt4 = 'Bitte entscheide dich für 1., 2. oder 3.'
        print(prompt4)
        return maingame(s)


def game_exit(s):
    """Beendet das Spiel bei Nein Antwort"""
    print(
        'Sherlock Holmes schüttelt enttäuscht den Kopf ...'
        'So wird kein Meisterdedektiv aus dir ( ͡ಠ ʖ̯ ͡ಠ)'
    )
    return s
# ---


# Weitere Funktionen

def dumb(s):
    """Antwort, wenn der Spieler die Anweisung nicht versteht."""
    print("Deine Taschenlaterne scheint heute nicht an zu sein... _/(.-.)")
    return s


def newstart(s):
    """Neustart des Spiels"""
    prompt4 = ('John Watson hat dich leider nicht verstanden'
               '... _(ಠ_ಠ)_/ Aber versuche es gern nochmal!')
    print(prompt4)
    return maingame(s)


def call_lestrade(s):
    """Ruft Inspektor Lestrade an. Dialog mit diesem."""
    prompt0 = (
        'Du entfernst dich einige Schritte vom Haus '
        'nd zückst dein Smartphone. Du suchst in deinen Kontakten '
        'nach der Nummer von Inspektor Lestrade und drückst auf anrufen. '

    )
    prompt1 = 'Eine etwas unwirsche Stimme meldet sich.'
    prompt2 = (
        'Du warstest eine Minute, bis der Anrufbeantworter von Lestrade'
        'sich meldet: '
        ' "Hier Inspektor Lestrade von Scottland Yard. Ich bin gerade nicht '
        'erreichbar, aber hinterlassen Sie mir nach dem Ton eine Nachricht."'
    )

    print(prompt0)
    random_bit = np.random.randint(0, 2, dtype=bool)

    if random_bit == 0:
        print(prompt1)
        prompt4 = ('“Inspektor Lestrade von Scottland Yard. Wer spricht da?”'
                   '[Gib hier deinen Namen ein] \n')
        name = input(prompt4)
        print("Guten Abend,", name, "was gibt es Neues?")
        answer1 = (' "Inspektor, ich stehe in einer Seitengasse nahe '
                   'der Brixton Road vor einem Haus in dem '
                   'vermutlich eingebrochen wurde. '
                   'Die Türe ist offenbar aufgebrochen worden und '
                   'im ersten Stock sehe ich das Licht einer Taschenlampe." ')
        print(answer1)
        prompt5 = (' "Ah ja. Bleiben Sie, wo sie sind. UIch komme vorbei'
                   'um mir das anzusehen."')
        print(prompt5)
    elif random_bit == 1:
        print(prompt2)

    return s


def inside_house(s):
    """Platzhalter für das Betreten des Hauses."""
    print("[Platzhalter]")
    return s


# Spielsart
def enter_game(s):
    """Begrüßt den Spieler und fragt, ob er das Spiel starten möchte."""
    start_prompt = 'Willkommen zum Sherlock Holmes Text Adventure Game.'
    print(start_prompt)
    ans = input('**Willst du das Spiel starten?** [ja/nein] \n')

    if ans.lower().strip() == 'ja':
        return maingame(s)
    elif ans.lower().strip() == 'nein':
        return game_exit(s)
    else:
        return newstart(s)


def lestrade_arrives(s):
    prompt0 = 'dummy'
    print(prompt0)
    return s


def stolpern(s):
    """Handlungsverlauf beim Stolpern."""
    prompt0 = (
                'Du bewegst dich einige Schritte zurück, musst dann '
                'aber straucheln.'
                '"Mist, bin ich etwa auf einer Nacktschnecke ausgerutscht?" '
                'geht es dir durch den Kopf '
                'bevor du hart auf dem Boden aufschlägst.'
                'Du hörst im Hintergrund ein Auto vor der '
                'Einfahrt des Hauses parken.'
                'Dann verlierst du das Bewusstsein...'
    )
    ans0 = input(
                '**Was willst du nun tun?** [1/2/3]'
                '1. Bewusstlos warten \n'
                '2. Das Spiel beenden\n'
                '3. Das Spiel von vonre beginnen\n'
    )
    print(prompt0)
    print(ans0)

    if ans0 == 1:
        return lestrade_arrives(s)
    elif ans0 == 2:
        return game_exit(s)
    elif ans0 == 3:
        return enter_game(s)
    else:
        prompt1 = 'Ungültige Eingabe. Entscheide dich für 1., 2. oder 3.'
        print(prompt1)
        return stolpern(s)


def beobachten(s):
    prompt0 = 'dummy'
    print(prompt0)
    return s


def gesicht_am_fenster(s):
    prompt0 = (
        'Du traust dich nicht hineinzugehen, aber starrst wie gebannt'
        'auf das Fenster, in dem sich das Taschenlampenlicht bewergt.'
        'Auf einmal siehst du ein bleiches Gesicht am Fenster. '
        'Die Person hat noch nicht nach draußen gesehen und '
        'dich noch nicht bemerkt... \n')
    print(prompt0)
    ans1 = input(
        '**Was wirst du tun?** [1/2/3]'
        '1. Wegrennen\n'
        '2. Dich hinter eine Hecke ducken und weiter beobachten\n'
        '3. Ins Haus hineingehen, denn irgendwie hast du doch Mut bekommen.')
    print(ans1)

    if ans1 == 1:
        return stolpern(s)
    elif ans1 == 2:
        return beobachten(s)
    else:
        return inside_house(s)


# Spielausfuehrung
enter_game('')
