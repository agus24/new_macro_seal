import mouseSeal as mouse
import keyboard
import pywinauto as p
from time import sleep
import macro
import imgread as img

print(mouse.getUserId())
inventory = []
k = p.keyboard

def buyPotion() :
    macro.buyPot()
    sleep(0.1)
    print("bank : " + str(macro.checkBank()))
    print("shop : " + str(macro.checkShop()))
    sleep(0.1)

while True:
    if keyboard.is_pressed('-') :
        print("Start Spam Hunt..")
        i = 0
        while True:
            print(i)
            macro.closeBSIfOpen()
            inventory = mouse.getItemValue()
            macro.mouseClick()
            k.send_keys('{q down}' '{q up}')
            k.send_keys('{F1}')
            sleep(0)
            k.send_keys('{F2}')
            sleep(0)
            k.send_keys('{F3}')
            sleep(0)
            k.send_keys('{F5}')
            sleep(0)
            k.send_keys('{F6}')
            sleep(0)
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
                mouse.moveMouse(262, 269)
                macro.mouseClick()
            # if i > 50 :
            #     k.send_keys('{F2}')
            #     sleep(0.2)
            #     k.send_keys('{F2}')
            #     mouse.spamSkill()
            #     print('force skill')
            #     i = 0
            # if img.checkImage("./img/skillsettemplar.png") :
            #     i = i+1

    if keyboard.is_pressed('=') :
        print('Script Stopped.')
        start = False
        break

    if keyboard.is_pressed(']') :
        if img.checkImage("./img/skillsettemplar.png", .6) :
            print('true')
        else : 
            print('false')
        mouse.getPosition()
        sleep(0.2)