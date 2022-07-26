import pyautogui
import time

pyautogui.PAUSE = 1.5

#abrindo a ferramenta no sistema
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("enter")

#verificando a posição do mouse para poder clicar no local certo
time.sleep(5)

#login
pyautogui.click(x=269, y=348)
pyautogui.write("Laura")


#senha
pyautogui.click(x=274, y=379)
pyautogui.write("123")

#login
#print(pyautogui.position())
pyautogui.click(x=225, y=437)