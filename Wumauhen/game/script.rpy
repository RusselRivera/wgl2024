﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# , what_outlines=[(2, "#444444", 0, 0)], what_color="#ffffff"

define player = Character("{color=#1E1E1E}[[[YN]]{/color}", what_size=32)
define narrator = Character(color="#1E1E1E")
define wu = Character("[[Wu]", color="#D362A4", what_font="great_vibes.ttf", what_size=50, who_outlines=[(1, "#444444", 0, 0)])
define mauh = Character("[[Mauh]", color="#FF9A56", who_outlines=[(1, "#444444", 0, 0)])
define n = Character("[[N]", color="#000000")
define wumauh = Character("[[Wu and Mauh]")
define wun = Character("[[Wu and N]]")
define wumauhn = Character("[[WuMauhN]")

image wu = DynamicDisplayable(bwImage, "characters/wu.png")
image mauh = DynamicDisplayable(bwImage, "characters/mauh.png")
image wu mic = DynamicDisplayable(bwImage, "characters/wu mic.png")
image mauh tear = DynamicDisplayable(bwImage, "characters/mauh tear.png")

image single_wu = DynamicDisplayable(bwImage, "props/single_wu.png")
image single_mauh = DynamicDisplayable(bwImage, "props/single_mauh.png")
image single_n = DynamicDisplayable(bwImage, "props/single_n.png")

image bg woman = DynamicDisplayable(bwImage, "backgrounds/bg_woman.png")
image bg fireworks = DynamicDisplayable(bwImage, "backgrounds/bg_fireworks.png")
image bg credits = DynamicDisplayable(bwImage, "backgrounds/bg_credits.png")
image bg single = DynamicDisplayable(bwImage, "backgrounds/bg_single.png")
image bg angel = DynamicDisplayable(bwImage, "backgrounds/bg_angel.png")
image bg karaoke = DynamicDisplayable(bwImage, "backgrounds/bg_karaoke.png")
image bg otaku = DynamicDisplayable(bwImage, "backgrounds/bg_otaku.png")
image bg beach = DynamicDisplayable(bwImage, "backgrounds/bg_beach.png")
image bg black = DynamicDisplayable(bwImage, "backgrounds/bg_black.png")
image bg classroom = DynamicDisplayable(bwImage, "backgrounds/bg_classroom.jpg")
image bg kitchen = DynamicDisplayable(bwImage, "backgrounds/bg_kitchen.jpg")
image bg road = DynamicDisplayable(bwImage, "backgrounds/bg_rutgers.png")
image bg sakura = DynamicDisplayable(bwImage, "backgrounds/bg_sakura.png")
image bg volleyball = DynamicDisplayable(bwImage, "backgrounds/bg_volleyball.png")
image bg kabedon = DynamicDisplayable(bwImage, "backgrounds/bg_kabedon.png")
image bg white = DynamicDisplayable(bwImage, "backgrounds/bg_white.png")
image bg chocolate = DynamicDisplayable(bwImage, "backgrounds/bg_chocolate.png")
image bg wheel = DynamicDisplayable(bwImage, "backgrounds/bg_wheel.png")
image bg rain = DynamicDisplayable(bwImage, "backgrounds/bg_rain.png")
image bg festival = DynamicDisplayable(bwImage, "backgrounds/bg_festival.png")
image bg kabedon_before = DynamicDisplayable(bwImage, "backgrounds/bg_kabedon_before.png")

init python:
    no_counter = 0
    no_vals = [
        "This option is unavailable. Choose another option.",
        "Did you read it the first time? This isn’t a viable option. Choose another.",
        "Damn I’m just going to pick for you at this point.",
        "Can you please just play the game.",
        "I am going to start a tantrum.",
        "..."
    ]

    flag_perfect = True
    saturation = 1.0
    wu_done = False
    wu_score = 0

    mauh_done = False
    mauh_score = 0

    n_done = False
    n_score = 0

    flag_trash = False

    YN = "???"

    day = -1

    day_word = ["first", "second", "third"]

    def moveColor():
        global saturation
        while saturation < 1:
            renpy.pause(.01)
            saturation += .1

    def moveBW():
        global saturation
        while saturation > 0:
            renpy.pause(.01)
            saturation -= .1


    def bwImage(st,at,path):
        return im.MatrixColor(Image(path),im.matrix.saturation(saturation)),None

    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    Shake = renpy.curry(_Shake)

transform shake:
    yoffset 0
    linear .05 xoffset -6
    linear .05 xoffset 0
    yoffset 0
    repeat


transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform spotlight:
    xalign 0.20 yalign 0.0

transform ball_hit:
    easein .175 yoffset -1000 xoffset -1000

transform audience_l:
    xalign 0.70 yalign 0.0

transform audience_m:

    xalign 1.0 yalign 0.0
transform audience_m2:
    xalign .85 yalign 0.0

transform audience_r:
    xalign 1.20 yalign 0.0

# The game starts here.

label start:
    # These display lines of dialogue.
    # call ending_women from _call_ending_women_1
    # call ending_single from _call_ending_single_1
    # call ending_wu from _call_ending_wu_1
    # call ending_mauh from _call_ending_mauh_1
    # call ending_n from _call_ending_n_1

    call intro from _call_intro

    call wake_up from _call_wake_up
    call wake_up from _call_wake_up_1
    call wake_up from _call_wake_up_2

    call choose_ending from _call_choose_ending
    scene bg credits

    return

label wake_up:
    window auto
    stop music fadeout 1.0
    scene bg_black with fade

    $ day += 1

    narrator "The [day_word[day]] day comes. Who will you spend your [day_word[day]] day with?"

    menu:
        "Wu" if not wu_done:
            call wu_day from _call_wu_day
        "Mauh" if not mauh_done:
            call mauh_day from _call_mauh_day
        "N" if not n_done:
            call n_day from _call_n_day

    return

