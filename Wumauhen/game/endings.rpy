label choose_ending:
    narrator "It’s finally the day of the summer festival. Do you have a date to go with?"

    if max(wu_score, mauh_score, n_score) <= 0:
        call ending_single from _call_ending_single

    else:
        menu:
            "Wu" if wu_score == max(wu_score, mauh_score, n_score):
                call ending_wu from _call_ending_wu
            "Mauh" if mauh_score == max(wu_score, mauh_score, n_score):
                call ending_mauh from _call_ending_mauh
            "N" if n_score == max(wu_score, mauh_score, n_score):
                call ending_n from _call_ending_n
            "All three" if wu_score == mauh_score and mauh_score == n_score:
                call ending_women from _call_ending_women

    return

label ending_wu:
    scene bg festival with fade
    play music "audio/Wu's Ending/soft jazz bgm.mp3"
    show wu at bounce, center with dissolve

    wu "I would say I'm flattered, but I am the most eligible, aren't I?"
    player "There’s no other person I could spend the festival with."
    show wu blush at bounce
    wu "You flatter me."
    show wu kimono
    narrator "In very expensive silk clothing, provided by Wu’s multi-level-marketing pyramid scheme Chaebol inheritance, you both walk hand-in-hand through the festival booths."
    
    show wu kimono at bounce, center
    wu "Pick anything, i'll pay for it."
    player "(Wow, it seemed like only 15 real-life minutes ago that I was worrying about being single for the rest of my life… and being hit by a truck. Hey, are we still glossing over that?)"
    scene bg kabedon_before with fade
    narrator "You and Wu go through the stalls, eat delicious candies, play carnival games, and enjoy the atmosphere.\nSuddenly, Wu pulls you aside in between booths."
    player "Woah!"
    narrator "You close your eyes, startled by the abrupt pull, thinking you might tumble down."
    play music "audio/Wu's Ending/Wu.mp3"
    scene bg kabedon with vpunch
    wu "Don't fall, [YN]."
    narrator "Wu is kabedoning you against the wall, except… she’s using her leg instead of her arm..?"
    wu "I thought you might need a break from the environment, and I've been meaning to do this the entire night..."
    narrator "Wu leans in, and you stand there flustered…\n      Leaning in…\n            Ever so slightly.."
    narrator "Kissing scenes are unlocked if you subscribe to our Patreon! Thanks for playing!"

    return

label ending_mauh:
    scene bg festival with fade
    play music "audio/Mauh's Ending/upbeat bgm.mp3"
    show mauh happy at bounce, center with dissolve

    mauh "Oh, oh really.. Me?!"
    narrator "Mauh looks extremely ecstatic that you have chosen her."
    player "You were always kind to me from the beginning. This was the only logical choice."
    show mauh happy at bounce, center
    mauh "Ah, [YN], I’m so over the moon!"
    narrator "You and Mauh go hand-in-hand through the festival. It’s a full moon tonight, and the night sky is clear save for some bright, twinkling stars."
    show mauh at bounce, center
    mauh "I heard there were going to be fireworks tonight, [YN]!\nAnd with such a clear sky, we’ll be able to see it from anywhere."
    player "Seems so. Maybe we should get a little away from the crowd, though?"
    narrator "Mauh seems to have thought the same thing."
    show mauh at bounce, center
    mauh "I know just the spot, actually."
    narrator "Mauh leads you toward a clearing, with only a few couples loitering about. She seems to be a little nervous regarding something though."
    player "Hey, everything alright?"
    show mauh flustered at bounce, center
    mauh "Yeah, of course.. It’s just that.. With this setting, it’s almost perfect for.."
    play sound "audio/Mauh's Ending/fireworks.mp3"
    scene bg fireworks
    show mauh flustered
    narrator "The fireworks seem to go off instantly, surprising you both."
    player "Sorry, the fireworks cut you off. What were you trying to say?"
    
    stop sound fadeout 1.0
    narrator "It looks like Mauh takes a deep breath before carefully considering what she is going to say to you\n…"
    show mauh flustered at shake, center
    stop music fadeout 1.0
    mauh "The- the thing is..!\n            I’ve actually been interested in you for a long time…!"
    narrator "There’s a foreboding feeling in your gut.."
    mauh "[YN]... I-.. I’ve been your fan forever!"
    narrator "With aggravated motions, Mauh seems to pull out a multitude of items!"
    play music "audio/Mauh's Ending/Mauh.mp3"

    scene bg otaku with vpunch
    mauh "Please accept my love!!"
    player "Oh my god.\n(If the truck didn’t kill me already, this would’ve done it.)"
    narrator "YOU WIN!\n                               ({size=-8}…? Do we count this as a win..?{/size})"

    return

label ending_n:
    scene bg festival with fade
    play music "audio/N's Ending/murmurs.mp3"
    show n blush at center with dissolve

    n "… ({i}looks fond{/i})"
    player "Thanks for going with me to the summer festival…"
    n "…"
    player "Should we go to the ferris wheel?"
    n "… ({i}nods{/i})"
    narrator "You and N walk, closely together, towards the ferris wheel."
    
    scene bg wheel with fade
    show n blush at center with dissolve
    player "They say something special happens at the top of the ferris wheel. Can you believe that?"
    n "…"
    narrator "You and N board the cart in the ferris wheel. It’s a silent ride up, but the silence is not unwelcome."
    n "…"
    player "…"
    narrator "You reach the top of the ferris wheel, and your cart stops."
    player "…"
    n "…"
    player "… Guess there’s not really a surprise, huh? The view is pretty nice here though."
    n "…"
    player "I’m glad, at least, that I went to the festival with you."
    n "…"
    narrator "Your knees are touching, and you are extremely close to N’s face."
    player "({i}Leaning in{/i})"
    n "…"
    
    scene bg_white with fade

    player "What…!"
    narrator "Everything seems to disappear around you. Your vision is only filled with pure white."
    scene bg angel with vpunch
    play music "audio/N's Ending/N.mp3" volume 1.20
    n "{font=Wingdings-Regular-Font.otf}Thank you, [YN]."
    player "Huh..?"
    n "{font=Wingdings-Regular-Font.otf}Despite our differences in communication, you took the chance with me. This - I am more than willing to reveal myself to you."
    player "Woah woah woah…"
    n "…"
    n "{font=Wingdings-Regular-Font.otf}Do you still accept me?"

    narrator "Do you accept or reject the extraterrestrial being?"

    menu:
        "Accept":
            n "{font=Wingdings-Regular-Font.otf}Thank you. In this age, it is hard not to be judged by out identities. By accepting me, I will accept you into a realm above."
            narrator "You take N’s… hand..? ..Wings..? Whatever it is, you take it, and N leads you above."
            narrator "You have ascended into godhood."

        "Reject":
            n "{font=Wingdings-Regular-Font.otf}A shame. It seems that you are only human after all."
            stop music fadeout 1.0
            narrator "The scene fades to black, and you are back in your hospital bed."
            narrator "You have returned to reality."


    return

label ending_single:
    scene bg single with fade
    play music "audio/Single Ending/LOLURSINGLE.mp3" volume 0.85
    narrator "You.. you didn’t bag anyone..?"
    narrator "That’s probably more impressive than bagging all of them at the same time…"
    narrator "Well, congratulations, I guess. You’re single."
    play sound "audio/Single Ending/clapping.mp3"
    show single_mauh at center with dissolve
    mauh "Congratulations!"
    show single_wu at center with dissolve
    wu "Congratulations!"
    show single_n at center with dissolve
    n "… ({i}celebratory{/i})"
    narrator "Congratulations.. you.. Are a strong independent woman..?"

    return

label ending_women:
    play music "audio/Women Ending/triumphant bgm.mp3" volume 0.85
    narrator "You.. You really are a womanizer!"
    narrator "Not one, but all three of them!"
    narrator "I really didn’t think you had it in you…"
    player "(What’s that supposed to mean??)"
    narrator "Well, I guess, here you go. Since you got her fair and square."
    
    show woman with fade
    play sound "audio/Women Ending/WOW.mp3"
    show woman at bounce
    wumauhn "You did it, [YN], you won THE woman!"
    player "What."
    show woman at bounce
    wumauhn "See, maybe you didn’t realize it all along, but despite all of our individual characters’ differences, we are all women in the end! And isn’t that wonderful, the power of womanhood!"
    player "What.."
    show woman at bounce
    wumauhn "Thank you for choosing us, [YN]! ♡"
    scene bg woman with fade
    narrator "Woman!"

    return