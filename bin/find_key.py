from pynput import keyboard

def on_press(key):
    print(f'Key pressed: {key}')

def on_release(key):
    print(f'Key released: {key}')

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
