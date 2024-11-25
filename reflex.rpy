init python:
    import random
    
    def light_button():
        global random_button_indexes
        global current_button_index

        if current_button_index < buttons - 1:
            current_button_index += 1
        else:
            current_button_index = 0
            random_button_indexes = random.sample(range(6), k=6)
        random_button_index = random_button_indexes[current_button_index]
        button_states[random_button_index] = "lit"
    
    def reflex_game_bpress(btn):
        global score
        if button_states[btn] == "lit":
            score += 1
            button_states[btn] = "idle"

    def setup_reflex_game():
        global random_button_indexes

        for i in range(buttons):
            button_states.append("idle")

        random_button_indexes = random.sample(range(buttons), k=buttons)

    def reset_reflex_game():
        global play_time
        global score
        global initial_countdown

        initial_countdown = 3.0
        play_time = 20.0
        score = 0
        for i in range(buttons):
            button_states[i] = "idle"

        renpy.show_screen("countdown_timer_react")

    def hide_countdown_and_start_game():
        """Function to hide countdown screen and show the game screen."""
        renpy.hide_screen("countdown_timer_react")  # Hide the countdown screen
        renpy.show_screen("reflex_minigame")  # Show the reflex minigame screen


screen reflex_minigame:
    on "show" action Show("countdown_timer_react")
    image "background_react.png"

    $ buttons_per_row = 3  # Maximum number of buttons per row (can be adjusted)
    $ rows = (buttons + buttons_per_row - 1) // buttons_per_row  # Calculate number of rows based on buttons count
    
    vbox:  # Using a vertical box layout (flow)
        spacing 20  # Space between rows
        align(0.5, 1.2)  # Align in the middle of the screen
        # Render the buttons in rows
        for row in range(rows):
            hbox:  # Horizontal box (for each row of buttons)
                spacing 20  # Space between buttons in a row
                align(0.5, 0.5)  # Center the buttons in each row
                for i in range(buttons_per_row):
                    $ index = row * buttons_per_row + i
                    if index < buttons:  # Only show buttons if they exist
                        imagebutton idle "button-%s.png" % button_states[index] focus_mask True action Function(reflex_game_bpress, btn = index)

        # Display score and play time
        text "[str(score)]" size 78 align(0.79, 0.145) text_align 0.5  # Display score
        text "[str(play_time)]" size 78 color "#FFFFFF" align(0.79, 0.355) text_align 0.5  # Display play time

        # Logic for lighting buttons and handling game time
        if renpy.get_screen("countdown_timer") == None:
            if "lit" not in button_states:  # If no buttons are lit, start lighting them
                timer 0.1 action Function(light_button) repeat False
            timer 1.0 action [
                If(play_time > 1, SetVariable("play_time", play_time - 1), Show("reflex_minigame_over")),
            ] repeat True



screen reflex_minigame_over:
    modal True
    frame:
        background "game-over-bg.png"
        xysize(1072,698)
        align(0.5, 0.5)
        text "Your score: [score]" size 50 text_align 0.5 align (0.5, 0.4)
        if score < 20:
            imagebutton idle "play-again-button.png" align(0.5, 0.8) action [Hide("reflex_minigame_over"), Function(reset_reflex_game)]
        else:
            imagebutton idle "quit-button.png" align(0.5, 0.8) action Return()
        
screen countdown_timer_react:
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "[initial_countdown]" size 120 text_align 0.5 align(0.5, 0.5)

    # Timer that decrements the countdown each second and hides the screen when the countdown hits 0
    timer 1.0 action [
        If(initial_countdown > 1, SetVariable("initial_countdown", initial_countdown - 1), None),  # Decrement countdown
        If(initial_countdown == 1, SetVariable("initial_countdown", 0), None),  # Set to 0 when it reaches 1
        If(initial_countdown == 0, Function(hide_countdown_and_start_game), None)  # Call function to hide and start game
    ] repeat True
    
default button_states = []
default buttons = 6
default random_button_indexes = []
default current_button_index = 0
default score = 0
default play_time = 20
default initial_countdown = 3
