import mouseSeal as mouse
import keyboard
from time import sleep
import pyautogui
import pywinauto as p
import win32api
import macro
import imgread as img

k = p.keyboard
m = p.mouse

print(
    "PID : "+ str(mouse.getPid()) + "\n"
    "ID : "+ str(mouse.getUserId()) + "\n"
)

start = True
inventory = []
# i = imagesearch

def puttingItem() :
    print('Put to Bank..')
    macro.itemToBank()
    sleep(0.2)
    macro.closeBSIfOpen()
    print('Done putting item.')
    # macro.sellTrashItem()

def runHunt() :
    print("Hunt Started..")
    start_hunt = True
    while start_hunt :
        print("Getting inventory list")
        inventory = mouse.getItemValue()
        if inventory[32] < 200 or inventory[33] < 150:
            macro.buyPot()
            sleep(0.1)
            print("bank : " + str(macro.checkBank()))
            print("shop : " + str(macro.checkShop()))
            macro.sellTrashItem()
            sleep(0.1)
        macro.closeBSIfOpen()
        mouse.moveMouse(505, 401)
        macro.mouseClick()
        sleep(1)
        if keyboard.is_pressed('c') :
            print('Hunt Stopped.')
            start_hunt = False
            break
        print("Item : "+ str(inventory[0]))
        if inventory[0] == 300 :
            print('Item Full Detected.')
            puttingItem()
            print("bank : " + str(macro.checkBank()))
            print("shop : " + str(macro.checkShop()))
            macro.closeBSIfOpen()
            print("Hunt Continue..")
        k.send_keys(
            "{q down}"
            "{q up}"
        )
        sleep(1)
        k.send_keys(
            "{F5}"
        )
        sleep(3)
        for x in range(0,10) :
            k.send_keys("{SPACE}")
            sleep(0.05)
            k.send_keys("{SPACE}")
            sleep(0.05)
            k.send_keys("{SPACE}")
            sleep(0.05)
            k.send_keys("{SPACE}")
            sleep(0.05)
            if keyboard.is_pressed('c') :
                print('Hunt Stopped.')
                start_hunt = False
                break

print("Press [=] to stop all\n"
    "Press [-] to start\n"
    "Press [c] to stop\n"
)

while start:
    if keyboard.is_pressed('-') :
        print("Starting Hunt..")
        runHunt()
    if keyboard.is_pressed(']') :
        mouse.getPosition()
        # mouse.getItemQty()
        sleep(0.3)

    if keyboard.is_pressed('=') :
        print('Script Stopped.')
        start = False
        break