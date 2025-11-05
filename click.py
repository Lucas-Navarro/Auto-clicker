import pyautogui
import time


achou = 'sim'

while achou == 'sim':
    try:
        img = pyautogui.locateCenterOnScreen('img/image.png', confidence=0.9)
        pyautogui.click(img.x, img.y)
        achou = 'não'
        if achou == 'não':
            pyautogui.click(623,965)
    except:
        time.sleep(0.1)
        print('Não encontrado')
