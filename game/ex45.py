#This will be an OOP version of Ex 36
# -*- coding: utf-8 -*-
# ^ this is for foreign text.
from sys import exit
import sys
from textwrap import dedent
from playsound import playsound as plays

class Player(object):
    def __init__(self, name, items):
        ## Person has-a name
        self.name = name

        #Person has-a items
        self.items = items

class Scene(object):

    def enter(self):
        exit(1)

    def walking():
        """Just prints the walking strings"""
        print("\nYou walk towards the painting.")
        print("Upon further examination, you see more details.")
        input()

    def learn_to_type():
        """Error message user gets for typing something nonsensical or erroneous"""
        print(f"\nI'm sorry {Player.name}, I don't know what to do with that ☹ ")
        input()
        print(dedent("""
            Please type something that makes sense.
            Or press 'CTRL Z' to end the game.
            We'll only be a lil hurt if you do that (ಥ_ಥ) """))
        input()

    def sucked_in():
        """This is the text for when you touch a painting"""
        print(dedent("""
            You defy every sign you've ever seen at a museum and touch the painting.
            As soon as you do, you feel slingshot into the painting."""))
        plays("painting.wav")
        input()

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play_game(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter() #this is a loop to move you through the Map.
                                                    #As you Enter() one room, it returns a Key from Scenes{}.
                                                    #Then current_scene is set to the Class for the the next scene
                                                    #This is done by next_scene(), that takes the returned value from Enter(),
                                                    #searches the dict and finds the value pair.
                                                    #The loop starts again.
                                                    #This time it makes next_scene_name equal to current_scene (value from next_scene())
                                                    #and uses Enter(). This returns a value and everything repeats again.
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter() #Once you reach the last scene, Finished(), this line Enters() the ending scence

class Death(Scene):
    """This is the message players get upon dying"""
    def enter(self):
        print("""
                         uuuuuuu
                     uu$$$$$$$$$$$uu
                  uu$$$$$$$$$$$$$$$$$uu
                 u$$$$$$$$$$$$$$$$$$$$$u
                u$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$"   "$$$"   "$$$$$$u
               "$$$$"      u$u       $$$$"
                $$$u       u$u       u$$$
                $$$u      u$$$u      u$$$
                 "$$$$uu$$$   $$$uu$$$$"
                  "$$$$$$$"   "$$$$$$$"
                    u$$$$$$$u$$$$$$$u
                     u$"$"$"$"$"$"$u
          uuu        $$u$ $ $ $ $u$$       uuu
         u$$$$        $$$$$u$u$u$$$       u$$$$
          $$$$$uu      "$$$$$$$$$"     uu$$$$$$
        u$$$$$$$$$$$uu    \"\"\"\"\"    uuuu$$$$$$$$$$
        $$$$\"\"\"$$$$$$$$$$uuu   uu$$$$$$$$$\"\"\"$$$\"
         \"\"\"      \"\"$$$$$$$$$$$uu \"\"$\"\"\"
                   uuuu \"\"$$$$$$$$$$uuu
          u$$$uuu$$$$$$$$$uu \"\"$$$$$$$$$$$uuu$$$
          $$$$$$$$$$\"\"\"\"           \"\"$$$$$$$$$$$\"
           \"$$$$$\"                      \"\"$$$$\"\"
             $$$"                         $$$$\"
        """)
        plays("death.wav")
        input()

        print(dedent(f"""
            Oh no!
            You died! ⚰
            Try playing the game again.
            This time, try choosing something different, try choosing more wisely."""))
        exit(0)

class PrankScreen(Scene):
    """This is just a prank scene to make the user believe they'll be playing Zelda"""
    def enter(self):
        input('Hello, press Enter to start game or CTRL Z at any point to terminate the game.')
        print("""
                           __        __   /\\/
                          /==\\      /  \\_/\\/
                        /======\\    \\/\\__ \\__
                      /==/\\  /\\==\\    /\\_|__ \\
                   /==/    ||    \\=\\ / / / /_/
                 /=/    /\\ || /\\   \\=\\/ /
              /===/   /   \\||/   \\   \\===\\
            /===/   /_________________ \\===\\
         /====/   / |                /  \\====\\
       /====/   /   |  _________    /  \\   \\===\\    THE LEGEND OF
       /==/   /     | /   /  \\ / / /  __________\\_____      ______       ___
      |===| /       |/   /____/ / /   \\   _____ |\\   /      \\   _ \\      \\  \\
       \\==\\             /\\   / / /     | |  /= \\| | |        | | \\ \\     / _ \\
       \\===\\__    \\    /  \\ / / /   /  | | /===/  | |        | |  \\ \\   / / \\ \\
         \\==\\ \\    \\  /____/   /_\\ //  | |_____/| | |        | |   | | / /___\\ \\
         \\===\\ \\   \\\\\\\\\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |
           \\==\\/     \\\\\\\\/ / //////   \\| |/==/ \\| | |        | |   | | | /   \\ |
           \\==\\     _ \\/ / /////     _ | |==/     | |        | |  / /  | |   | |
             \\==\\  / \\ / / ///      /|\\| |_____/| | |_____/| | |_/ /   | |   | |
             \\==\\ /   / / /________/ |/_________|/_________|/_____/   /___\\ /___\\
               \\==\\  /               | /==/
               \\=\\  /________________|/=/    OCARINA OF TIME
                 \\==\\     _____     /==/
                / \\===\\   \\   /   /===/
               / / /\\===\\  \\_/  /===/
              / / /   \\====\ /====/
             / / /      \\===|===/
             |/_/         \\===/
                            =""")
        plays('prank.wav')
        input()

        print("Jk. I'm not that fancy with Python.")
        print("Press 'Enter' again to start the actual game.")
        input()

        return 'welcome_screen'

class Welcome(Scene):
    """Welcomes player to game"""

    def enter(self):
        input("""
 __    __   __   __   __   __   __   __    __   __    __   __   __
_\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
\\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/
  __    __   __   __   __   __   __   __    __   __    __   __   __
 _\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
 \\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/
  __  __                 _   _             _
 |  \\/  |           /\\  | | | |           | |
 | \\  / |_   _     /  \\ | |_| |_ __ _  ___| | __   ___  _ __
 | |\\/| | | | |   / /\\ \\| __| __/ _` |/ __| |/ /  / _ \\| '_ \\
 | |  | | |_| |  / ____ \\ |_| || (_| | (__|   <  | (_) | | | |
 |_|  |_|\\__, | /_/    \\_\\__|\\__\\__,_|\\___|_|\\_\\  \\___/|_| |_|
   _____  __/ |                  _____      _       _   _
  / ____||___/                  |  __ \\    (_)     | | (_)
 | (___  _   _ _ __   ___ _ __  | |__) |_ _ _ _ __ | |_ _ _ __   __ _ ___
  \\___ \\| | | | '_ \\ / _ \\ '__| |  ___/ _` | | '_ \\| __| | '_ \\ / _` / __|
  ____) | |_| | |_) |  __/ |    | |  | (_| | | | | | |_| | | | | (_| \\__ \\
 |_____/ \\__,_| .__/ \\___|_|    |_|   \\__,_|_|_| |_|\\__|_|_| |_|\\__, |___/
              | |                                                __/ |
              |_|                                               |___/
  _    _  _  ____  ____  ___  ____  _____  _  _    ___     ___     _
 / )  ( \\/ )( ___)(  _ \\/ __)(_  _)(  _  )( \\( )  (__ \\   / _ \\   ( \\
( (    \\  /  )__)  )   /\\__ \\ _)(_  )(_)(  )  (    / _/  ( (_) )   ) )
 \\_)    \\/  (____)(_)\\_)(___/(____)(_____)(_)\\_)  (____)()\\___/   (_/

 __    __   __   __   __   __   __   __    __   __    __   __   __
_\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
\\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/
  __    __   __   __   __   __   __   __    __   __    __   __   __
 _\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
 \\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/""")

        print("\nWelcome to My Attack on Super Paintings! (Python 3 version)")
        plays("intro.wav")
        input()

        print(f"Or as the creator of this game calls it, '{sys.argv[0]}' script")
        input()

        Player.name = input("First, what's your name?\n>")
        print(dedent(f"""
            Nice! Glad to meet you {Player.name}.
            Let's get started."""))
        input()

        print("Oh, and make sure you have your volume turned on 🔊")
        input()

        return 'start_room'

class StartRoom(Scene):
    """This sets up the world for the player & describes the paintings."""
    def enter(self):
        print(f"You wake up alone in a strange room...")
        input()

        print(dedent("""
            The walls are made of white, dull stones.
            You are at the entrance of a hallway.
            It's right ahead of you.
            Down the hallway is a red carpet with a giant painting at the end."""))
        input()

        print(dedent("""
            You look at the painting ahead of you (#1).
            It looks like a snowy, winter scene from Tokyo (東京).
            You don't have snow boots, but you notice a pair under the painting."""))
        input()

        print(dedent("""
            There's some humanoid looking giant of titan-size attacking the city.
            Some hero seems to be battling it. The hero is normal sized.
            You guess that the hero might lose, given the size difference."""))
        input()

        print(dedent("""
            You look at the painting towards your right (#2).
            It shows modern day Seoul (서울), the Hyehwa (혜화) area.
            You see people in brightly colored uniforms fighting during a hot, summer day.
            Their hairstyles are only slightly less ridiculous than their clothing."""))
        input()

        print(dedent("""
            You can't tell who's winning or losing.
            Or who's good or evil (because what does good/evil even look like?).
            All you can see is that the city looks empty and only partially destroyed."""))
        input()

        print(dedent("""
            You look the painting to your left (#3).
            It shows some kind of castle standing tall and alone in the background.
            It's spring and cherry blossoms seem to be falling slowly.
            There's a path leading to it making the castle easily accesible."""))
        input()

        return 'what_direction'

class Test(Scene):#This is a scene to test with to skip the scenes that are dialogue heavy
    def enter(self):
        Player.name = input("First, what's your name?\n>")

        return 'what_direction'

class WhatDirection(Scene):
    """This let's the user decide what painting/world to visit."""
    def enter(self):
        self.forward = ['forward', 'Foward', 'front', 'Front', 'F', 'f', '#1', '1', "pa'lante", 'adelante', 'pa lante']
        self.right = ['right', 'Right', 'r', 'R', '2', '#2', 'derecha']
        self.left = ['left', 'Left', 'l', 'L', '#3', '3', 'izquierda']
        self.up = ['jump', 'jump up', 'jump off wall', 'jump on wall', 'ceiling', '#4', '4', 'j', 'u', 'mirror', 'm', 'up']
        self.back =['back', 'b', 'turn around']

        print(dedent(f"""
            So {Player.name}, what do you want to do?
            What direction do you want to go in?
            You can also try to touch the mirror if that's your thing.
            """))
        player_Choice = input("> ")

        if player_Choice in self.forward: #This allows you to go to painting1
            WhatDirection.walking()
            return 'painting1'


        elif player_Choice in self.right: #This allows you to go to painting2
            WhatDirection.walking()
            return 'painting2'

        elif player_Choice in self.left: #This allows you to go to painting3
            WhatDirection.walking()
            return 'painting3'

        elif player_Choice in self.up: #This allows you to touch the ceiling/mirror
            print(f'Interesting choice {Player.name}')
            input()

            return 'mirror'

        elif player_Choice in self.back: #This resets the scene; you can't go back
            print(dedent(f"""
                I'm sorry {Player.name}, but you can't do that.
                The only way out is ahead.
                Pick a painting if you want to escape."""))
            input()
            return 'what_direction'

        else:
            WhatDirection.learn_to_type()
            return 'what_direction'

        return 'debug'

class PaintingOne(Scene):
    """This is the start of the AoT world"""
    def enter(self):
        """This is the path for painting #1 i.e the AoT painting"""

        Player.items = []

        input("The monster seems to be eating something human looking.")
        print(dedent("""
            The hero also looks like they've unresolved childhood trauma.
            You look at a particular subject of the painting.
            It looks like some beast-looking, titan-sized monster."""))
        input()

        print("""
                      ,   .-'"'=;_  ,
                      |\\.'-~`-.`-`;/|
                      \\.` '.'~-.` './
                      (\\`,__=-'__,'/)
                   _.-'-.( d\_/b ).-'-._
                 /'.-'   ' .---. '   '-.`\\
               /'  .' (=    (_)    =) '.  `\\
              /'  .',  `-.__.-.__.-'  ,'.  `\\
             (     .'.   V       V  ; '.     )
             (    |::  `-,__.-.__,-'  ::|    )
             |   /|`:.               .:'|\\   |
             |  / | `:.              :' |`\\  |
             | |  (  :.             .:  )  | |
             | |   ( `:.            :' )   | |
             | |    \\ :.           .: /    | |
             | |     \\`:.         .:'/     | |
             ) (      `\\`:.     .:'/'      ) (
             (  `)_     ) `:._.:' (     _(`  )
             \\  ' _)  .'           `.  (_ `  /
              \\  '_) /   .'"```"'.   \\ (_`  /
               `'"`  \  (         )  /  `"'`
           ___        `.`.       .'.'        ___
         .`   ``\"\"\"\'\'\'--`_)     (_'--'\'\'\"\"\"``   `.
        (_(_(___...--'"'`         `'"'--...___)_)_)
        """)

        input()

        boots = "Snow Boots"
        print(dedent("""
            You also look at the snow boots.
            They're very fashionable and seem practical.
            You decide to take them."""))
        Player.items.append(boots)
        input()

        print("\nYou got Spumoni boots!")
        plays("item.wav")

        input(f"\nItems:\n{Player.items}")

        PaintingOne.sucked_in()

        return 'attack_on_titan'

class AOT(Scene):
    """This is if the user decides to touch P1; They are now in the AOT world"""
    def enter(self):
        Yes = ['Y', 'y', 'Yes', 'yes']
        No = ['N', 'n', 'No', 'no']
        Player.items = [] #you need to figure out how to pass this list from the previous scenes
        print(dedent("""
            You land hard on concrete.
            Dazed, you look around as you feel a rhythmic thundering.
            The sharp, cold air only adds to your frustration."""))

        input()
        print(dedent("""
            There's snow everywhere.
            You decide to put on your new, stylish yet practical snow boots.
            They provide a lot more grip than your old shoes."""))

        input()
        print(dedent("""
            You now see the cause of all the thundering.
            The Jaw Titan, I mean monster is smashing his way through the city.
            It roars, striking terror in your heart."""))

        input()
        print("""            _______________
           /               \\
          /                 \\
        //                   \\/\\
        \\|   XXXX     XXXX   | /
         |   XXXX     XXXX   |/
         |   XXX       XXX   |
         |                   |
         \\__      XXX      __/
           |\     XXX     /|
           | |           | |
           | I I I I I I I |
           |  I I I I I I  |
           \\_             _/
             \\_         _/
               \\_______/""")
        plays("roar.wav")

        input()
        print(dedent(f"""
            You also see some humans zipping around, using some kind of mechanical device.
            There's one next to you, with a sticky note that says 'VME'."""))
        while True:
            grab = input(f"Do you want to grab it? \n\n>")

            if grab in Yes:
                VME = 'VME ⚙ '
                Player.items.append(VME)
                print("\nYou got the Vertical Maneuvering Equipment (VME)!")
                plays("item.wav")

                input()
                print(f"Items:\n{Player.items}")

                input()
                print(dedent("""
                    You also see a pair of distinctive looking swords.
                    You think they look cool!
                    You decide to grab them as well."""))

                input()
                print("You added 'Flesh Pairing Swords' to your items too!")
                plays("item.wav")
                swords = 'Flesh Pairing Swords ⚔ '
                Player.items.append(swords)

                input()
                print(f"Items:\n{Player.items}")

                input()
                print(f"Nice!")

                input()
                print(dedent("""
                    You're feeling prepared to help fight the titan, so you go towards the fight.
                    As you get there, the hero tells you how to take down a titan.
                    Given how new you are, you decide you can't fight and will distract the titan."""))

                input()
                print(dedent("""
                    The titan sees you and starts charging at you.
                    You use the VME to quickly navigate away, around the corner of some buildings.
                    The titan is quickly gaining on you and you notice the hero is no longer around.
                    You start to worry..."""))

                input()
                print(dedent("""
                    You continue turning corners as sharp as possible, trying to shake the titan.
                    On your last turn, the titan's hand falls upon you.
                    It barely missed you because you used your swords to parry.
                    However, the heavy attack has shattered your swords."""))

                input()
                Player.items.pop(1)
                print(f"Items:\n{Player.items}")

                input()
                print(dedent("""
                    You start to panic because now you're defenseless.
                    But suddenly, you see blood, the titan stops, and then starts to fall.
                    You see Levi, I mean the hero, standing on the nape of its neck."""))

                input()
                print(dedent("""
                    The hero nods in thanks and acknowledgement.
                    You nod back, thinking that they def should work on their timing.
                    Your VME is also out of gas, so you decide to discard it."""))

                input()
                Player.items.pop()
                print(f"Items:\n{Player.items}")

                input()
                print(dedent("""
                    All of a sudden, you hear a ringing sound.
                    You wake up...it dawns on you that this was a dream.
                    You realize you're going to be late for school, so you get out of bed."""))

                input()
                print(dedent("""
                    But then you notice, you're wearing those dope Spumoni boots.
                    You take a second to think about what that means....
                    Your second alarm goes off!
                    You head out for school, you'll think about all this later."""))

                return 'finished'

            elif grab in No:
                print(dedent("""
                    You realize this is outside your capabilities.
                    You see the titan suddenly swat the hero...it doesn't look good.
                    The titan then turns to face you; you immediately run away."""))

                input()
                print(dedent("""
                    The titan gives chase and you start to panic.
                    It reaches out with one hand.
                    You instinctively duck out in a nearby, partially destoryed building."""))

                input()
                print(dedent("""
                    Its thundering steps are only getting closer.
                    Its other hand starts coming for you.
                    Your mind goes blank, the shadow from its palm closes in on you."""))

                input()
                print(dedent("""
                    Just then, you hear an increduibly loud ringing sound.
                    It's your alarm...
                    You wake up...you realize it was all a dream.
                    You also realize you're late!"""))

                input()
                Player.items[:] = []

                print("You check if you still have the Spumoni boots.")

                input()

                print(f"Items: \n{Player.items}")

                input()
                print(dedent("""
                    You do not....sadness.
                    You arrive late to school"
                    Your homeroom teacher gives you detention.
                    For life..."""))
                input()

                return 'death'

            else:
                AOT.learn_to_type()

class PaintingTwo(Scene):
    """This is the start of the MHA world/Seoul"""
    def enter(self):
        Player.items = []

        print(dedent("""
            The disfigured man has on some kind of coat or suit.
            He also has a mask on that has valves or exhausts coming out of it.
            You observe the name of the creepy man is actually written below."""))
        input()

        print("""
                           _.._
                        .'      '
                       _;.-\"\"\"-.;_
                   _.-' _..-.-.._ '-._
                  ';--.-----------.--;'
                  \\\\     #     #     //
                   \\\\_   _______    //
                    \\\\  | || || |  //
                _.-'`;\\\\| || || | //   ;'-.
              .' :  /   | || || |   \\     '.
             /   : /__  \\ _____ / __\\ :      `.
            /    |   /  '._/_\\_.'  \\   :       `\\
          /      |      |()    ()      |         \\
        |         |                        |     /
        \\     \\   |][     |   |    ][ |   /     /
         \\     \\ ;=""====='\"\"\"'====""==; /     /
          |/`\\  \\/      |()    ()      \\/  /`\\|
           |_/.-';      |              |`-.\\_|
             /   |      ;              :   \\
             |__.|      |              |.__|
                 ;      |              |
                 '-._   ;           _.-'
                     `;"--.....--";`
                      |    | |    |
                      |    | |    |
                 _..._L____J L____J _..._
               .` "-. `%   | |    %` .-" `.
              /      \\    .: :.     /      \\
              '-..___|_..=:` `-:=.._|___..-'
                      (ALL FOR ONE)""")
        input()
        print(dedent("""
            You notice the other person in the painting.
            They're wearing a red and blue suit.
            Their eyes are sunken, and he looks skeletal."""))
        input()

        PaintingTwo.sucked_in()

        return 'my_hero'

class MHA(Scene):
    """This is the path for painting #2, i.e. the My Hero Academia painting"""
    def enter(self):

        Yes = ['Y', 'y', 'Yes', 'yes']
        No = {'N', 'n', 'No', 'no'}


        print(dedent("""
            You land face first.
            You stand up and compose yourself."""))

        input()
        print("On the floor, you also notice a bag of money.")

        input()
        print(dedent("""
            ──────────────────██████────────────────
            ─────────────────████████─█─────────────
            ─────────────██████████████─────────────
            ─────────────█████████████──────────────
            ──────────────███████████───────────────
            ───────────────██████████───────────────
            ────────────────████████────────────────
            ────────────────▐██████─────────────────
            ────────────────▐██████─────────────────
            ──────────────── ▌─────▌────────────────
            ────────────────███─█████───────────────
            ────────────████████████████────────────
            ──────────████████████████████──────────
            ────────████████████─────███████────────
            ──────███████████─────────███████───────
            ─────████████████───██─███████████──────
            ────██████████████──────────████████────
            ───████████████████─────█───█████████───
            ──█████████████████████─██───█████████──
            ──█████████████████████──██──██████████─
            ─███████████████████████─██───██████████
            ████████████████████████──────██████████
            ███████████████████──────────███████████
            ─██████████████████───────██████████████
            ─███████████████████████──█████████████─
            ──█████████████████████████████████████─
            ───██████████████████████████████████───
            ───────██████████████████████████████───
            ───────██████████████████████████───────
            ─────────────███████████████────────────"""))

        input()
        print("There's a sign next to it that says 'Free Gift!'")

        money = "100,000 ₩ (KRW)"
        while True:
            print(f"Do you pick it up {Player.name}?")
            pick_up_money = input(">")

            if pick_up_money in Yes:
                input(f"\nGood choice {Player.name}.")
                Player.items.append(money)
                print("\nYou got some money (KRW)!")
                plays("item.wav")
                input(f"\nItems:\n{Player.items}")
                input()
                break
            elif pick_up_money in No:
                print("\nYou decide to leave it there because you aren't sure if it's a trap.")
                input()
                break
            else:
                MHA.learn_to_type()

        print(dedent("""
            You suddenly hear yelling.
            You scan the area and see the person with a disfigured face.
            They are being blown away by the punch of a person with a disfigured arm.
            You instantly put together that this is All Might defeating All For One."""))
        plays("smash.wav")
        input()

        print(dedent("""
            As you realize what's happening, you're blown away from the shockwave.
            You find your fall broken by some trash bags under a small building.
            You decide to let the rest of the chapter from the manga play out."""))
        input()

        print(dedent("""
            You look at the sign of the building that you landed near.
            It says "PURIE" and there's a pleasant smell coming from it.
            You decide to go in since the fight outside is settled."""))
        input()

        print(dedent("""
            You are greeted by the nicest family of sisters.
            You see that they sell jams and perfumes.
            It seems business is slow today, probably due to the fight."""))
        input()

        print("They offer to sell you some jam at a discount.")
        input()

        while True:
            if money in Player.items: #If you took the bag of money...
                jam = input(f"Do you want to buy some {Player.name}?\n>")

                if jam in Yes: #...and you decide to buy some jam...
                    input(f"\nGood choice {Player.name}.")
                    Player.items.pop()

                    coco = 'Coconut Jam'
                    rose = "Rose Jam"
                    wine = "Wine Jam"
                    mango = "Mango Jam"

                    print(dedent(f"""
                        You sample a few different jams, for free!
                        You buy your favorites and some as a gift for those back home.
                        It comes out to exactly {money}, nice!"""))

                    Player.items.extend((coco, rose, wine, mango))
                    input()

                    print("\nYou got some amazing jams!")
                    plays("item.wav")
                    input(f"\nItems:\n{Player.items}")

                    print(dedent("""
                        The Jam Fam thanks you for your patronage.
                        They give you a gift as 'service'.
                        Apparently, they've connects in the airline industry."
                        It's a flight ticket home!"""))
                    input()

                    print(f"Nice!\nYou instantly go home {Player.name} ✈ !")
                    return 'finished' #...You win the game!

                elif jam in No: #...and you decide not to buy the jam...
                    print(dedent("""
                        You decide to be greedy and hoard your money.
                        Not only does this have a negative effect on the economy, you also are hungry!
                        You leave the cozy store in search of food and a way back home."""))

                    Player.items[:] = []
                    input()

                    print("You never find a way back home and eventually starve to death.")
                    input()
                    return 'death' #...You die :(

                else:
                    MHA.learn_to_type()

            elif money not in Player.items: #You didn't take the money...
                jam = input(f"Do you want to buy some {Player.name}?\n>")
                if jam in Yes: #...and you try to buy the jam with any money...
                    print(dedent("""
                        You check your pockets...you don't have any money!
                        You realized you should've grabbed that free money...
                        The staff smiles, they are so nice.
                        They give you a few free samples before you leave."""))

                    Player.items[:] = []
                    input()

                    print("You wander around and never find a way back home and eventually starve to death.")
                    input()
                    return 'death' #...You die :(

                elif jam in No: #...or you decide not to buy jam because you've no money
                    print(dedent("""
                        You know you don't have money, so you decline to save face.
                        Before leaving, the Jam Fam offers you some free samples.
                        They are so nice!"""))

                    Player.items[:] = []
                    input()

                    print("You wander around and never find a way back home and eventually starve to death.")
                    input()
                    return 'death' #...You die :(

                else:
                    MHA.learn_to_type() #learn_to_type and then restart the loop to ask the user what to do

            else:
                print("Somehow you broke the game; congrats!")
                return 'death'

class PaintingThree(Scene):
    """This is the path for painting #3 i.e. the start of smudged_painting"""
    def __init__(self, smudge):
        self.smudge = smudge

    def sucked_in():
        """This is the text for when you touch painting 3"""
        print(dedent("""
            You defy every sign you've ever seen at a museum and touch the painting.
            As soon as you do, you realize you've made a mistake."""))
        input()

    def enter(self):
        if PaintingThree.smudge == False:
            print(dedent("""
                You see the beautiful painting.
                There's a small, mustached plumber fighting a giant turtle-monster.
                You look further at the face of this chimera, noticing how ugly it is."""))
            input()

            print("""
        ───────▄█──────────█─────────█▄───────
        ─────▐██──────▄█──███──█▄─────██▌─────
        ────▐██▀─────█████████████────▀██▌────
        ───▐██▌─────██████████████─────▐██▌───
        ───████────████████████████────████───
        ──▐█████──██████████████████──█████▌──
        ───████████████████████████████████───
        ────███████▀▀████████████▀▀███████────
        ─────█████▌──▄▄─▀████▀─▄▄──▐█████─────
        ───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───
        ──██████████████████████████████████──
        ─████████████████████████████████████─
        ▐██████──███████▀▄██▄▀███████──██████▌
        ▐█████────██████████████████────█████▌
        ▐█████─────██████▀──▀██████─────█████▌
        ─█████▄─────███────────███─────▄█████─
        ──██████─────█──────────█─────██████──
        ────█████────────────────────█████────
        ─────█████──────────────────█████─────
        ──────█████────────────────█████──────
        ───────████───▄────────▄───████───────
        ────────████─██────────██─████────────
        ────────████████─▄██▄─████████────────
        ───────████████████████████████───────
        ───────████████████████████████───────
        ────────▀█████████▀▀█████████▀────────
        ──────────▀███▀────────▀███▀──────────""")
            input()

            PaintingThree.sucked_in()

            print(dedent("""
                You touching the painting smudged it.
                You have ruined the painting.
                You are filled with shame ☹ ."""))

            plays("shame.wav")
            input()

            print(dedent("""
                You quickly look around to see if anyone saw what you did.
                No one did because you remembered when the game that said, 'you wake up alone'.
                You quickly walk back to the middle of the room after this faux pas."""))

            #Change the painting to a smudged version so revisiting this room is updated to show correct painting
            PaintingThree.smudge = True

        else:
            print(dedent("""
                You see the smudged painting.
                You see your past mistake.
                The beautiful painting is now ruined."""))
            input()

            print("""
        ───────▄█──────────█──────────────────
        ─────▐██──────▄█──███──█▄─────────────
        ────▐██▀─────█████████████───────███──
        ───▐██▌─────███████████████──────███──
        ───████────█████████████████──────██──
        ──▐█████──███████████████────────████─
        ───█████████████████████────────████──
        ────███████▀▀███████████──────██████──
        ─────█████▌──▄▄─▀████▀─▄▄──▐█████─────
        ───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───
        ──██████████████████████████████████──
        ─████████████████████████████████████─
        ▐██████──███████▀▄██▄▀███████──██████▌
        ▐█████────██████████████████────█████▌
        ▐█████─────██████▀──▀██████─────█████▌
        ─█████▄─────███────────███─────▄█████─
        ──██████─────█──────────█─────██████──
        ────█████────────────────────█████────
        ─────█████──────────────────█████─────
        ──────█████────────────────█████──────
        ───────████───▄────────▄───████───────
        ────────████─██────────██─████────────
        ────────████████─▄██▄─████████────────
        ───────████████████████████████───────
        ───────████████████████████████───────
        ────────▀█████████▀▀█████████▀────────
        ──────────▀███▀────────▀███▀──────────""")
            input()

            print(dedent("""
                You are filled with shame again and wonder why you tried this painting again.
                You scurry back to the center room, hopefully remembering your choices."""))

        return 'what_direction'

class Mirror(Scene):
    """This is a false room. So enter() is basically sucked_in() + resetting you to the beginning of WhatDirection()"""
    def enter(self):
        print(dedent("""
            You get a running start and make towards a blank part of the wall.
            As you approach the wall, you push off the ground as hard as you can and jump.
            You say \"yahoo!\" for some reason and notice you jump higher than usual.""" ))
        plays("yahoo.wav")
        input()

        print(dedent("""
            You hit the mid-point of the wall and you immediately push off it.
            You realize you'll have enough force to reach the ceiling/mirror.
            You reach out to touch it, your fingers basically scraping it."""))
        input()

        print(dedent("""
            As your fingers touch the ceiling/mirror, it feels like a liquid.
            As soon as you do, you feel slingshot into the ceiling/mirror."""))
        plays("painting.wav")
        input()

        print(dedent("""
            You land, hard back on the carpeted floor in the middle of the first room.
            You see your familar paintings and stand up again, taking in this new info.
            You realize the ceiling isn't an exit, so maybe try picking a painting."""))
        input()

        return 'what_direction'

class Finished(Scene):
    def enter(self):
        """This is the message you get for finding a true ending."""
        input()
        print(f"""Congrats on finding one of the true endings in the game!
You made the right choices throughout the game and were able to end up here.
Clearly you showed empathy, courage, and altruism in this imaginary game.
Try playing the game again and discovering all 3 true endings!""")
        plays("ending.wav")

        input()
        print("Thank you for playing!")
        exit(0)

class Debug(Scene):
    def enter(self):
        """This is a debug message."""
        input()
        print(f"""Something went wrong. This is a debug message.""")
        exit(0)

class Map(object):

    scenes = {
    'test': Test(),
    'prank_screen': PrankScreen(),
    'welcome_screen': Welcome(),
    'start_room': StartRoom(),
    'what_direction': WhatDirection(),
    'painting1': PaintingOne(),
    'painting2': PaintingTwo(),
    'painting3': PaintingThree('smudge'),
    'mirror' : Mirror(),
    'attack_on_titan' : AOT(),
    'my_hero': MHA(),
    'death': Death(),
    'finished': Finished(),
    'debug': Debug()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name): #next_scene reads from the dict Scenes and then calls that Class
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

PaintingThree.smudge = False #This sets the initial state of the painting as unsmudged.
                             #This will be changed later if the user visits this painting
a_map = Map('prank_screen')
a_game = Engine(a_map)
a_game.play_game()
