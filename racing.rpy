init python:
    def reset_racing_game():
        #Function to reset variables
        global selected_character
        global selected_character_pos
        global who_won
        global goal_reached
        global countdown_timer

        countdown_timer = 3
        who_won = None
        goal_reached = False
        selected_character = None
        selected_character_pos = [0,0]
        character_1.x = character_start_xpos
        character_2.x = character_start_xpos
        character_3.x = character_start_xpos

        #Hide game over and show menu again
        renpy.hide_screen("game_over")
        renpy.hide_screen("racing_mini_game")
        renpy.show_screen("racing_game_menu")

    def npc_movement(st):
        if not goal_reached and countdown_timer == 0:
            if selected_character == "character_1":
                npc_move(character = character_2)
                npc_move(character = character_3)

            elif selected_character == "character_2":
                npc_move(character = character_1)
                npc_move(character = character_3)

            elif selected_character == "character_3":
                npc_move(character = character_1)
                npc_move(character = character_2)
            return 0

        elif countdown_timer != 0:
            return 0

        else:
            return None

    def npc_move(character):
            # This function is for moving an NPC character according to their individual speeds.
            global goal_reached
            global who_won
            if character.x < goal_xpos:
                character.x += character.speed
            else:
                goal_reached = True
                who_won = character
                renpy.show_screen("game_over")
                renpy.restart_interaction()

    def character_move(character):
        global goal_reached
        global who_won
        global selected_character_pos

        if character.x < goal_xpos:
            character.x += player_char_speed
            selected_character_pos = [character.x, character.y]
            renpy.restart_interaction()
        else:
            goal_reached = True
            who_won = character
            renpy.show_screen("game_over")
            renpy.restart_interaction()


    def character_events(event, x, t, st):
        global left_key_pressed
        global right_key_pressed
        global player_start_move

        if event.type == renpy.pygame_sdl2.KEYDOWN and countdown_timer == 0:
            keys_pressed = renpy.pygame_sdl2.key.get_pressed()

            if keys_pressed[renpy.pygame_sdl2.K_LEFT]:
                player_start_move = True
                left_key_pressed = True
            elif keys_pressed[renpy.pygame_sdl2.K_RIGHT]:
                player_start_move = True
                right_key_pressed = True

            if left_key_pressed and right_key_pressed:
                left_key_pressed = False
                right_key_pressed = False

                if selected_character == "character_1":
                    character_move(character_1)
                elif selected_character == "character_2":
                    character_move(character_2)
                elif selected_character == "character_3":
                    character_move(character_3)

    def setup_racing_game():
        global selected_character_pos

        character_1.x = character_start_xpos
        character_1.y = 500
        character_1.speed = 0.1

        character_2.x = character_start_xpos
        character_2.y = 620
        character_2.speed=0.4

        character_3.x = character_start_xpos
        character_3.y=730
        character_3.speed = 0.3

        if selected_character == "character_1":
            selected_character_pos = [character_1.x, character_1.y]
        elif selected_character == "character_2":
            selected_character_pos = [character_2.x, character_2.y]
        elif selected_character == "character_3":
            selected_character_pos = [character_3.x, character_3.y]

        renpy.hide_screen("racing_game_menu")
        renpy.show_screen("racing_mini_game")

    def decrement_timer():
        global countdown_timer
        if countdown_timer > 0:
            countdown_timer -= 1

screen game_over:
    modal True

    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            align(0.5, 0.5)
            xysize(500,350)
            background Solid("#00000080")
            text "Game Over!" size 50 align(0.5, 0.2)
            if who_won is not None:
                if who_won == character_1:
                    if selected_character == "character_1":
                        text "You won!" size 40 align (0.5, 0.4)
                        textbutton "EXIT" align (0.5, 0.8) action Return()
                    else:
                        text "character_1 won!" size 40 align (0.5, 0.4)
                        textbutton "Play again!" align(0.5, 0.8) action Function(reset_racing_game)

                elif who_won == character_2:
                    if selected_character == "character_2":
                        text "You won!" size 40 align (0.5, 0.4)
                        textbutton "EXIT" align (0.5, 0.8) action Return()
                    else:
                        text "character_2 won!" size 40 align (0.5, 0.4)
                        textbutton "Play again!" align(0.5, 0.8) action Function(reset_racing_game)

                elif who_won == character_3:
                    if selected_character == "character_3":
                        text "You won!" size 40 align (0.5, 0.4)
                        textbutton "EXIT" align (0.5, 0.8) action Return()
                    else:
                        text "character_3 won!" size 40 align (0.5, 0.4)
                        textbutton "Play again!" align(0.5, 0.8) action Function(reset_racing_game)
            else:
                text "No winner yet!" size 40 align (0.5, 0.4)

            

screen countdown_timer:
    frame:
        background "#00000080"
        align(0.5, 0.5)
        xysize 400, 250
        vbox:
            align(0.5, 0.5)
            text "Get Ready!" size 40 xalign 0.5
            text "[countdown_timer]" size 40 xalign 0.5
    timer 1.0 action Function(decrement_timer) repeat True



screen racing_mini_game:
    on "show" action Show("countdown_timer")
    key ["K_LEFT", "K_RIGHT"] action NullAction()
    image "background.png"

    add character_sprites

    if not player_start_move and countdown_timer == 0:
        frame:
            align(0.5, 0.3)
            xysize(600, 250)
            background "#00000080"
            vbox:
                spacing 20
                align(0.5, 0.5)
                text "Alternate arrow keys to move" xalign 0.5
                add "arrow_keys" xalign 0.5

    image "player_indicator.png" xpos selected_character_pos[0] + 50 ypos selected_character_pos[1] - 50

screen racing_game_menu:
    image "background.png"
    image Solid("#00000080")

    text "Select a character!" size 50 align(0.5,0.1)
    
    hbox:
        align (0.5, 0.4)
        spacing 10
        imagebutton auto "character_1_%s.png" selected If(selected_character == "character_1", True, False) align(0.5, 0.5) action SetVariable("selected_character", "character_1")
        imagebutton auto "character_2_%s.png" selected If(selected_character == "character_2", True, False) align(0.5, 0.5) action SetVariable("selected_character", "character_2")
        imagebutton auto "character_3_%s.png" selected If(selected_character == "character_3", True, False) align(0.5, 0.5) action SetVariable("selected_character", "character_3")
    imagebutton idle "play_button_idle.png" sensitive If(selected_character is not None, True, False) action Function(setup_racing_game) align(0.5, 0.8)


image arrow_keys:
    zoom 0.5
    "arrow_keys_1.png"
    pause 0.5
    "arrow_keys_2.png"
    pause 0.5
    repeat

#sprites
default character_sprites = SpriteManager(update = npc_movement, event = character_events)
default character_1 = character_sprites.create("character_1.png")
default character_2 = character_sprites.create("character_2.png")
default character_3 = character_sprites.create("character_3.png")

#character variables
default character_start_xpos = 100
default goal_xpos = 1500
default player_char_speed = 20

#key variables
default left_key_pressed = False
default right_key_pressed = False
default player_start_move = False

#Other variables
default selected_character = None
default selected_character_pos = [0,0]
default who_won = None
default goal_reached = False
default countdown_timer= 3


