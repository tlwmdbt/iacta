# Würfelsimulator ==================================
from random import seed, randint
#===================================================
# Endlosschleife mit Exception Handling um User Input 
# einzulesen und zu formatieren
while True:
    # 1. Frage "Wieviele Würfel"
    while True:
        dice = input("\nWieviele Würfel (quit um zu beenden): ")
        try:
            int_dice = int(dice)
            if int_dice < 1 or int_dice > 10:
                print("Zahl zwischen 1 und 10, quit um zu beenden.")
                continue
            break
        except ValueError:
            continue
        else:
            print("Nein, nochmal, Zahlen zwischen 1 bis 10.")
        finally:
            if "quit" in dice:
                print("Bye!\n")
                raise SystemExit

    # 2. Frage "Was für ein Würfel Typ 1d10, 1d6, etc."
    while True:
        dice_typ = input("Würfel Art: d")
        try:
            int_dice_typ = int(dice_typ)
            if int_dice_typ < 1 or int_dice_typ > 100:
                print("Zahl zwischen 1 und 100, quit um zu beenden.")
                continue
            break
        except ValueError:
            continue
        else:
            print("Nein, nochmal, Zahlen zwischen 1 bis 100.")
        finally:
            if "quit" in dice_typ:
                print("Bye!\n")
                raise SystemExit

    # User Wahl zeigen:
    print("Deine Wahl:", int_dice, "d", int_dice_typ)

    # Counter
    i = 1

    # Initialize the random generator from OS specific random device
    while True:
        try:
            # check if /dev/urandom is working
            # If it exist (no error is produced) it is used to seed the python random generator later used
            from os import urandom
            seed(int.from_bytes(urandom(100), byteorder='big', signed=False))
            print("Benutze /dev/urandom.")
            break
        except ImportError:
            # module not available, so use standard randint (should be also secure)
            print("Benutze standard randint().")
            seed(randint(1, 1000))
            break
        else:
            # all other cases, kill -9 this script - bye bye ¯\_(ツ)_/¯ 
            print("Kein random möglich. Bye!")
            raise SystemExit

    # Eingabe auswerten und Würfe generieren:
    while i <= int_dice:
        actual_throw = randint(1, int_dice_typ)
        print("\nWurf", i, ":", actual_throw)
        i = i + 1
