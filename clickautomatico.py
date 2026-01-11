import threading
import pyautogui
from pynput import keyboard

rodando = False
thread = None

def loop_apertar_p():
    global rodando
    while rodando:
        pyautogui.keyDown('p')
        pyautogui.keyUp('p')
def alternar():
    global rodando, thread
    if not rodando:
        rodando = True
        thread = threading.Thread(target=loop_apertar_p, daemon=True)
        thread.start()
        print("▶ ON")
    else:
        rodando = False
        print("⏹ OFF")

def on_press(key):
    try:
        if key.char.lower() == 'g':
            alternar()
    except AttributeError:
        pass

print("G = ligar/desligar | Ctrl+C = sair")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

