# Aufgabe 3-2 Text Adventure Game


# --- Imports
import numpy as np
from textwrap import dedent


# --- Variables and Helpers

name: str = None


def options_message_3(s: str) -> str:
    prompt0: str = '---Bitte entscheide dich für 1., 2. oder 3.---'
    print(prompt0)
    return s


def options_message_2(s: str) -> str:
    prompt0: str = '---Bitte entscheide dich für 1. oder 2.---'
    print(prompt0)
    return s


def game_exit(s: str) -> str:
    print(dedent(f"""
    Sherlock Holmes schüttelt enttäuscht den Kopf und geht… ( ͡ಠ ʖ̯ ͡ಠ)
    """))


def dumb(s: str) -> str:
    print(dedent(f"""
    Das war keine mögliche Antwort… _/(.-.) Versuche es gerne nochmal.
    """))
    return maingame(s)


def newstart(s: str) -> str:
    print(dedent(f"""
    John Watson hat dich leider nicht verstanden… _(ಠ_ಠ)_/
    Aber versuche es gern nochmal!
    """))
    return enter_game(s)


def final_game_stage(s: str) -> str:
    prompt0 = dedent(f"""
    Du fährst also in die Baker Street zu Sherlock Holmes. 
    Jetzt kann das Abenteuer richtig beginnen! 
    Aber das erfahren wir erst im nächsten Teil des 
    **Sherlock Holmes Text Adventure**... 
    Danke fürs Spielen! :) 
    """)
    print(prompt0)
    return s


# --- Game Logic

def maingame(s: str) -> str:
    print(dedent(f"""
    --- The Game is on! ---
    Du befindest dich im London des 21. Jahrhunderts.
    Du stehst auf einer dunklen, menschenleeren Straße.
    Leichter Nieselregen setzt sich auf deinem Mantel ab und du spürst
    eine Windbrise durch dein Haar streichen.
    Du siehst dich um. Alles um dich herum ist dunkel. Alles? Alles,
    bis auf ein einzelnes Fenster im ersten Stock.
    Es sieht aus, als würde jemand mit einer Taschenlampe durch das Zimmer
    laufen, eines etwas heruntergekommenen Backsteinhauses zu deiner Rechten.
    Du näherst dich, sorgsam darauf bedacht, deine Schritte nicht zu laut
    werden zu lassen. Beim Vorgarten angekommen bemerkst du, dass die
    Eingangstüre des Hauses einen Spalt breit offen steht.
    """))

    print(dedent(f"""
    **Willst du hineingehen?** [1/2/3]
    1. Nein.
    2. Mh, ich rufe lieber erstmal Inspector Lestrade an…
    3. Ja, sofort!
    """))

    try:
        ans0 = int(input())
    except:
        options_message_3(s)
        return maingame(s)

    if ans0 == 1:
        return gesicht_am_fenster(s)
    elif ans0 == 2:
        return call_lestrade(s)
    elif ans0 == 3:
        return inside_house(s)
    else:
        options_message_3(s)
        return maingame(s)


def maingame_version2(s: str) -> str:
    print(dedent(f"""
    Mh, der Inspektor ist nicht ans Telefon gegangen.
    Vielleicht geht er aber dran, wenn ich nochmal anrufe?
    **Was willst du jetzt versuchen?** [1/2/3]
    1. Ich rufe nochmal Inspektor Lestrade an.
    2. Ich gehe doch ins Haus.
    """))

    try:
        ans2 = int(input())
    except:
        options_message_2(s)
        return maingame_version2(s)

    if ans2 == 1:
        return call_lestrade(s)
    elif ans2 == 2:
        return inside_house(s)
    else:
        options_message_2(s)
        return maingame_version2(s)


def gesicht_am_fenster_version2(s: str) -> str:
    print(dedent(f"""
    Du wartest also auf den Inspektor und schaust dir das Fenster genauer an,
    in dem sich das Taschenlampenlicht bewegt.
    Auf einmal siehst du ein bleiches Gesicht am Fenster. Die Person hat noch
    nicht nach draußen gesehen und dich noch nicht bemerkt…
    """))

    print(dedent(f"""
    **Was wirst du nun tun?** [1/2/3]
    1. Wegrennen
    2. Dich hinter eine Hecke ducken und weiter beobachten
    3. Ins Haus hineingehen, denn irgendwie hast du jetzt doch Mut bekommen.
    """))

    try:
        ans1 = int(input())
    except:
        options_message_3(s)
        return gesicht_am_fenster_version2(s)

    if ans1 == 1:
        return stolpern(s)
    elif ans1 == 2:
        return beobachten(s)
    elif ans1 == 3:
        return inside_house(s)
    else:
        options_message_3(s)
        return gesicht_am_fenster_version2(s)


def called_lestrange(s: str) -> str:
    print(dedent(f"""
    Du hast in deinem Adressbuch versehentlich Lestrange statt Lestrade
    gedrückt und rufst daher jetzt Bellatrix Lestrange an.
    Als diese rangeht hörst du nur noch "Avada Kedavra" hinter dir –
    und schwups, du bist tot.
    Game over!
    """))

    print(dedent(f"""
    **Möchtest du das Spiel neu starten? (1/2)**
    1. Ja!
    2. Nee..du spinnst doch...
    """))

    try:
        ans1 = int(input())
    except:
        options_message_2(s)
        return called_lestrange(s)

    if ans1 == 1:
        return maingame(s)
    elif ans1 == 2:
        return s
    else:
        options_message_2(s)
        return called_lestrange(s)


def call_lestrade(s: str) -> str:
    global name
    print(dedent(f"""
    Du entfernst dich einige Schritte vom Haus und zückst dein Smartphone.
    Du suchst in deinen Kontakten nach der Nummer von Inspektor Lestrade
    und drückst auf anrufen.
    """))

    random_int = int(np.random.randint(0, 3))

    if random_int == 0:
        print("Eine etwas unwirsche Stimme meldet sich.")
        name = input(dedent(f"""
        Inspektor Lestrade von Scotland Yard. Wer spricht da?
        [Gib hier deinen Namen ein]:
        """))

        print(dedent(f"""
        Lestrade: Guten Abend {name}, was gibt es Neues?
        Du: Inspektor, ich stehe in einer Seitengasse nahe der Brixton Road
        vor einem Haus, in dem vermutlich eingebrochen wurde.
        Die Türe ist offenbar aufgebrochen worden und im ersten Stock sehe ich
        das Licht einer Taschenlampe.
        """))

        print(dedent(f"""
        Lestrade: Ah ja. Bleiben Sie, wo Sie sind.
        Ich komme vorbei, um mir das anzusehen.
        """))
        return gesicht_am_fenster_version2(s)

    elif random_int == 1:
        print(dedent(f"""
        Du wartest eine Minute, bis der Anrufbeantworter von Lestrade sich
        meldet: "Hier Inspektor Lestrade von Scotland Yard.
        Ich bin gerade nicht erreichbar, aber hinterlassen Sie mir nach dem
        Ton eine Nachricht."
        """))
        return maingame_version2(s)

    elif random_int == 2:
        return called_lestrange(s)

    else:
        options_message_2(s)
        return call_lestrade(s)


def inside_room(s: str) -> str:
    prompt0 = dedent(f"""
    Du öffnest die Türe und siehst zu deiner großen Überraschung
    Sherlock Holmes persönlich im Zimmer herumlaufen und offenbar
    etwas suchen. Er dreht sich um mit den Worten:
    Sherlock: {name}, Dr. Watson ist spurlos verschwunden und ich denke,
    es gibt Hinweise, wo er sein könnte – irgendwo hier in diesem Zimmer.

    Du: Mr. Holmes, woher wissen Sie meinen Namen?
    Sherlock: Nun, woher wissen Sie meinen? Ihren habe ich vorhin Ihrem
    Telefonat draußen mit Inspektor Lestrade entnehmen können.
    Habe da so meine Methoden...

    Du: Niemand sonst hat so einen merkwürdigen Hut auf!
    Sherlock: Richtig deduziert, aber das ist kein merkwürdiger Hut,
    das ist ein Deerstalker. Aber genug davon! Kommen Sie nun mit,
    um Dr. Watson zu finden, oder nicht?
    """)
    print(prompt0)
    prompt1 = dedent(f"""
    1. Ja, natürlich!
    2. Nein, Sie schaffen das schon alleine...
    """)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        return final_game_stage(s)
    elif ans0 == 2:
        return game_exit(s)
    else:
        options_message_2(s)
        return inside_room(s)


def sherlock_coming(s: str) -> str:
    prompt0 = dedent(f"""
    Du wartest verborgen hinter der Statue ab und siehst zu deiner großen
    Überraschung Sherlock Holmes aus dem Zimmer laufen, in der linken Hand
    hat er einen zerknüllten Zettel und in der rechten eine Taschenlampe.
    Er dreht sich um mit den Worten:
    Sherlock: {name}, Dr. Watson ist spurlos verschwunden und ich denke,
    es gibt Hinweise, wo er sein könnte – irgendwo hier in diesem Zimmer.

    Du: Mr. Holmes, woher wissen Sie meinen Namen?
    Sherlock: Nun, woher wissen Sie meinen? Ihren habe ich vorhin Ihrem
    Telefonat draußen mit Inspektor Lestrade entnehmen können.
    Habe da so meine Methoden...

    Du: Niemand sonst hat so einen merkwürdigen Hut auf!
    Sherlock: Richtig deduziert, aber das ist kein merkwürdiger Hut,
    das ist ein Deerstalker. Aber genug davon! Kommen Sie nun mit,
    um Dr. Watson zu finden, oder nicht?
    """)
    print(prompt0)
    prompt1 = dedent(f"""
    1. Ja, natürlich!
    2. Nein, Sie schaffen das schon alleine...
    """)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        return final_game_stage(s)
    elif ans0 == 2:
        return game_exit(s)
    else:
        options_message_2(s)
        return inside_room(s)


def first_floor(s: str) -> str:
    prompt0 = dedent(f"""
    Du gehst also die Treppe nach oben und hörst, 
    als du angekommen bist, Schritte in dem Zimmer 
    zu deiner Linken.
    """)
    prompt1 = dedent(f"""
    **Was willst du tun?**
    1. Ins Zimmer hineingehen
    2. Mich hinter einer Statue links vom Zimmer verstecken und warten
    """)
    print(prompt0)
    ans0 = int(input(prompt1))

    if ans0 == 1:
        return inside_room(s)
    elif ans0 == 2:
        return sherlock_coming(s)
    else:
        options_message_2(s)
        return first_floor(s)


def right_door(s: str) -> str:
    prompt0 = dedent(f"""
    Du gehst durch die rechte Türe und gelangst in eine Küche. Von oben hörst du
    Schritte die Treppe herunterkommen.
    Zu deiner großen Überraschung kommt Sherlock Holmes persönlich in die Küche,
    in der linken Hand hat er einen zerknüllten Zettel
    und in der rechten eine Taschenlampe. Er dreht sich um mit den Worten:
    Sherlock: {name}, Dr. Watson ist spurlos verschwunden und ich denke,
    es gibt Hinweise, wo er sein könnte – irgendwo hier in diesem Zimmer.

    Du: Mr. Holmes, woher wissen Sie meinen Namen?
    Sherlock: Nun, woher wissen Sie meinen? Ihren habe ich vorhin Ihrem
    Telefonat draußen mit Inspektor Lestrade entnehmen können.
    Habe da so meine Methoden...

    Du: Niemand sonst hat so einen merkwürdigen Hut auf!
    Sherlock: Richtig deduziert, aber das ist kein merkwürdiger Hut,
    das ist ein Deerstalker. Aber genug davon! Kommen Sie nun mit,
    um Dr. Watson zu finden, oder nicht?
    """)
    print(prompt0)
    prompt1 = dedent(f"""
    1. Ja, natürlich!
    2. Nein, Sie schaffen das schon alleine...
    """)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        prompt2 = dedent(f"""
        Du fährst also mit Sherlock in die Baker Street. 
        Jetzt kann das Abenteuer richtig beginnen! 
        Aber das erfahren wir erst im nächsten Teil des 
        **Sherlock Holmes Text Adventure**...
        Danke fürs Spielen! :) 
        """)
        print(prompt2)
    elif ans0 == 2:
        return game_exit(s)
    else:
        options_message_2(s)
        return right_door(s)


def inside_house(s: str) -> str:
    prompt0 = dedent(f"""
    Du stehst vor der Eingangstür und schaust durch den Spalt
    in den verlassenen Flur, bevor du die Tür schließlich 
    öffnest und hinein gehst. Du siehst direkt vor dir eine 
    Treppe, welche wohl in den ersten Stock führt.
    Rechts neben dir siehst du eine weitere Türe.
    """)
    print(prompt0)
    ans0: int = int(input(dedent(f"""
    **Wo möchtest du jetzt hingehen?** [1/2] 
    1. Über die Treppe nach oben
    2. Nach rechts durch die Türe.
    """)))

    if ans0 == 1:
        return first_floor(s)
    elif ans0 == 2:
        return right_door(s)
    else:
        options_message_2(s)
        return inside_house(s)


def enter_game(s: str) -> str:
    global name
    """Begrüßt den Spieler und fragt, ob er das Spiel starten möchte."""
    start_prompt = dedent(f"""
    **Willkommen zum Sherlock Holmes Text Adventure Game.**
    """)
    print(start_prompt)
    ans_name_prompt = str(input(dedent(f"""
    Wie ist dein Name? [hier eingeben]\n
    """)))
    name = ans_name_prompt
    ans: str = input(dedent(f"""
    **Willst du das Spiel starten?** [ja/nein] 
    """))

    if ans.lower().strip() == 'ja':
        return maingame(s)
    elif ans.lower().strip() == 'nein':
        return game_exit(s)
    else:
        newstart(s)
        return enter_game(s)


def papier_allein_lesen(s: str) -> str:
    prompt0 = dedent(f"""
    Auf dem Papier steht
    "Kommen Sie sofort in die Bakerstreet 221b. 
    Dr. Watson ist spurlos verschwunden und Sie sind von Nutzen 
    in der Angelegenheit.
    S.H."
    """)
    prompt1 = dedent(f"""
    **Was willst du machen?** [1/2]
    1. Die Nachricht doch noch Inspektor Lestrade zeigen
    2. Inspektor Lestrade sagen, dass du dich nicht wohl fühlst und gehen musst – in Wahrheit gehst du aber in die Baker Street
    """)
    print(prompt0)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        return papier_zeigen(s)
    elif ans0 == 2:
        return final_game_stage(s)
    else:
        options_message_2(s)
        return papier_allein_lesen(s)


def papier_zeigen(s: str) -> str:
    prompt0 = dedent(f"""
    Du zeigst Inspektor Lestrade das Papier.
    Lestrade: Nun, {name}, wir sollten schnellsten 
    in die Baker Street gehen und Holmes behilflich sein. Es ist schließlich selten, 
    dass er überhaupt mal die Hilfe von Leuten außer Watson benötigt.
    Kommen Sie mit? [1/2]
    """)
    print(prompt0)
    prompt1 = dedent(f"""
    1. Ja, klar!
    2. Nein...
    """)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        prompt2 = dedent(f"""
        Du fährst daher mit Lestrade in die Baker Street. 
        Jetzt kann das Abenteuer richtig beginnen! 
        Aber das erfahren wir erst im nächsten Teil des 
        **Sherlock Holmes Text Adventure**... 
        Danke fürs Spielen! :) 
        """)
        print(prompt2)
        return s
    elif ans0 == 2:
        prompt3 = dedent(f"""
        Lestrade: Schade, aber kann ich Sie verstehen. 
        Es könnte ja schließlich auch gefährlich werden!
        Und hiermit endet das **Sherlock Holmes Text Adventure**
        Danke fürs Spielen! :) 
        """)
        print(prompt3)
        return s
    else:
        options_message_2(s)
        return papier_allein_lesen(s)


def lestrade_arrives(s: str) -> str:
    prompt0 = dedent(f"""
    Du fühlst, wie dich jemand schüttelt, während du langsam 
    wieder zu Bewusstsein kommst. 
    Wie viel Zeit ist wohl vergangen?
    Lestrade: {name}, was ist passiert?
    Du setzt dich langsam auf und stützt dich dabei auf dem Boden ab. Dabei bemerkst du, 
    dass unter deiner Hand ein zerknülltes Blatt Papier liegt.
    """)
    print(prompt0)
    ans0: int = int(input(dedent(f"""
    **Was möchtest du tun?** [1/2]
    1. Das Papier Inspektor Lestrade zeigen.
    2. Das Papier unauffällig in der Hand behalten und dem Inspektor nicht zeigen
    """)))

    if ans0 == 1:
        return papier_zeigen(s)
    elif ans0 == 2:
        return papier_allein_lesen(s)
    else:
        options_message_2(s)
        return lestrade_arrives(s)


def stolpern(s: str) -> str:
    prompt0 = dedent(f"""
    Du bewegst dich einige Schritte zurück, musst dann 
    aber straucheln. 
    Mist, bin ich etwa auf einer Nacktschnecke ausgerutscht? 
    geht es dir durch den Kopf, bevor du hart auf dem Boden aufschlägst. 
    Du hörst im Hintergrund ein Auto vor der Einfahrt des Hauses parken. 
    Dann verlierst du das Bewusstsein...
    """)
    print(prompt0)
    ans0: int = int(input(dedent(f"""
    **Was willst du nun tun?** [1/2/3]
    1. Bewusstlos werden und warten... 
    2. Das Spiel beenden
    3. Das Spiel von vorne beginnen
    """)))

    if ans0 == 1:
        return lestrade_arrives(s)
    elif ans0 == 2:
        return game_exit(s)
    elif ans0 == 3:
        return enter_game(s)
    else:
        options_message_3(s)
        return stolpern(s)


def beobachten(s: str) -> str:
    prompt0 = dedent(f"""
    Jetzt stehst du hinter der Hecke und beobachtest 
    den mutmaßlichen Einbrecher. 
    Du schaust etwas genauer hin und siehst, dass 
    es sich um niemand anderen als Sherlock Holmes handelt. 
    Aber Sherlock Holmes bricht doch nirgendwo ein, es sei 
    denn er hat einen Fall!
    """)
    print(prompt0)
    ans0: int = int(input(dedent(f"""
    **Was hast du jetzt vor?** [1/2]
    1. Du gehst doch ins Haus hinein. Du willst nämlich 
    wissen, was Sherlock Holmes dort macht
    2. Aus irgendwelchen Gründen willst du dir den 
    Gartenzwerg direkt hinter dir nochmal genauer anschauen 
    und drehst dich um
    """)))

    if ans0 == 1:
        return inside_house(s)
    elif ans0 == 2:
        return stolpern(s)
    else:
        options_message_2(s)
        return beobachten(s)


def gesicht_am_fenster(s: str) -> str:
    prompt0 = dedent(f"""
    Du traust dich nicht hineinzugehen, aber starrst wie gebannt 
    auf das Fenster, in dem sich das Taschenlampenlicht bewegt. 
    Auf einmal siehst du ein bleiches Gesicht am Fenster. 
    Die Person hat noch nicht nach draußen gesehen und 
    dich noch nicht bemerkt... 
    """)
    print(prompt0)
    ans1: int = int(input(dedent(f"""
    **Was wirst du tun?** [1/2/3]
    1. Schnell wegrennen
    2. Dich hinter eine Hecke ducken und weiter beobachten
    3. Ins Haus hineingehen, denn irgendwie hast du doch Mut bekommen.
    """)))

    if ans1 == 1:
        return stolpern(s)
    elif ans1 == 2:
        return beobachten(s)
    else:
        options_message_3(s)
        return inside_house(s)


# --- Spielausführung
enter_game('')
