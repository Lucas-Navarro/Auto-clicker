import pyautogui
import time
import os, sys

rodando = False

def resource_path(relative_path):
    """Garante o caminho correto para o arquivo (funciona no .py e no .exe)"""
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def localizarOferta():
    global rodando
    while rodando:
        try:
            img_path = resource_path('image.png')
            img = pyautogui.locateCenterOnScreen(img_path, confidence=0.9)
            pyautogui.click(img.x, img.y)
            achou = 'sim'
            if achou == 'sim':
                pyautogui.click(623,965)
        except:
            print('Não encontrado')
    time.sleep(0.1)

def iniciar():
    global rodando
    rodando = True

def parar():
    global rodando 
    rodando = False
