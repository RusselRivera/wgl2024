# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character(color="1E1E1E")
define narrator = Character(color="1E1E1E")
define wu = Character("wu", color="000000", what_font="great_vibes.ttf")
define mauh = Character("mauh", color="000000")
define n = Character("n", color="000000")

image bg road = DynamicDisplayable(bwImage, "backgrounds/bg_road.png")

init python:

    saturation = 1.0

    wu_done = False
    wu_score = 0

    mauh_done = False
    mauh_score = 0

    n_done = False
    n_score = 0

    YN = "DRAAAAVEN"

    day = 0

    day_word = ["first", "second", "third"]

    def bwImage(st,at,path):
        return im.MatrixColor(Image(path),im.matrix.saturation(saturation)),None

# The game starts here.

label start:
    # These display lines of dialogue.

    call wake_up
    call intro

    call wake_up
    call wake_up
    call wake_up

    return

label wake_up:
    narrator "The [day_word[day]] day comes. Who will you spend your [day_word[day]] day with?"
    menu:
        "Wu" if not wu_done:
            call wu_day
        "Mauh" if not mauh_done:
            call mauh_day
        "N" if not n_done:
            call n_day

    return

label intro:
    scene bg road

    player "Wow. I am so lonely. Wish I had a woman."

    narrator "OH ████ A TRUCK!"

    show truck at left with vpunch 

    scene bg_black with fade

    narrator "You blearily open your eyes."

    scene bg road with fade

    narrator "The heck?"

    $ wu.name = "???"
    $ mauh.name = "???"
    $ n.name = "???"

    show mauh at center with dissolve
    mauh "Oh!!! {image=props/ru.png} ok??!"

    player "hey.. Am i ok..? ({i}I just got hit by a truck...{/i})"
    show mauh at right with move

    show wu at center with dissolve
    wu "{font=DejaVuSans.ttf}Nah bruv u goodie … oops. What I meant was… "
    wu "You're fine now."
    show wu at left with move

    $ saturation = 0
    show n at center with dissolve
    n "…"
    $ saturation = 1

    mauh "Hey, anyways, glad you’re awake [YN]. You weren’t paying attention, but the school summer festival is in 3 days!"

    player "({i}The heck is she talking about… Hey… I just got hit by a truck!!!{/i})"

    mauh "[YN]… do you have a date to go with?"

    player "No…"

    mauh "GASP!"

    wu "Gasp!"

    n "…"

    mauh "[YN]…! You have to find a date for the summer festival…! Or else…!"

    player "{i}Or else what…?{/i})"

    call q_find_date

    $ wu.name = "Wu"
    $ mauh.name = "Mauh"

    mauh "Great! Oh, and oops (character shake), I forgot to introduce myself silly me. I’m Mauh, your friendly neighborhood happy-go-lucky popular girl! And this is..."

    wu "Pleased to make your acquaintance. You're looking rather lovely today [YN]"

    player "({i}Hey!! Let’s not forget I just got hit by a truck…?!?{/i})"

    mauh "And lastly…"

    n "…"

    player "Does she (they…? it…?)… talk?"

    n "... ({i}nods{/i})"

    player "...?"

    mauh "That’s N. And that’s the three of us!"
    
    $ n.name = "N"

    player "Er.. wait, she didn’t even-"

    narrator "Ding dong!"

    wu "Ah, there's the bell. We should probably go home now. Or else..."

    player "({i}Or else what?!?!? Why the heck isn’t anyone explaining anything?!{/i})"

    mauh "Wow, it feels like {i}{b}{u}{color=#f00}I’ve been hit by a truck{/color}{/u}{/b}{/i} with how fast the day went! Well, alright, see you guys tomorrow!"

    player "Haha, that’s funny, because I also-!"

    wu "See ya'."

    n "… ({i}tilting her head as a sign of goodbye{/i})"

    mauh "And don’t you forget, [YN], 3 days to find a date for the summer festival…"

    player "({i}Someone save my soul…{/i})"

    narrator "The scene fades to black."

    return

label q_find_date:
    menu:
        "Shrug and go along with it, “OK”":
            return

        "Shake your head, “I don’t think I want to":
            narrator "This option is unavailable. Choose another option."
            call q_find_date

            return
