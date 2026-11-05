label common_route:
    #Glimpse into the job system. There's only one job on the menu and it's for clothing repair. Players must choose the job to continue. 

    #click job and hit confirm. 

    "Clothing repair jobs are his favorite. They don't come up in his gig searches very often, but when they do—he snatches them up as fast as he can." 

    #nvl mode - bg is inner-city alley

    "He messages the client and gets an enthusiastic response upon realizing that he's the one who repaired her clothes the last time too." 

    "She tells him to come to the same place as before and that she'll clear a space for him to work at her apartment. All she asks is that he hem an old dress of hers."

    "Aero hums happily at the chance to work peacefully with his needle and thread in hand. The work won't exhaust him nearly as much as Neon's does."

    #stat check
    if aero.stat_num("Knowledge") > 10:
        $ aero.statMath("Affluence", 10)
    
    "The job is complete with no issues, and he had a surprisingly nice time speaking with his client. The extra money in his bank account doesn't hurt much either." 

    "He walks down the street feeling lighter after a job well done." 

    #stat check
    #awareness ✕

    "Too caught up in his own mind, Aero doesn't notice the pair of footsteps trailing behind him." 
    #back to adv mode
    #alley bg - evening/night
    #bg is half blurred (left side)
    #Aero's mood is at 2
    
    "His head reverberates what feels like a kick drum in his skull. A steady pounding of constant, distant pain. His vision is blurred, likely caused by the slow trickle of something hot and wet seeping into his eye."

    #black screen/blink effect

    aero.c "Fucking hell."

    "The dark makes it easier to parse through his memories."

    "A sharp kick to the ribs, a punch to the jaw, and the thud of his head hitting the wall behind him." 

    "Snippets of the things they shouted at him float back to him."

    aero.c "Always something about my damn clothes..."  

    "Selen used to warn him about dressing the way he does. About people who would target him for no other reason than for what he wore."

    "But his clothes are the only things that truly belong to him."

    "He checks his pocket for his phone, sighing in relief when he feels it is still safely tucked into aero.c hidden pocket of his pants."

    #If VA is in, Aero coughs here
    #Aero's eyes snap open
    "Anger claws its way up through his throat with such ferocity that he almost chokes on it."

    "It isn't the first time he's lost a fight. It probably won't be the last."

    aero.c "(This is bullshit.)"

    #show bg with the blurred out again
    #blink effect
    #clear bg

    #phone buzz sfx
    #text notification/prompt appears. Player must click to access the phone interface and then navigate to the text screen

    aero.c "(What is it now?)"

    
    # Neon: Where are you? 

    menu: 
        "A little busy atm.":
            
            neon "You get jumped again?"
            neon "Told you that pretty face of yours was trouble. "

        "Omw, calm down.":
             
            neon "I'm perfectly calm."
            neon "You won't be when you see how much I dock your pay for this. Hurry up."

    #Aero shuts off his phone

    "He tucks the device into his back pocket with a sigh."

    "As much as he wants to, skipping out on Neon isn't an option."

    #Aero groans
    aero.c "Guess I've got no choice."

    "His feet are a bit unsteady, but it's nothing he can't push through."
   
    #alley #2  bg - night

    "Lurid LEDs cast an acidic glow over the backstreets, reflecting in the pools of water leftover from an earlier rain."
    #Neon CG 1 start
    "Neon leans against the adjacent wall. Her electric green contacts lazily track his movements."

    "She doesn't bother with pleasantries." 

    neon "Clients will be here any minute now."

    "A heavy metal case is held out to him."

    neon "Don't hand it over until I receive payment. I'll text when I get it."

    aero.c "I know. I've done this enough times."

    neon "Just making sure that head injury didn't scramble your brains. You're still bleeding."

    #end CG

    "Aero stops just outside of Neon's reach with an exaggerated sigh."

    aero.c "Have a little sympathy, Neon. Can't you see that I'm at death's door?"

    aero.c "You should be asking if I'm okay, or at least giving me a second to breathe."

    "Neon's lips press together in a tight line, and her bright contacts blink out as she closes her eyes. They open again after a count of five."

    "Most people count to ten when they need to calm down. Neon calls that inefficient."

    neon "I don't have time to entertain you right now. Take the case."

    "It's held out between them, dangling from Neon's fingers mockingly. The gesture resembles that of an owner teasing their dog with aero.c treat."

    "Aero's fingers twitch with restrained emotion."

    "How many times has he done this now? Taken small jobs from people with cold and condescending eyes for the percentage of a percentage of aero.c buck?"

    "How many more times will he be forced to beg for scraps before life throws him a bone?"

    "Probably too many to count."

    menu:
        
        "Take the case.":
            #patience +
            $ aero.statMath("Patience", 10)
            "Cold metal meets his fingertips. Neon nods."
            neon "Don't forget your mask."
            aero.c "I'm not stupid."
            neon "Could've fooled me."

        "Refuse.":
            $ aero.statMath("Arrogance", 10)
            #arrogance +
            aero.c "You do it."
            neon "We've been over this, Aero."
            neon "{i}You{/i} do the handovers—"
            
    neon "{i}I{/i} do the tech, run the bar, manage the client list, and every other little fucking thing that keeps us both fed."
    "The case is pushed into his chest with enough force to make him stumble."

    "Footsteps echo from around the corner—Neon's gone before he can form a response."

    "He scowls, skimming his boot over the surface of a puddle and trying his best not to feel like somebody's kicked puppy. It doesn't work."

    aero.c "(Whatever. I'll do it.)"

    aero.c "(You never know—this could be my thread to freedom.)"

    "Aero presses a hand to his head, attempting to ease the faint pounding in his skull. It almost feels like a warning."

    aero.c "(It's getting harder and harder to believe myself.)"

    "From around the corner appears a paltry party of two. Dirty clothes, tired slouches, flitting eyes."

    "They reek of desperation."

    "He briefly wonders if it's contagious. Maybe he's already infected."

    "The jumpy-looking one speaks first."

    "Hasty Client" "You have it?"

    aero.c "No, I'm waiting in a waterlogged alley holding highly illegal contraband for someone else."

    "It's hard to make out their expressions beneath the masks, but judging from their silence, Aero doubts they're amused." 

    aero.c "...Yes. I have it."

    "Hasty Client" "Great, then hand it—"

    aero.c "Ah—no. I need the money first."

    aero.c "Five grand. Then you can have your tech."

    "Skeptical Client" "You first. Open the case."

    aero.c "Wary guy, aren't you?"

    "Still keeping his distance, Aero carefully shifts the case to be horizontal and unclasps the latches holding it closed."

    #show tech (mask and contacts) in case on screen - art asset needed

    "Skeptical Client" "What is {i}that{/i}?"

    "Hasty Client" "That's just a mask and contacts."

    aero.c "Uh, yeah? What'd you think they'd look like?"

    "Skeptical Client" "How are we supposed to know they work?"


    aero.c "That's where this thing called \"trust\" comes in."

    aero.c "I sell illegal shit, people buy it. The fact that I'm still here is our product guarantee."

    aero.c "It's very simple, actually." 

    "Aero shuts the case."

    "The two share a glance, a silent conversation taking place."

    #phone ding sfx and on-screen notif. player has to open the phone to see the text msg and proceed

    #(TEXT)
    #Neon: Received.

    aero.c "See?"

    "Skeptical Client"  "Are you serious?!"

    "Hasty Client" "We need a way to avoid facial recognition scanners, right? We'll just have to trust him."

    "Hasty Client" "And if it doesn't work—well, you heard him. We'll have ourselves a new mark."

    "While Neon's tech is the real deal—he would've been busted by now if his own mask and contacts didn't work—Aero still winces. If there's one thing he can't afford to do, it's die young."

    "Not only would it be a waste of a pretty face, but he hasn't made his way to the top yet. He'd like to look down on everyone from above."

    "Preferably from the balcony of a cushy penthouse."

    aero.c "Great! Looks like we're all in agreement then."

    aero.c "Good luck with your heist!"

    "Skeptical Client" "Wha—"

    "Hasty Client" "Dude, shut up. Let's go."

    "The sad sacks who are probably planning to rob some rich assholes clear out first. Aero makes himself scarce shortly after."

    aero.c "I need a drink…"
   

    #scene change 
    #CyberCELL - night

    "CyberCELL isn't anything special as far as bars are concerned. It might even be less than special with its fraying leather booths, burnt-out overhead lights, and generally unsavory patronage."

    "Cigarette smoke fills Aero's lungs, and the sharp sting of alcohol burns his nostrils as he steps into the bar. He breathes it in readily, comforted by the idea that technology will never steal his favorite vices."

    "Not that they were in danger of extinction to begin with. After all, what would big pharma do if people stopped sabotaging themselves?"

    "The rhythmic shaking of a cocktail shaker grows louder the closer Aero gets to the counter. He has to press himself between two drunk bodies to catch a glimpse of his target: Neon."

    "Fluid and quiet grace characterizes her movements. It's hard not to notice, and even harder not to envy."

    "Neon's always been that way."

    "When they were kids it was unconscious. Now, it's calculated."

    "His eyes track her as she works, and Aero can't stop himself from noticing how toned her biceps are with every shake of the mixer. Maybe she should be the one taking care of the hand-offs."

    aero.c "(Working as a bartender for years on end is surprisingly good for building muscle.)"

    "In another life, he might've fallen for her."

    aero.c "..."

    "Neon notices him loitering at the end of the bar and acknowledges him with a nod."

    "It takes a few minutes, but eventually Neon deigns to grace Aero with her full attention and a glass of his favorite whiskey."

    neon "Were there any issues?"

    aero.c "Unless you consider my deteriorating mental state a loss, then no."

    neon "Great. I'll wire you five percent."

    "Like a video feed cutting out, Aero's mind fills with static."

    aero.c "Five percent?"

    neon "Yes."

    aero.c "That's—that's nothing. You made five grand!"

    neon "First of all, you need to keep your voice down. Being in a blind spot doesn't mean jack if some undercover asshole overhears you."

    neon "Second of all, your only job was to hand over the product."

    neon "Most of the money goes back into operating expenses. You're not the only one getting snubbed."

    aero.c "I'm worth more than five percent."

    "She scoffs."

    neon "Since when?"

    #begin negotiation 

    #timed choice:
    menu:
        

        "Handovers are dangerous.":
                
                aero.c "I take on the risk of things going sideways. Even with a mask on, I'm the one facing clients."
                neon "So, what? You want hazard pay?"
                aero.c "I want you to acknowledge my efforts—but hazard pay would be nice too."
                neon "I'm not forcing you to do this."
                aero.c "No. But wouldn't it be annoying if I were to quit?"
                "Neon raises an eyebrow."
                neon "You're not going to quit."
                
                menu:
                    

        

                    "You underestimate me.":
                        aero.c "I'm not above betrayal."
                        aero.c "You think I can't make my own client list? Source my own product?"
                        neon "I'm sure you {i}can{/i}."
                        neon "I just don't think you {i}will{/i}."
                        
                        menu:
                            
                            "I could surpass you.":
                                "She sighs, unamused."
                                neon "Then why haven't you done it already?" 
                                jump negotiation_fail
                            
                            "Selen used to say that was your fatal flaw.":
                
                                aero.c "You don't see anyone's potential but your own. That's why she didn't take you with her."
                                "Neon's jawline tightens subtly. Aero smirks in satisfaction."
                                neon "I chose to stay here."
                                "Aero raises an eyebrow in disbelief. Neon switches gears."
                                neon "...She left you too."
                                "Bringing up Selen was a risky move. A double-edged sword that always ended up cutting them both."
                                aero.c "Maybe. But wasn't it you who came crying to me when she left?"
                                neon "Screw you, Aero."
                                neon "You want hazard pay? Fine."
                                "A few taps later, and Aero's phone buzzes in his pocket."
                                neon "Take it, and then step away from my counter. I'm done with you today."
                                aero.c  "Glad we're on the same page." 
                                jump negotiation_success
                            
                    
                    "You're not the only person I work for.":
                
                        neon "No. But I'm the only one who hires you consistently."
                        neon "I can't quite abandon you, even though it would be easier."
                        aero.c "Fuck off." 
                        "Aero hates Neon the most when she's right. She called his bluff—quiting wasn't something he could afford. At least, not right now."
                        neon "So? Five percent? Take it or leave it."
                        aero.c "...I'll take it."
                        neon "There we go."
                        "A few taps later, and Aero's phone buzzes in his pocket."
                        jump negotiation_fail

        

        
        
    

    


        "Since always.":
            
            neon "Right…"
            jump negotiation_fail

    
label negotiation_fail:
    $ aero.statMath("Affluence", -100)
    $ aero.moodMath(-2)
    aero.c "Nevermind. Just—wire the money."
    "A few taps later, and Aero's phone buzzes in his pocket."
    neon "Done."
    
    "Tucked into a hidden corner of the bar, Aero nurses his bruised ego."
    jump common_route_b


label negotiation_success:
        
    $ aero.statMath("Affluence", 150)
    $ aero.moodMath(2)
    "Tucked into a hidden corner of the bar, Aero nurses his drink of choice. The extra bit of money in his bank account only keeps his spirits high for as long as it takes for Neon to shake up another cocktail."

    "It's a victory as shallow as the honey brown liquor before him."
   

    

label common_route_b:
    #BRANCHES CONVERGE HERE

    "Neon thinks she's better than him—that's nothing new, but her attitude towards him has only grown more antagonistic over time."

    aero.c "(She used to rely on me… when did that change?)"

    "One moment, Aero was the one keeping her afloat. Then, seemingly overnight, she was the one leading {i}him{/i} around by the nose."

    aero.c "(Pathetic.)"

    "From his pocket Aero produces a lighter and a pack of cigarettes. He sets one to his lips, inhaling as he watches the tip glow ember red. The first pull is always the strongest, and Aero delights in the pleasant lightheadedness that overtakes him."

    "He exhales a puff of smoke as he tips his head back to stare at the pulsing lights above. If you ignore the signs of his earlier scuffle, then Aero paints quite the beautiful picture with how he's curled comfortably in the worn booth."

    "Inside, the truth is much uglier. His head still pounds from a definite concussion, and at this point he's running on pure defiance."

    "The drink will dull his physical pain, and the nicotine will calm the shaking of his hands."

    "Now he just needs something, or someone, to bring him out of his own mind."

    aero.c "(Just for long enough to get through the night.)"

    "Each day Aero survives in this hell brings him closer to the break he believes is coming. It's only a matter of time, and when the opportunity arises, he'll be waiting for it."

    "???" "You look like you could use some company."

    #Lynx CG 1

    "Suddenly, someone slides into the seat across from him. They lean forward on their elbows—clearly flirtatious."

    "Aero angles himself towards the stranger."

    aero.c "(Maybe God {i}is{/i} real.)"

    aero.c "Are you offering?"

    "???" "Depends. Are you interested?"

    "Aero is rarely uninterested. It isn't in his playbook to turn down a conveniently timed beauty."

    aero.c "Always."

    "???" "Always, he says. Doesn't that get you into trouble?"

    "All the time."

    aero.c "I can handle it."

    #end CG

    "The person across from him stands abruptly, moving to Aero's side of the booth."

    "Their thighs brush, and the stranger leans in until their noses are just about touching."

    lynx "I'm Lynx."

    "Aero snuffs his cigarette in the nearest ashtray in favor of something he finds much more stimulating."

    aero.c "Aero."

    lynx "Ah,\"to lift up\"."

    aero.c "What?"

    lynx "That's what your name means. It's Greek, right?"

    lynx "Unless it's actually spelled A-R-R-O-W? In which case—"

    "Lynx shrugs, a very exaggerated 'I have no idea.'" 

    aero.c "(\"To lift up\", huh? How ironic.)"

    "No one had ever bothered to teach Aero what his name meant—how could they when his parents weren't around to pass the knowledge down?"

    "His fingers itch to light another cigarette."

    "Lynx taps a finger to the side of their face."

    lynx "It's a good name. Optimistic."

    aero.c "Thanks… I guess?"

    aero.c "What does your name mean then? Besides the obvious."

    lynx "You like it? I chose it myself."

    lynx "I picked it for the constellation. We can't see it anymore—too much air pollution—but it's there."

    aero.c "How do you know it's still there if you can't see it?"

    lynx "Constellation patterns are well documented. That, combined with a little faith?"

    "Lynx winks."

    lynx "I know it."

    aero.c "..."

    "What is it like to be brave enough to choose your own name?"

    "Aero smooths a hand over the fabric of his pants, wiping the sweat from them. An identity crisis is a luxury he can't afford right now—he hardly has the time to think about his next meal." 

    "A cool finger presses against the spot between his brows. The sudden gesture causes Aero to flinch backwards."

    lynx "You'll ruin your good looks if you keep doing that."

    "The praise loosens the knot of tension keeping him wound tight. Aero lets his shoulders drop a fraction."

    aero.c "Well, we can't have that."

    lynx "No, we can't."

    lynx "What are you doing here anyways?"

    aero.c "At the bar?"

    lynx "Sure."

    "The last thing he needs is someone prying into his business, accidentally or otherwise."

    aero.c "(You never know who might be listening.)"

    aero.c "Needed a drink. Long day."

    lynx "Payment negotiations aside, right?"

    lynx "Nobody comes here just because they \"needed a drink\". Also, you're not very subtle."

    "Aero bites his lip in annoyance before blurting out:"

    aero.c "Why are {i}you{/i} here?"

    lynx "For gossip, of course. People let all kinds of things slip when they're drunk."

    aero.c "You're terrible at picking targets. I'm not even tipsy."

    lynx "Maybe not. But {i}they{/i} are."

    "They flick their hand casually towards a couple arguing nearby."

    lynx "They've been fighting about money for the last twenty minutes."

    aero.c "Thrilling."

    lynx "Listen."

    "By now Aero has given up on his fantasies of having any fun tonight. He stifles a sigh, tuning into the low whisper-shouts nearby."

    "Agitated Woman" "This could be our chance to make it big—"

    "Wary Man" "We could just as easily wind up dead in a ditch."

    "Wary Man"  "How many times do I have to tell you—" 

    "Wary Man" "No."

    "Agitated Woman" "What's {i}your{\i} plan then? We're scraping the bottom of the barrel here."

    "Wary Man" "I don't know, Kei! But joining The Claw? Hell no."

    "Woman Called Kei" "Shhh! Fuck, okay. It's just—"

    "Wary Man" "Not worth it. The Claw isn't a place you join for fun. I don't care how much money they offer."

    "Aero scoffs, locking eyes with Lynx."

    aero.c "Lots of people try to join The Claw for money. What of it?"

    lynx "You haven't heard the news then?"

    lynx "Anyways, sounds like they're offering a bonus to anyone who's able to pass the initiation test."

    aero.c "Yeah? A bonus of what, five-hundred bucks? Not worth it."

    lynx "You tuned in too late. The bonus is twenty-grand."


    aero.c "Twenty—! Per person?"

    "Lynx's eyes crinkle in amusement, and they laugh, tinkling and bright."

    lynx "That got your attention, huh? That much is a spider's thread to anyone looking to climb out of this hellhole."

    lynx "For a bonus, it's more than generous."

    aero.c "..."

    "It's more than enough to get Aero thinking. Proof that he's just as bad as the quarreling couple."

    "Even so, he stands by what he said earlier. Getting access to The Claw is dangerous enough on its own."

    aero.c "I'm not that desperate." 

    "Their gaze feels like a rake as it drags over him—appraising."

    lynx "I see."

    "The air surrounding them seems to drop ten degrees as Lynx's playful demeanor drops like a discarded coat."

    lynx "Well. That's a shame."

    "Then they slip out of the booth, leaving Aero alone, and cold. Again."

    #Mood -2
    $ aero.moodMath(-2)


    "He doesn't linger in CyberCELL for much longer after that."

    #scene Aero's apartment - night

    "Patience is in short supply with Aero, especially after today."

    "He's unfortunately used to being jerked and dragged around, but the last few months have worn him thinner than a sheet of paper."

    "Neon's authoritative grip lost its novelty early on. Still, the pay was good enough to land him his own cramped studio… and despite all Neon's talk, he knew she wouldn't actually replace him."

    aero.c "(Better the devil you know than the one you don't.)"

    "Still…"

    aero.c "(Something has to give.)"

    aero.c "(Surely I'm meant for better things.)"

    "\"To lift up.\""

    aero.c "(It sounds so… martyr-ish.)"

    "Aero never plans to lift anyone up but himself."
    return 
    