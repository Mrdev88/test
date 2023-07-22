myImage: Image = None

def on_button_pressed_a():
    basic.show_string("Test")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for index in range(2):
        basic.show_arrow(ArrowNames.NORTH)
        basic.pause(100)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.pause(100)
        basic.show_arrow(ArrowNames.EAST)
        basic.pause(100)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.pause(100)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.pause(100)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.pause(100)
        basic.show_arrow(ArrowNames.WEST)
        basic.pause(100)
        basic.show_arrow(ArrowNames.NORTH_WEST)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global myImage
    myImage = images.create_image("""
        # # # # #
        # # . . #
        # . # # #
        # # # . #
        # # # # #
        """)
    myImage.show_image(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_arrow(ArrowNames.NORTH)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    pass
basic.forever(on_forever)
