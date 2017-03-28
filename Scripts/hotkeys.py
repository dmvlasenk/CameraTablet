import keyboard

def test1():
    print("hhh")

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))
#keyboard.add_hotkey('alt+1', test1)
keyboard.add_hotkey('ctrl+win', test1)
keyboard.add_hotkey('alt+f8', test1)
keyboard.add_hotkey('ctrl+1', test1)

#keyboard.press_and_release('shift+s, space')

# Blocks until you press esc.
keyboard.wait('esc')