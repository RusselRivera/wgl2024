label intro:
    scene bg road
    play music "audio/Intro/upbeat bgm.mp3"

    player "Wow. I am so lonely. Wish I had a woman."

    narrator "OH ████ A TRUCK!"

    play sound "audio/Intro/truck-kunc.mp3"

    show truck at center with vpunch 

    scene bg_black with fade

    narrator "You blearily open your eyes."

    scene bg classroom with fade

    narrator "The heck?"

    $ wu.name = "[[???]"
    $ mauh.name = "[[???]"
    $ n.name = "[[???]"

    show mauh at shake, center with dissolve
    mauh "Oh!!! {image=props/ru.png} ok??!"

    player "hey.. Am i ok..? ({i}I just got hit by a truck...{/i})"
    show mauh at right with move

    show wu at bounce, center with dissolve
    wu "{size=-18}{font=DejaVuSans.ttf}Nah bruv u goodie … oops. What I meant was… "

    play sound "audio/Intro/sparkly.mp3"

    wu "You're fine now."

    $ moveBW()
    show n at left with dissolve
    n "…"
    $ moveColor()


    mauh "Hey, anyways, glad you’re awake, um, err, sorry, I’m forgetting your name!"

    $ YN = renpy.input("What is your name?", length=32)
    $ YN = YN.strip()

    play sound "audio/Intro/general gasp.mp3"
    show mauh at bounce
    mauh "Hey, anyways, glad you’re awake [YN]. You weren’t paying attention, but the school summer festival is in 3 days!"


    player "({i}The heck is she talking about… Hey… I just got hit by a truck!!!{/i})"

    show mauh at bounce
    mauh "[YN]… do you have a date to go with?"

    player "No…"

    show mauh at bounce
    play sound "audio/Intro/mauh gasp.mp3"
    mauh "GASP!"

    
    show wu at bounce
    play sound "audio/Intro/wu gasp.mp3"

    wu "Gasp!"

    play sound "audio/Intro/cricket.mp3" volume 0.6
    n "…"
    
    stop sound fadeout 1.0
    show n at shake
    show mauh at shake
    show wu at shake
    mauh "[YN]…! You have to find a date for the summer festival…! Or else…!"

    player "({i}Or else what…?{/i})"

    play music "audio/Intro/kahoot.mp3"

    call q_find_date from _call_q_find_date

    play music "audio/Intro/upbeat bgm.mp3"

    $ wu.name = "[[Wu]"
    $ mauh.name = "[[Mauh]"

    show n at left
    show wu at center
    show mauh at right

    show mauh at bounce
    mauh "Great! Oh, and oops (character shake), I forgot to introduce myself silly me. I’m Mauh, your friendly neighborhood happy-go-lucky popular girl! And this is..."

    show wu at bounce
    wu "Pleased to make your acquaintance. You're looking rather lovely today [YN]"

    player "({i}Hey!! Let’s not forget I just got hit by a truck…?!?{/i})"

    show mauh at bounce
    mauh "And lastly…"

    $ moveBW()
    n "…"

    player "Does she (they…? it…?)… talk?"

    n "... ({i}nods{/i})"

    player "...?"
    $ moveColor()

    show mauh at bounce
    mauh "That’s N. And that’s the three of us!"
    
    $ n.name = "[[N]"

    player "Er.. wait, she didn’t even-"

    play sound "audio/Intro/school bell.mp3"

    show wu at bounce
    wu "Ah, there's the bell. We should probably go home now. Or else..."
    stop sound fadeout 1.0

    player "({i}Or else what?!?!? Why the heck isn’t anyone explaining anything?!{/i})"

    show mauh at bounce
    mauh "Wow, it feels like {i}{b}{u}{color=#f00}I’ve been hit by a truck{/color}{/u}{/b}{/i} with how fast the day went! Well, alright, see you guys tomorrow!"

    player "Haha, that’s funny, because I also-!"

    show wu at bounce
    wu "See ya'."

    n "… ({i}tilting her head as a sign of goodbye{/i})"

    show mauh at bounce
    mauh "And don’t you forget, [YN], 3 days to find a date for the summer festival…"

    player "({i}Someone save my soul…{/i})"

    narrator "The scene fades to black."

    return

label q_find_date:
    menu:
        "Shrug and go along with it, \"OK\"":
            return

        "Shake your head, \"I don’t think I want to\"":
            narrator "[no_vals[no_counter]]"
            $ no_counter = min(5, no_counter + 1)
            call q_find_date from _call_q_find_date_1

            return