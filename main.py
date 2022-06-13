import pyautogui
import time

screen = pyautogui.size()
print(screen.width)
print(screen.height)

pyautogui.FAILSAFE = False
pyautogui.moveTo(1, 1079)

colors = {
    "sarkana": (255, 0, 0), 
    "dzeltena": (255, 255, 0), 
    "zaļa": (0, 255, 0)
}

run = True
while run == True:
    p = pyautogui.position()
    for color in colors.keys():
        if pyautogui.pixelMatchesColor(p.x, p.y, colors[color]):
            print(color)
    time.sleep(3)