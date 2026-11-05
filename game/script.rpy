# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
default diceroll = Twod6()

default aero = Aero(Character("Aero"), {"Affluence": 0,
                                        "Arrogance": 0, 
                                        "Awareness": 0,
                                        "Knowledge": 0, 
                                        "Patience": 0 }, 6)
                                    

define neon = Character("Neon")
define clem = Character("Clementine")
define selene = Character("Selene")
define lynx = Character("Lynx")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    python:
        print(success_rate(10, diceroll()))
        print(success_rate(5, diceroll()))
        print(success_rate(12, diceroll()))
        print(success_rate(1, diceroll()))
        
        aero.statMath("Affluence", 200)
        print(aero.stats)
        
        
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    jump common_route

    return
