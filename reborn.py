import mouseSeal as mouse
import keyboard
from time import sleep
import macro
import imgread as img

print(mouse.getUserId())
inventory = []

def buyPotion() :
    macro.buyPot()
    sleep(0.1)
    print("bank : " + str(macro.checkBank()))
    print("shop : " + str(macro.checkShop()))
    sleep(0.1)

while True:
    if keyboard.is_pressed('-') :
        print("Start Spam Hunt..")

        while True:
            macro.closeBSIfOpen()
            mouse.spamSkill()
            sleep(2.3)
            inventory = mouse.getItemValue()
            if inventory[32] < 150 or inventory[33] < 150:
                buyPotion()
                sleep(0.5)
                mouse.moveMouse(816, 228)
                sleep(0.5)
                macro.mouseClick()
                mouse.moveMouse(500, 378)
                sleep(0.5)
                macro.mouseClick()
            if img.checkImage("./img/party.jpg") :
                mouse.moveMouse(234, 263)
                macro.mouseClick()

    if keyboard.is_pressed('=') :
        print('Script Stopped.')
        start = False
        break

    if keyboard.is_pressed(']') :
        mouse.getPosition()
        sleep(0.2)