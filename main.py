def on_button_pressed_a():
    x = randint(0, 9)
    basic.show_number(x)
input.on_button_pressed(Button.A, on_button_pressed_a)