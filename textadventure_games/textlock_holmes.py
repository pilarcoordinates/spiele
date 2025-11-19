# Aufgabe 3-2 Text Adventure Game
# Imports

import numpy as np
name: str = None


# --- Haupthandlung
def maingame(s: str) -> str:
    """Startet das Hauptspiel mit den ersten Optionen."""
    prompt0: str = 'The Game is on!'
    prompt1: str = (
        'Du befindest dich im London des 21. Jahrhunderts. '
        'Du stehst auf einer dunklen, menschenleeren Straße. '
        'Leichter Nieselregen setzt sich auf deinem Mantel ab '
        'und du spürst eine Windbrise durch dein Haar streichen. '
        'Du siehst dich um. Alles um dich herum ist dunkel. '
        'Alles? Alles, bis auf ein einzelnes Fenster im ersten Stock. '
        'Es sieht aus, als würde jemand mit einer Taschenlampe '
        'durch das Zimmer laufen, '
        'eines etwas heruntergekommenen Backsteinhauses zu deiner Rechten. '
        'Du näherst dich, sorgsam darauf bedacht, deine Schritte nicht zu '
        'laut werden zu lassen. Beim Vorgarten angekommen bemerkst du, '
        'dass die Eingangstüre des Hauses einen Spalt breit offen steht.'
    )
    prompt2: str = '**Willst du hineingehen?** [1/2/3]'
    prompt3: str = (
        '1. Nein. \n'
        '2. Mh, ich rufe lieber erstmal Inspector Lestrade an...\n'
        '3. Ja, sofort! \n'
    )

    print(prompt0)
    print(prompt1)
    print(prompt2)
    ans0: int = int(input(prompt3))

    if ans0 == 1:
        return gesicht_am_fenster(s)
    elif ans0 == 2:
        return call_lestrade(s)
    elif ans0 == 3:
        return inside_house(s)
    else:
        prompt4: str = 'Bitte entscheide dich für 1., 2. oder 3.'
        print(prompt4)
        return maingame(s)


def maingame_version2(s: str) -> str:
    prompt0: str = (
        'Mh, der Inspektor ist nicht ans Telefon gegangen. '
        'Vielleicht geht er aber dran, wenn ich nochmal anrufe? '
        '**Was willst du jetzt versuchen?** [1/2/3]\n'
    )
    prompt1: str = (
        '1. Ich rufe nochmal Inspektor Lestrade an. \n'
        '2. Ich gehe doch ins Haus.\n'
    )
    print(prompt0)
    ans2: int = int(input(prompt1))

    if ans2 == 2:
        return gesicht_am_fenster(s)
    elif ans2 == 1:
        return call_lestrade(s)
    else:
        prompt2: str = 'Bitte entscheide dich für 1 oder 2'
        print(prompt2)
        return maingame_version2(s)


def game_exit(s: str) -> str:
    """Beendet das Spiel bei Nein Antwort"""
    print(
        'Sherlock Holmes schüttelt enttäuscht den Kopf '
        'und geht...( ͡ಠ ʖ̯ ͡ಠ)'
    )
    return s


def dumb(s: str) -> str:
    """Antwort, wenn der Spieler die Anweisung nicht versteht."""
    prompt0: str = (
        'Das war keine mögliche Antwort... _/(.-.) '
        'Versuche es gerne nochmal.'
    )
    print(prompt0)
    return maingame(s)


def newstart(s: str) -> str:
    """Neustart des Spiels"""
    prompt0: str = (
        'John Watson hat dich leider nicht verstanden '
        '... _(ಠ_ಠ)_/ Aber versuche es gern nochmal!'
    )
    print(prompt0)
    return maingame(s)


def gesicht_am_fenster_version2(s: str) -> str:
    prompt0: str = (
        'Du wartest also auf den Inspektor und schaust dir das Fenster '
        'genauer an, in dem sich das Taschenlampenlicht bewegt. '
        'Auf einmal siehst du ein bleiches Gesicht am Fenster. '
        'Die Person hat noch nicht nach draußen gesehen und '
        'dich noch nicht bemerkt... \n'
    )
    print(prompt0)
    ans1: int = int(input(
        '**Was wirst du nun tun?** [1/2/3]\n'
        '1. Wegrennen\n'
        '2. Dich hinter eine Hecke ducken und weiter beobachten\n'
        '3. Ins Haus hineingehen, '
        'denn irgendwie hast jetzt du doch Mut bekommen.\n'
    ))

    if ans1 == 1:
        return stolpern(s)
    elif ans1 == 2:
        return beobachten(s)
    else:
        return inside_house(s)


def call_lestrade(s: str) -> str:
    """Ruft Inspektor Lestrade an. Dialog mit diesem."""
    global name
    prompt0: str = (
        'Du entfernst dich einige Schritte vom Haus '
        'und zückst dein Smartphone. Du suchst in deinen Kontakten '
        'nach der Nummer von Inspektor Lestrade und drückst auf anrufen. '
    )
    prompt1: str = 'Eine etwas unwirsche Stimme meldet sich.'
    prompt2: str = (
        'Du warstest eine Minute, bis der Anrufbeantworter von Lestrade '
        'sich meldet: '
        '"Hier Inspektor Lestrade von Scottland Yard. Ich bin gerade nicht '
        'erreichbar, aber hinterlassen Sie mir nach dem Ton eine Nachricht."\n'
    )
    print(prompt0)
    random_bit: bool = np.random.randint(0, 2, dtype=bool)

    if random_bit == 0:
        print(prompt1)
        prompt4: str = (
            '"Inspektor Lestrade von Scottland Yard. '
            'Wer spricht da?” [Gib hier deinen Namen ein] \n'
        )
        name = input(prompt4)
        print("Guten Abend,", name, "was gibt es Neues?")
        ans0: str = (
            '"Inspektor, ich stehe in einer Seitengasse nahe '
            'der Brixton Road vor einem Haus in dem '
            'vermutlich eingebrochen wurde. '
            'Die Türe ist offenbar aufgebrochen worden und '
            'im ersten Stock sehe ich das Licht '
            'einer Taschenlampe."\n'
        )
        print(ans0)
        prompt5: str = (
            '"Ah ja. Bleiben Sie, wo sie sind. Ich komme vorbei '
            'um mir das anzusehen."\n'
        )
        print(prompt5)
        return gesicht_am_fenster_version2(s)

    elif random_bit == 1:
        print(prompt2)
        return maingame_version2(s)

    else:
        prompt6: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt6)
        return call_lestrade(s)


def final_game_stage(s: str) -> str:
    prompt0: str = (
        'Du fährst also in die Baker Street zu Sherlock Holmes. '
        'Jetzt kann das Abenteuer richtig beginnen! '
        'Aber das erfahren wir erst im nächsten Teil des '
        '**Sherlock Holmes Text Adventure**... '
        'Danke fürs Spielen! :) '
    )
    print(prompt0)
    return s


def inside_room(s: str) -> str:
    prompt0: str = (
        'Du öffnest die Türe und siehst zu deiner großen '
        'Überraschung Sherlock Holmes persönlich im Zimmer '
        'herumlaufen und offenbar etwas suchen. '
        'Er dreht sich um mit den Worten " ', name,
        ', Dr. Watson ist spurlos verschwunden und ich denke, es gibt '
        'Hinweise, wo er sein könnte, irgendwo hier in diesem Zimmer." \n'
        '"Mr. Holmes, woher wissen Sie meinen Namen?"\n'
        '"Nun, woher wissen Sie meinen? Ihren habe ich vorhin Ihrem Telefonat '
        'draußen mit Inspektor Lestrade entnehmen können. '
        'Habe da so meine Methoden..." \n'
        '"Niemand sonst hat so einen merkwürdigen Hut auf!"\n '
        '"Richtig deduziert, aber das ist kein merkwürdiger Hut, das ist '
        'ein Deerstalker. Aber genug davon! Kommen Sie nun mit, '
        'um Dr. Watson zu finden, oder nicht?"\n'
    )
    print(prompt0)
    prompt1 = (
        '1. Ja, natürlich!\n'
        '2. Nein, Sie schaffen das schon alleine...\n'
    )
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        return final_game_stage(s)
    elif ans0 == 2:
        return game_exit(s)
    else:
        prompt2 = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt2)
        return inside_room(s)


def sherlock_coming(s: str) -> str:
    prompt0: str = (
        'Du wartest hinter der Statue und zu '
        'deiner Überraschung kommt Sherlock Holmes persönlich aus dem Zimmer. '
        'In der linken Hand hat er einen zerknüllten Zettel und in der '
        'rechten eine Taschenlampe. '
        'Er dreht sich zu dir um mit den Worten " ', name,
        ', Dr. Watson ist spurlos verschwunden und ich denke, ich habe '
        'soeben Hinweise in diesem Zimmer gefunden." \n'
        '"Mr. Holmes, woher wissen Sie meinen Namen?"\n'
        '"Nun, woher wissen Sie meinen? Ihren habe ich vorhin Ihrem Telefonat '
        'draußen mit Inspektor Lestrade entnehmen können. '
        'Habe da so meine Methoden..." \n'
        '"Niemand sonst hat so einen merkwürdigen Hut auf!"\n '
        '"Richtig deduziert, aber das ist kein merkwürdiger Hut, das ist '
        'ein Deerstalker. Aber genug davon! Kommen Sie nun mit, '
        'um Dr. Watson zu finden, oder nicht?"\n'
    )
    print(prompt0)
    prompt1 = (
        '1. Ja, natürlich!\n'
        '2. Nein, Sie schaffen das schon alleine...\n'
    )
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        return final_game_stage(s)
    elif ans0 == 2:
        return game_exit(s)
    else:
        prompt2 = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt2)
        return inside_room(s)


def first_floor(s: str) -> str:
    prompt0: str = (
        'Du gehst also die Treppe nach oben und hörst, '
        'als du angekommen bist, Schritte in dem Zimmer '
        'zu deiner Linken.\n'
    )
    prompt1: str = (
        '**Was willst du tun?**\n'
        '1. Ins Zimmer hineingehen\n'
        '2. Mich hinter einer Statue links vom Zimmer verstecken '
        'und warten\n'
    )
    print(prompt0)
    ans0 = int(input(prompt1))

    if ans0 == 1:
        return inside_room(s)
    elif ans0 == 2:
        return sherlock_coming(s)
    else:
        prompt2: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt2)
        return first_floor(s)


def right_door(s: str) -> str:
    prompt0: str = (
        'Du gehst durch die rechte Türe und gelangst in eine Küche. '
        'Von oben hörst du Schritte die Treppe herunterkommen. '
        'Zu deiner Überraschung kommt Sherlock Holmes auf einmal in die '
        'Küche. In der linken Hand hat er einen zerknüllten Zettel '
        'und in der rechten eine Taschenlampe. '
        'Er dreht sich zu dir mit den Worten: '
        f'"{name}, Dr. Watson ist spurlos verschwunden und ich denke, '
        'ich habe soeben Hinweise in diesem Zimmer gefunden." \n'
        '"Mr. Holmes, woher wissen Sie meinen Namen?"\n'
        '"Nun, woher wissen Sie meinen? Ihren habe ich vorhin Ihrem Telefonat '
        'draußen mit Inspektor Lestrade entnehmen können. '
        'Habe da so meine Methoden..." \n'
        '"Niemand sonst hat so einen merkwürdigen Hut auf!"\n'
        '"Richtig deduziert, aber das ist kein merkwürdiger Hut, '
        'das ist ein Deerstalker. Aber genug davon! Kommen Sie nun mit, '
        'um Dr. Watson zu finden, oder nicht?"\n'
    )
    print(prompt0)
    prompt1: str = (
        '1. Ja, natürlich!\n'
        '2. Nein, Sie schaffen das schon alleine...\n'
    )
    print(prompt1)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        prompt2: str = (
            'Du fährst also mit Sherlock in die Baker Street. '
            'Jetzt kann das Abenteuer richtig beginnen! '
            'Aber das erfahren wir erst im nächsten Teil des '
            '**Sherlock Holmes Text Adventure**...\n'
            'Danke fürs Spielen! :) '
        )
        print(prompt2)
    elif ans0 == 2:
        return game_exit(s)
    else:
        prompt3: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt3)
        return right_door(s)


def inside_house(s: str) -> str:
    prompt0: str = (
        'Du stehst vor der Eingangstür und schaust durch den Spalt '
        'in den verlassenen Flur, bevor du die Tür schließlich '
        'öffnest und hinein gehst. Du siehst direkt vor dir eine '
        'Treppe, welche wohl in den ersten Stock führt. '
        'Rechts neben dir siehst du eine weitere Türe.'
    )
    print(prompt0)
    ans0: int = int(input(
        '**Wo möchtest du jetzt hingehen?** [1/2] \n'
        '1. Über die Treppe nach oben\n'
        '2. Nach rechts durch die Türe.\n'
    ))
    if ans0 == 1:
        return first_floor(s)
    elif ans0 == 2:
        return right_door(s)
    else:
        prompt1: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt1)
        return inside_house(s)


def enter_game(s: str) -> str:
    """Begrüßt den Spieler und fragt, ob er das Spiel starten möchte."""
    start_prompt: str = 'Willkommen zum Sherlock Holmes Text Adventure Game.'
    print(start_prompt)
    ans: str = str(input('**Willst du das Spiel starten?** [ja/nein] \n'))

    if ans.lower().strip() == 'ja':
        return maingame(s)
    elif ans.lower().strip() == 'nein':
        return game_exit(s)
    else:
        return newstart(s)


def papier_allein_lesen(s: str) -> str:
    prompt0: str = (
        'Auf dem Papier steht\n "Kommen Sie sofort in die Bakerstreet 221b. '
        'Dr. Watson ist spurlos verschwunden und Sie sind von Nutzen '
        'in der Angelegenheit.\n S.H."'
    )
    prompt1: str = (
        '**Was willst du machen?** [1/2]\n'
        '1. Die Nachricht Inspektor Lestrade zeigen\n'
        '2. Inspektor Lestrade sagen, dass du dich nicht '
        'wohl fühlst und gehen musst – in Wahrheit gehst du '
        'aber in die Baker Street\n'
    )
    print(prompt0)
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        return papier_zeigen(s)
    elif ans0 == 2:
        return final_game_stage(s)
    else:
        prompt2: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt2)
        return papier_allein_lesen(s)


def papier_zeigen(s: str) -> str:
    prompt0: str = (
        'Du zeigst Inspektor Lestrade das Papier. '
        '"Nun, ', name, ', wir sollten schnellsten '
        'in die Baker Street gehen und Holmes '
        'behilflich sein. Es ist schließlich selten, '
        'dass er überhaupt mal die Hilfe von Leuten '
        'außer Watson benötigt. \n'
        'Kommen Sie mit? [1/2]"\n'
    )
    print(prompt0)
    prompt1: str = (
        '1. Ja, klar!\n'
        '2. Nein...\n'
    )
    ans0: int = int(input(prompt1))

    if ans0 == 1:
        prompt2: str = (
            'Du fährst daher mit Lestrade in die Baker Street. '
            'Jetzt kann das Abenteuer richtig beginnen! '
            'Aber das erfahren wir erst im nächsten Teil des '
            '**Sherlock Holmes Text Adventure**... '
            'Danke fürs Spielen! :) '
        )
        print(prompt2)
        return s
    elif ans0 == 2:
        prompt3 = (
            'Lestrade: "Schade, aber kann ich Sie verstehen. '
            'Es könnte ja schließlich auch gefährlich werden!"\n'
            'Und hiermit endet das **Sherlock Holmes Text Adventure**\n'
            'Danke fürs Spielen! :) '
        )
        print(prompt3)
        return s
    else:
        prompt4: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt4)
        return papier_allein_lesen(s)


def lestrade_arrives(s: str) -> str:
    prompt0: str = (
        'Du fühlst, wie dich jemand schüttelt, während du langsam '
        'wieder zu Bewusstsein kommst. '
        'Wie viel Zeit ist wohl vergangen? ', name,
        '", was ist passiert?" '
        'hörst du Inspektor Lestrade hektisch sagen. '
        'Du setzt dich langsam auf und '
        'stützt dich dabei auf dem Boden ab. Dabei bemerkst du, '
        'dass unter deiner Hand ein zerknülltes Blatt Papier liegt.'
    )
    print(prompt0)
    ans0: int = int(input(
        '**Was möchtest du tun?** [1/2]\n'
        '1. Das Papier direkt Inspektor Lestrade zeigen.\n'
        '2. Das Papier unauffällig in der Hand behalten '
        'und dem Inspektor nicht zeigen\n'
    ))

    if ans0 == 1:
        return papier_allein_lesen(s)
    elif ans0 == 2:
        return papier_zeigen(s)
    else:
        prompt4: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt4)
        return lestrade_arrives(s)


def stolpern(s: str) -> str:
    prompt0: str = (
        'Du bewegst dich einige Schritte zurück, musst dann '
        'aber straucheln. '
        '"Mist, bin ich etwa auf einer Nacktschnecke ausgerutscht?" '
        'geht es dir durch den Kopf, '
        'bevor du hart auf dem Boden aufschlägst. '
        'Du hörst im Hintergrund ein Auto vor der '
        'Einfahrt des Hauses parken. '
        'Dann verlierst du das Bewusstsein...'
    )
    print(prompt0)
    ans0: int = int(input(
        '**Was willst du nun tun?** [1/2/3]\n'
        '1. Bewusstlos werden und warten... \n'
        '2. Das Spiel beenden\n'
        '3. Das Spiel von vorne beginnen\n'
    ))
    if ans0 == 1:
        return lestrade_arrives(s)
    elif ans0 == 2:
        return game_exit(s)
    elif ans0 == 3:
        return enter_game(s)
    else:
        prompt1: str = (
            'Ungültige Eingabe. Entscheide dich für 1., 2. oder 3.'
        )
        print(prompt1)
        return stolpern(s)


def beobachten(s: str) -> str:
    prompt0: str = (
        'Jetzt stehst du hinter der Hecke und beobachtest '
        'den mutmaßlichen Einbrecher. '
        'Du schaust etwas genauer hin und siehst, dass '
        'es sich um niemand anderen als Sherlock Holmes handelt. '
        'Aber Sherlock Holmes bricht doch nirgendwo ein, es sei '
        'denn er hat einen Fall!'
    )
    print(prompt0)
    ans0: int = int(input(
        '**Was hast du jetzt vor?** [1/2/3]\n'
        '1. Du gehst doch ins Haus hinein. Du willst nämlich '
        'wissen, was Sherlock Holmes dort macht\n'
        '2. Aus irgendwelchen Gründen willst du dir den '
        'Gartenzwerg direkt hinter dir nochmal genauer anschauen '
        'und drehst dich um\n'
    ))

    if ans0 == 1:
        return inside_house(s)
    elif ans0 == 2:
        return stolpern(s)
    else:
        prompt2: str = 'Bitte entscheide dich für 1. oder 2.'
        print(prompt2)
        return beobachten(s)


def gesicht_am_fenster(s: str) -> str:
    prompt0: str = (
        'Du traust dich nicht hineinzugehen, aber starrst wie gebannt '
        'auf das Fenster, in dem sich das Taschenlampenlicht bewegt. '
        'Auf einmal siehst du ein bleiches Gesicht am Fenster. '
        'Die Person hat noch nicht nach draußen gesehen und '
        'dich noch nicht bemerkt... \n'
    )
    print(prompt0)
    ans1: int = int(input(
        '**Was wirst du tun?** [1/2/3]\n'
        '1. Schnell wegrennen\n'
        '2. Dich hinter eine Hecke ducken und weiter beobachten\n'
        '3. Ins Haus hineingehen, denn irgendwie hast du doch Mut bekommen.\n'
    ))

    if ans1 == 1:
        return stolpern(s)
    elif ans1 == 2:
        return beobachten(s)
    else:
        prompt1: str = (
            'Bitte entscheide dich für 1., 2. oder 3.'
        )
        print(prompt1)
        return inside_house(s)


# --- Spielausführung
enter_game('')
