
label wu_day:
    scene bg kitchen with fade
    
    show n at left
    show wu at center
    show mauh at right

    play music "audio/Wu's Storyline/soft jazz bgm.mp3"

    narrator "It’s during school hours. You are in culinary class with Wu, Mauh, and N. Wu is insisting, even though it is nowhere near February, that you all practice your chocolatier skills for Valentine’s Day."
    
    show wu at bounce
    wu "My favorite holiday, you ask? Of course, Valentine's day! What is more beautiful than a day dedicated to celebrating your loved one?"
    show mauh at bounce
    mauh "Though it’s definitely not my favorite… I can’t disagree!"
    n "… ({i}nodding enthusiastically{/i})"
    show wu at bounce
    wu "[YN], what do you think?"

    menu:
        "\"I'd have to agree with you Wu!":
            show wu at bounce
            wu "Lovely!!~ I knew you'd feel the same."
            $ wu_score += 1
        "\"Eh… I don’t really care for stuff like that…\"":
            show wu at bounce
            wu "Ah, I guess you're entitled to your own opinions..."
            $ wu_score -= 1
            $ flag_perfect = False

    show mauh at bounce
    mauh "Well, I guess we should get chocolatier-ing!"
    n "…"
    narrator "Commencing an awesome, off-screen cooking scene!"

    play music "audio/Wu's Storyline/chaos.mp3" 

    scene bg chocolate with vpunch
    mauh "Hey, a little help over here!"
    n "!!!"
    wu "Oh jeez louise, the oven's on fire!"
    player "({i}What is going on…{/i})"

    show n choc at left with dissolve
    show wu choc1 at center with dissolve
    show mauh choc_sad at right with dissolve
    
    play music "audio/Wu's Storyline/soft jazz bgm.mp3" fadeout 1.0 fadein 1.0
    show mauh choc_sad at bounce
    mauh "Oh wow.. I really suck at this don’t I? Oh well…"
    show wu choc1 at bounce
    wu "It's ok Mauh, you can have mine."
    show mauh choc_happy at bounce
    show wu choc
    mauh "Really!! Oh Wu, you’re always the best!"
    show wu at bounce
    wu "Good try N. Though, I'm not sure what we'll be doing with that..."
    show mauh choc_happy at bounce
    mauh "What about yours, [YN]?"
    narrator "You hold up a normal piece of chocolate. Not as beautiful as Wu’s, but definitely not as dangerously radioactive as N’s."
    show wu at bounce
    show mauh choc_happy at bounce
    wumauh "Not bad!!"
    n "…!"
    narrator "The thing is, you’re pretty hesitant to try this. What if you’ve been stuck in a coma or something and this will choke your last remaining breath out of you? You decide not to risk it."
    
    menu:
        "Give it to Wu, who has no chocolate":
            show wu choc1 at bounce
            wu "Oh my! For me, really?"
            narrator "You nod, insistent.\nWu looks genuinely taken aback, and a slight blush creeps up her ears."
            show mauh choc_happy at bounce
            mauh "How kind of you [YN]!!"
            narrator "You all continue to eat your respective chocolates, the scene fading to black."
            $ wu_score += 1

        "Give it to N, who has no chocolate":
            n "…!"
            player "Since yours didn’t go so well… you can have mine."
            show n blush
            n "… ({i}flushed{/i})"
            show mauh choc_happy at bounce
            mauh "What a generous soul!"
            show wu at bounce
            wu "Oh, N, I would've given you some of mine too!"
            n "… ({i}shaking her head, indicating it is ok{/i})"
            narrator "You all continue to eat your respective chocolates, the scene fading to black."
            $ n_score += 1

        "Secretly throw it in the trash later":
            narrator "They all continue to eat their respective chocolates."
            narrator "Later, Wu comes up to you as everyone is leaving the classroom."
            show wu at bounce
            wu "Now I wouldn't usually say something, but what a waste."
            player "…!"
            show wu at bounce
            wu "Maybe give it to someone who wants it next time... no matter how bad it is!"
            player "Right, sorry…"    
            play sound "audio/Wu's Storyline/womp womp.mp3"
            narrator "You seem to have rubbed on Wu the wrong way. It’s best to be weary of your actions. The scene fades to black."


            $ wu_score -= 1
            $ flag_perfect = False
            $ flag_trash = True

    scene bg sakura with fade
    show n at right
    show wu at left
    show mauh at center
    narrator "A bit after school, you, Mauh, and N catch wind of a confession happening under the cherry blossom tree in the school yard. All three of you hide behind the wall corner, peeking out ever so slightly."
    narrator "Wu is confronted by a shorter, non-visible student who seems to be flustered and stammering in front of her."
    show mauh at bounce
    mauh "No way! Someone is confessing to Wu again?!"
    n "…"
    player "({i}Again..?{/i})"
    show mauh at bounce
    mauh "If I’m popular, then Wu is definitely popularEST! Her charm and wit outmatch any other girl in this school! Even I had a crush on Wu once."
    player "{i}(Does heterosexuality not exist in this world…? Wait a minute, I haven’t seen a single man!){/i}"
    n "… ({i}vigorously nodding{/i})"
    player "It seems like the confession is taking quite some time…"
    narrator "Actually, it’s been 2 hours. Behind the unnamed girl, you realize, is a line of ten more girls. At least of what you can see around the corner."
    show mauh at bounce
    mauh "Ah.. yeah.. This is usually how it goes…"

label disrupt:
    menu:
        "Disrupt the crowd and pull Wu away.":
            if flag_trash:
                "This option is locked!"
                jump disrupt
            hide n with dissolve
            hide mauh with dissolve
            show wu at center with move

            narrator "Rushing out of the corner, you march right up to Wu as the girl in front of her continues to stutter {i}“I… I.. always.. I always.. Always… I.. I{/1}”"
            player "Wu, let’s get out of here!"
            show wu hand at bounce
            wu "Oh! Huh?!"
            narrator "With Wu’s hand in yours, you rush somewhere else away from the scene. It is just you two now."
            show wu hand at bounce
            wu "What are you doing, [YN]?"

            menu:
                "\"I can’t stand to see someone else confessing to you.\"":
                    show wu hand_flustered at bounce
                    wu "Oh. ({i}flustered{/i})"
                    narrator "Your hand stays adamantly gripped to Wu’s.\nWu smiles." 
                    show wu hand_flustered  at bounce
                    wu "You should've said so in the first place, honey."
                    narrator "Wu grips your hand back."
                    show wu hand_flustered  at bounce
                    wu "Let's go home then, shall we?"
                    narrator "You both head back to where Mauh and N are."

                    $ wu_score += 1

                "\"We’ve been waiting for two hours. It’s time to go now.\"":
                    show wu hand at bounce
                    wu "Ah, I see.\n...\n It's still important for every woman to be listen to, fully."
                    narrator "Wu looks slightly distraught that you had interrupted her. But, she realizes her friends have been waiting for her, and nods her head resolutely.\nYou both head back to where Mauh and N are."

                    $ wu_score -= 1
                    $ flag_perfect = False
                    
        "Stand and wait for 2 more hours.":
            narrator "The street lamps are starting to turn on now. As the last remaining girls get in their confessions, the three of you behind the corner creep out from your hiding place."
            show wu at bounce
            wu "Wow... all wonderful, passionate, independent women."
            show mauh at bounce
            mauh "Anyone catch your eye?"
            show wu at bounce
            wu "Once again, I prefer that these beautiful women explore the world before going for the most eligible bachlorette."
            n "… ({i}nodding, as if to say, how eloquently spoken!{/i})"
            narrator "…"
            narrator "The hours of the afternoon were pretty much put to waste. Unless you consider watching a line of confessions – like a KPop idol meet-and-greet – for 4 hours entertaining…"

    narrator "The day comes to a close, the scene fading to black."

    $ wu_done = True

    return


label mauh_day:
    scene bg beach with fade
    show n at left with dissolve
    show mauh at center with dissolve
    show wu at right with dissolve
    play music "audio/Mauh's Storyline/beach bgm.mp3"

    narrator "Despite you just arriving (consciously) here in less than a blink of an eye’s time, it seems that you’re already going on a field trip with everyone! And its… the beach? (Hey, how is this even possible..? That’s the sound of real waves..?!)"
    play sound "audio/Mauh's Storyline/ocean waves.wav" volume 0.8
    show mauh at bounce
    mauh "Wooh, it’s really warm out today! And the sea breeze feels nice on the skin!"
    player "({i}What..? We’re still in front of the chalk board..{/i})"
    show wu at bounce
    wu "I most definitely can't wait for golden hour on the beach… (She says, focused only on taking selfies)."
    n "…"

    scene bg volleyball with fade
    show n at left with dissolve
    show mauh at center with dissolve
    show wu at right with dissolve

    show mauh at bounce
    mauh "Why don’t we play some beach volleyball?"
    show n exclaim
    n "…! ({i}excitedly{/i})"
    show n
    show wu at bounce
    wu "Ohoh, willing to lose again?"
    show mauh at bounce
    mauh "W-well! This time we have [YN]! Surely we can’t lose!"
    player "({i}I should have a serious spinal injury by now…{/i})"
    show mauh at bounce
    mauh "See, [YN], the last time we did this… it was N and I against Wu. Because as the most eligible bachelorette and simultaneously also the best soccer player, the best baseball player, the best swimmer, the best basket weaver, the best-"
    narrator "This goes on for quite some time."
    show mauh at bounce
    mauh "..she’s also the best volleyball player! Even with the both of us, we couldn’t even get close to winning!"
    n "… ({i}in agreement{/i})"
    player "({i}So.. she a freak..?{/i})"
    show mauh at bounce
    mauh "It’s a good thing I brought a ball!"
    narrator "You four approach the empty beach volleyball courts. You really, really think maybe you shouldn’t be doing this after getting mauled by a 80 mp/h (in a pedestrian zone) truck."
    narrator "But hey! You have no idea where you are right now, so what’s the harm in playing some volleyball?"
    show wu at bounce
    wu "Here I come, girls~"
    narrator "Wu breathes in and out, with her eyes closed."
    narrator "Suddenly, she opens her eyes, lifts the ball into the air, and jumps with a running start.\nThe sound barrier breaks as she serves it right past your ear, just within the court lines."
    
    play sound "audio/Mauh's Storyline/serve.mp3"
    player "..What."
    show mauh at bounce
    mauh "EEK! There’s the killer serve!"
    show n scared
    n "… ({i}trembling{/i})"
    show wu at bounce
    wu "One point! Let's keep it going~!"
    narrator "This goes for quite a while. The current score is 24-3. Really, Wu’s just one point away, so you have to make this count (Not that you really have a chance after, anyway…)"
    show mauh at bounce
    mauh "Come on guys, it’s match point! We really have to give it our all here!"
    show n at ball_hit
    narrator "When Wu serves it to your side, N receives the ball.\nWith her head.\n…\nShe’s out cold now!"
    narrator "It’s headed towards your direction, and a very important deciding factor from here."

    menu:
        "Set it to Mauh!":
            $ mauh_score += 1
            narrator "…And time seems to slow down as you set it towards Mauh!"
            play music "audio/Mauh's Storyline/deep fried haikyuu.mp3"
            player "Mauh..!"
            show mauh happy at bounce
            mauh "I’ve got it [YN]!"
            narrator "It reaches Mauh, and she looks at you with gratitude. She goes to spike it over the net…"

        "Bump it over the net!":
            narrator "…And you decide to bump it over the net!"
            show mauh at bounce
            mauh "Naisu!"
            narrator "You three watch the ball go over from your side to across the netting, and…"

    narrator "Wu blocks the ball quickly by striking it back down onto your side of the net as if it were a third impact meteorite."
    
    if mauh_score > 0:
        play music "audio/Mauh's Storyline/beach bgm.mp3"
    play sound "audio/Mauh's Storyline/coach whistle.mp3"
    show wu at bounce
    hide n 
    wu "Nice try, ladies! That really was an exhausing match. (There is no visible sweat on her)"
    show mauh tired at bounce
    show n worry at left with dissolve
    mauh "Ah.. what a match.. At least we got to play with you this time, [YN]!"
    n ". . . ({i}still looking haggard{/i})"
    show wu at bounce
    wu "After all that strenuous activity, what say we all get some ice cream and enjoy the beach itself?"
    show mauh at bounce
    show n 
    mauh "I’d love to do that!"
    scene bg beach with fade
    narrator "You all decided to get some ice cream. (Again, where are we getting all of this stuff…?)\nOnce back at the edge of the shore, everyone seems to be doing their own thing."
    narrator "Wu is quite entertainingly occupied by burying N in the sand."
    show mauh at bounce
    mauh "Looks like they’re having fun."
    narrator "Say, why don’t we go help Wu out?"

    menu:
        "Sure, why not.":
            narrator "You and Mauh both crouch down onto the sand, trying to form the figure around N.:"
            player "(I still don’t even know how this is possible. Like, N isn’t even physically here for us to form a figure.. She’s literally a silhouette?)"
            narrator "You spent quite a bit of the rest of the evening doing this, because really, how would you form a sand figure around someone who isn’t in this physical, mortal realm?"
        "Let’s do something together, just you and me.":
            hide n with dissolve
            hide wu with dissolve
            show mauh flustered
            mauh "Oh! Really? (She looks flustered)"
            player "Yeah, we should…"

            menu:
                "Learn about Ren’Py.":
                    show mauh nervous at bounce
                    mauh "Oh, um, ok!"
                    narrator "You decide to explain to Mauh what Ren’Py is."
                    play music "audio/Mauh's Storyline/fitness gram.mp3"
                    player "Ren'Py is a visual novel engine – used by thousands of creators from around the world – that helps you use words, images, and sounds to tell interactive stories that run on computers and mobile devices. These can be both visual novels and life simulation games."
                    player "The easy to learn script language allows anyone to efficiently write large visual novels, while its Python scripting is enough for complex simulation games."
                    narrator "Ren'Py is open source and free for commercial use."
                    show mauh nervous at bounce
                    mauh "Wow, um.. Where do I get it?"
                    player "The latest official release of Ren'Py 8 is 8.3.3 \"Second Star to the Right\", released on November 15, 2024. Ren'Py 8 is recommended for all projects."
                    show mauh nervous at bounce
                    mauh "Oh that’s cool.. I guess! What happens if I speak another language?"
                    player "Ren'Py comes with a comprehensive, if complex, reference manual, also available in Japanese, Simplified Chinese, and Traditional Chinese."
                    player "{font=NotoSansJP.ttf}Ren'Py にバグを見つけたと思われる場合は、GitHub の問題追跡システムに報告してください。Ren'Py の開発に貢献したい場合は、GitHub プロジェクト ページにアクセスしてください。"
                    show mauh at bounce
                    mauh "Sugoi!"
                    narrator "This dialogue goes on for quite a while until you decide to meet back up with the other two."
                    stop music fadeout 1.0

                "Take a walk along the coast.":
                    $ mauh_score += 1
                    show mauh at bounce
                    mauh "Oh, I’d be more than happy to, with you, [YN]."
                    player "You and Mauh decide to take a leisurely stroll down the coast. The scenery is quite nice."
                    show mauh at bounce
                    mauh "I really appreciate you being with us here, [YN]. It feels like we’ve been friends forever, really."
                    player "Hmm.."
                    show mauh at bounce
                    mauh "Sometimes I get a little antsy about always being around Wu and N! I love them to death, but I gotta branch out sometimes, you know!"
                    player "Mhm…"
                    show mauh at bounce
                    mauh "And obviously they’re my friends, so, if I want to, maybe, find the love of my life, maybe I need to be looking elsewhere!"
                    player "Uhuh…"
                    show mauh at bounce
                    mauh "So really, I’m glad that it was you. Really glad."
                    player "Wow, um, thanks I guess. It’s really nice to be here with you too."
                    narrator "Mauh gives you one last smile, and you continue to walk down the path until you both enjoy a silence on the way back to the others."


    narrator "The day quickly comes to an end, as you all pack up your belongings and head home.\nThe scene fades to black."

    $ mauh_done = True
    return

label n_day:
    # scene bg 
    scene bg karaoke with fade
    show mauh at spotlight with dissolve
    show n at audience_l with dissolve
    show wu at audience_m with dissolve
    
    narrator "It’s after school hours. N has invited you as well as Wu and Mauh to the Karaoke club, in which N is an active member in."
    player "({i}So, logistically speaking.. How is that possible..?{/i})"
    play music "audio/N's Storyline/billie meow.mp3" noloop
    
    show mauh mic  at bounce
    mauh "~~~!"
    show wu at bounce
    wu "Wow, she's really good!"
    show mauh tired
    narrator "Mauh finishes her song, wiping a sweat drop off her forehead."
    play sound "audio/N's Storyline/clapping.mp3" 
    stop music fadeout 1.0
    n "…"

    menu:
        "\"N, you should go up and sing.\"":
            stop sound fadeout 1.0
            $ n_score += 1
            show n exclaim
            narrator "N looks at you in surprise, but not with any malice."
            show mauh at bounce
            mauh "Here N, take the mic!"
            show mauh at audience_l with move
            show n mic at spotlight with move
            narrator "N takes the mic."
            $ moveBW()
            # $ saturation = 0
            play sound "audio/N's Storyline/G note.mp3" 
            n "…\n      …\n            … ♪"
            show mauh tear at bounce
            mauh "Oh my god, N’s singing is so beautiful…"
            show wu at bounce
            wu "Absolutely breathtaking..."
            player "({i}Am I the only one hearing nothing…?{/i})"
            narrator "The song ends."
            show n
            play sound "audio/N's Storyline/clapping.mp3" 
            $ moveColor()
            show mauh tear at bounce
            mauh "That was so wonderful N!"
            n "… ({i}blushing{/i})"
            show mauh at bounce
            mauh "What did you think, [YN]?"

            menu:
                "\"It definitely reached somewhere in my heart.\"":
                    $ n_score += 1
                    show n blush
                    n "… ({i}flustered, appreciative{/i})"
                    show n
                "\"Nothing that great.\"":
                    $ n_score -= 1
                    $ flag_perfect = False
                    n "…"
                    show mauh at bounce
                    mauh "Come on now, I thought it was fantastic N."

            show n at audience_m2 with move

        "\"I’ll go up and sing!\"":
            show mauh at bounce
            mauh "Wow, really?! Sure, [YN], here’s the mic!"
            show wu at audience_r with move
            show n at audience_m2 with move
            show mauh at audience_l with move
            player "Here I go…"
            narrator "You take the mic."
            
            play music "audio/N's Storyline/terrible bgm.mp3" noloop
            
            player "LAAA LAAA LA LA!!\nLAA LAAAA LA LA LAA!!" with Shake((0, 0, 0, 0), 3.0, dist=30)
            show mauh nervous at bounce
            mauh "Oh..!"
            show wu at bounce
            wu "Oh wow."
            n "…!"
            narrator "The music fades out."
            stop music fadeout 1.0
            play sound "audio/N's Storyline/exhale slow clap.mp3" 
            show mauh nervous at bounce
            mauh "Wow, [YN], that was.. That was really something!"
            show wu at bounce
            wun "*Nodding heads*"
            player "Thanks. I really put my all into that one."
            show mauh 

    show wu mic at spotlight, bounce with move
    wu "I guess it's my time to shine~"
    # play music "audio/N's Storyline/Quiet Wu.mp3"
    $ moveBW()
    narrator "Wu gets up to sing. You and N sit next to each other in the back."

    menu:
        "\"So… what made you join this club?\"":
            $ n_score += 1
            narrator "N seems to like your unexpected question."
            n "… ({i}with motions here and there{/i})"
            player "Uhuh."
            n "… ({i}emphasis{/i})"
            player "I see"
            show n exclaim
            n "…!"
            show n
            player "Ah. ({i}Wow. I really don’t understand any of this at all.{/i})"
            show mauh at bounce
            mauh "Seems like you two are really getting along!"
            show n blush
            n "… ({i}flustered{/i})"
            player "N is good company!"
            show n

        "\"Do you ever speak?\"":
            $ n_score -= 1
            $ flag_perfect = False
            narrator "N seems to grimace at your intrusive questions."
            show n angry
            n "… (irritated)"
            player "Ah, no need to answer. I realize that might be a bit personal. (Wrong question to ask…)"
            $ moveColor()
            show n at audience_r with move
            show mauh at audience_m2 with move
            show mauh at bounce
            mauh "Hey guys, let me join you over here!"
            narrator "Mauh sits down between you two."
            show n

    $ moveColor()
    show mauh at bounce
    mauh "N’s always been on the more silent side. It’s always been just us three, me, Wu, and N… you know, women stick together!"
    player "That’s nice, I guess."
    n "…"
    mauh "We’re glad to have you here with us, though! Sometimes it gets a little repetitive when it’s us three all the time."
    n "…"
    player "Thanks… ({i}Again… how did I get here..?{/i})"
    narrator "The minutes seem to pass by, and the end of karaoke clubs comes quickly. Wu and Mauh head home together, waving goodbye to you and N.\nYou and N walk to the school entrance."
    
    stop music fadeout 1.0
    play music "audio/N's Storyline/rain.mp3"
    scene bg rain with fade
    n "… ({i}looking at the sky{/i})"
    player "Oh, it’s raining."
    narrator "You somehow have your own umbrella, just for this occasion."
    show n worry
    n "… ({i}standing, worriedly{/i})"
    show n
    player "What’s wrong?"
    n "…"
    narrator "It seems that N did not bring her umbrella."

    menu:
        "\"Would you like to share an umbrella?\"":
            $ n_score += 1
            show n exclaim
            n "…!"
            n "… ({i}nodding{/i})"
            show n blush
            player "Sure. Try to stick close to me, my umbrella isn’t all that big…"
            narrator "The scene fades to black."
        "\"Ah, sorry N. I really have to rush home…\"":
            $n_score -= 1
            $ flag_perfect = False
            n "… ({i}motions for you to go, with no worries{/i})"
            player "Really sorry again.."
            narrator "The scene fades to black."

    $ n_done = True

    return