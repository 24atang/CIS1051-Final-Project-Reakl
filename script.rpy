
label start:  
    scene new_school_gym:
        xysize(1920,1080)
    show eight neutral at left
    show zero happy at right:
        ypos 1300
    "Jane" "Hello!"
    "John" "We are physical trainers that will help you pace your FitnessGram PACER test"
    show eight serious
    "Jane" "Well, not really, cause they are just playing some computer games"
    show zero surprised:
        ypos 1300 
    "John" "You're right"
    show eight neutral 
    "Jane" "Yes, as always. What we are really doing is mentally preparing them for the test"
    show zero worried:
        ypos 1300 
    "John" "But how is playing a game going to help them?"
    "Jane" "Well, they can envision themseleves doing these things..."
    "John" "I'm still not really convinced..."
    show eight angry
    "Jane" "Well it doesn't matter what you think, because this is a scientifically proven method of helping kids pass this test"
    show zero sad:
        ypos 1300
    "John" "Ok..."
    show eight neutral
    "Jane" "Well, welcome to the FitnessGram PACER test for Lazies!"
    show zero happy:
        ypos 1300 
    "John" "First, you are going to run a mile and beat all your other classmates"
    "Jane" "That's how you assert your dominance and show everyone how athletic you are!"

    call screen racing_game_menu
    jump after_race

label after_race:
    scene new_school_gym:
        xysize(1920,1080)
    show eight neutral at left
    show zero happy at right:
        ypos 1300
    "Jane" "Good job!!"
    "John" "You did it!"
    "Jane" "Now it is time for you to test your reaction time"
    show zero worried
    "John" "How would that help with the test?"
    show eight serious
    "Jane" "Well, because with a faster reaction time they can quickly pivot between each lap, duh"
    show zero happy
    "John" "That makes sense!"
    show eight worried
    "Jane" "Where should we put the game though?"
    show zero serious
    "John" "Mmmmmmmmmm"
    show eight surprised
    "Jane" "What about some place relaxing, since reaction games can be stressful"
    show zero happy
    "John" "Good idea!"
    show eight angry
    "Jane" "Well do you have any ideas?"
    show zero sad 
    "John" "Uhhhhh, no I don't..."
    show eight angry
    "Jane" "Do I have to think of everything...well a beach is a good idea"
    show zero happy
    "John" "Yeah that's really good"
    show eight neutral
    "Jane" "No thanks to you"
    show zero sad
    "Jane" "Here is the game! You must get a score of more than 20 within 20 seconds, or else you have to keep trying."

    $setup_reflex_game()
    call screen reflex_minigame
    jump after_reflex

label after_reflex:
    scene new_school_gym:
            xysize(1920,1080)
    show eight surprised at left
    show zero happy at right:
        ypos 1300

    "Jane" "Finally! Our work here is done!"
    "John" "You now should be prepared for your test soon!"
    "Jane" "Mentally, at least"
    "John" "Of course!"
    show eight serious
    "Jane" "I hope to see you again for our next test for lazies"
    "John" "See you soon!"

