import mouseSeal as mouse
import keyboard
import pywinauto as p
from time import sleep
import macro
import imgread as img

print("ant.py")
print(mouse.getUserId())
inventory = []
k = p.keyboard
target = 0

def sellItem() :
    print('Selling Item..')
    mouse.moveMouse(555, 227)
    sleep(0.5)
    macro.mouseClick()
    sleep(0.5)
    while img.checkImage("./img/shop.jpg") == False :
        k.send_keys('{ENTER}')
        sleep(0.5)
        mouse.moveMouse(394, 296)
        macro.mouseClick()
        sleep(0.5)
    sleep(0.5)
    macro.sellSlot1()
    macro.sellSlot2()
    macro.sellSlot3()
    macro.sellSlot4()
    macro.sellSlot5()
    sleep(1)
    print("escape")

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
            macro.closeBSIfOpen()
            print('setting target')
            mouse.setTarget(target)
            print("target : " + str(target))
            inventory = mouse.getItemValue()
            k.send_keys('{SPACE}')
            k.send_keys('{F1}')
            k.send_keys('{F2}')
            k.send_keys('{F3}')
            k.send_keys('{F5}')
            k.send_keys('{F6}')
            k.send_keys('{F7}')
            k.send_keys('{F8}')
            k.send_keys('{SPACE}')
            k.send_keys('{SPACE}')
            if inventory[32] < 150 or inventory[33] < 150:
                buyPotion()
                sleep(0.5)
            for i in range(0,5) :
                if inventory[i] >= 250 :
                    print('Item Full Detected.')
                    sellItem()
                    print("Hunt Continue..")
            if keyboard.is_pressed('c') :
                print('stopping.')
                break
    if keyboard.is_pressed('=') :
        print('Script Stopped.')
        start = False
        break
    if keyboard.is_pressed("/") :
        print(mouse.getCurrentTarget())
        target = mouse.getCurrentTarget()
        mouse.setTarget(mouse.getCurrentTarget())
        sleep(0.2)

    if keyboard.is_pressed(']') :
        if img.checkImage("./img/monster.jpg", .65) :
            print('true')
        else : 
            print('false')
        mouse.getPosition()
        sleep(0.2)