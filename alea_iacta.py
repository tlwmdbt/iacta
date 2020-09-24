# Würfelsimulator ==================================
from random import seed, randint
#===================================================
# Endlosschleife mit Exception Handling um User Input 
# einzulesen und zu formatieren
while True:
    # 1. Frage "Wieviele Würfel"
    while True:
        dice = input("\nWieviele Würfel (quit um zu beenden)? ")
        try:
            int_dice = int(dice)
            if int_dice < 1 or int_dice > 10:
                print("Zahl zwischen 1 und 10, quit um zu beenden.")
                continue
            break
        except ValueError:
            if "quit" in dice:
                raise SystemExit

            print("Zahl zwischen 1 und 10, quit um zu beenden.")

            continue
        else:
            print("Nein, nochmal, Zahlen zwischen 1 bis 10.")
        finally:
            if "quit" in dice:
                print("Bye!\n")
                raise SystemExit

    # 2. Frage "Was für ein Würfel Typ 1d10, 1d6, etc."
    while True:
        dice_typ = input("Wieviele Augen soll der Würfel haben (quit um zu beenden)? ")
        
        try:
            int_dice_typ = int(dice_typ)
            if int_dice_typ < 1 or int_dice_typ > 100:
                print("Zahl zwischen 1 und 100, quit um zu beenden.")
                continue
            break
        except ValueError:
            if "quit" in dice_typ:
                raise SystemExit

            print("Zahl zwischen 1 und 100, quit um zu beenden.")
            continue
        else:
            print("Nein, nochmal, Zahlen zwischen 1 bis 100.")
        finally:
            if "quit" in dice_typ:
                print("Bye!\n")
                raise SystemExit

    # User Wahl zeigen:
    print("Deine Wahl:", int_dice, "d", int_dice_typ)

    # den Random Generator mit /dev/urandom initialisieren wenn möglich
    while True:
        try:
            # Wenn das Laden des Moduls urandom keinen Fehler produziert, 
            # weitermachen mit der Würfelsimulation
            from os import urandom
            seed(int.from_bytes(urandom(100), byteorder='big', signed=False))
            #print("Benutze /dev/urandom.")
            break
        except ImportError:
            # Modul urandom nicht vorhanden, darum eingebaute python random 
            # Funktion benutzen um den Random Generator zu initialisieren
            #print("Benutze standard randint().")
            seed(randint(1, 1000))
            break
        else:
            # Geht beides nich, auf wiedersehen! ¯\_(ツ)_/¯ 
            print("Kein random möglich. Bye!")
            raise SystemExit

    # Würfe generieren:
    i = 1
    actual_throw_tmp = 0

    while i <= int_dice:
        actual_throw = randint(1, int_dice_typ)
        actual_throw_tmp = actual_throw_tmp + actual_throw
        print("Wurf", i, ":", actual_throw)
        
        i = i + 1
    print("Gesammte Augenanzahl:", actual_throw_tmp)
