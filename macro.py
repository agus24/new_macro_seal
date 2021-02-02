import pyautogui
import mouseSeal as mouse
from time import sleep
import pywinauto as p
import imgread as img
from constants import DIALOG

k = p.keyboard
delay = 0.5

slot = [
    [301, 86],
    [331, 86],
    [361, 86],
    [391, 86],
    [421, 86],
    [451, 86],
    [481, 86],
    [511, 86],
    # [301, 123],
    # [331, 123],
    # [361, 123],
    # [391, 123],
    # [421, 123],
    # [451, 123],
    # [481, 123],
    # [511, 123],
]

shop = [555, 227]

def mouseClick() :
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    sleep(delay)

def mouseDown() :
    pyautogui.mouseDown()
    sleep(delay)

def mouseUp() :
    pyautogui.mouseUp()
    sleep(delay)

def sell(x, y) :
    mouse.moveMouse(x, y)
    sleep(delay)
    mouseDown()
    mouse.moveMouse(122, 219)
    mouseUp()
    mouse.moveMouse(346, 236)
    mouseClick()
    mouseClick()
    mouseClick()
    mouse.moveMouse(312, 367)
    mouseClick()
    mouse.moveMouse(394, 296)
    mouseClick()
    sleep(delay * 2)

def sellSlot1() :
    sell(294, 98)

def sellSlot2() :
    sell(324, 96)

def sellSlot3() :
    sell(359, 92)

def sellSlot4() :
    sell(386, 92)

def sellSlot5() :
    sell(417, 95)

def itemToBank():
    mouse.moveMouse(790, 228)
    sleep(delay)
    mouseClick()
    sleep(delay)
    k.send_keys('{ENTER}')
    sleep(delay)
    k.send_keys( '{r down}' '{r up}' )
    k.send_keys( '{a down}' '{a up}' )
    k.send_keys( '{h down}' '{h up}' )
    k.send_keys( '{a down}' '{a up}' )
    k.send_keys( '{s down}' '{s up}' )
    k.send_keys( '{i down}' '{i up}' )
    k.send_keys( '{a down}' '{a up}' )
    sleep(delay)
    k.send_keys('{ENTER}')
    mouse.moveMouse(334, 119)
    sleep(delay)
    mouseDown()
    sleep(delay)
    mouse.moveMouse(117, 227)
    sleep(delay)
    mouseUp()
    mouse.moveMouse(419, 319)
    mouseClick()
    mouseClick()
    mouseClick()
    k.send_keys('{ENTER}')
    mouse.moveMouse(416, 451)
    mouseClick()
    mouse.moveMouse(499, 299)
    mouseClick()
    closeBSIfOpen()

def sellTrashItem() :
    openShop()
    for idx, (x, y) in enumerate(slot) :
        if idx == 0 :
            continue
        else :
            sell(x, y)
    print("Done Selling Trash Item.")

def openShop() :
    if not checkShop() :
        print("Shop is closed.")
        mouse.moveMouse(shop[0], shop[1])
        sleep(1)
        mouseClick()
        k.send_keys("{ENTER}")
        sleep(delay)

def buyPot() :
    openShop()
    buyItem(45, 326)
    buyItem(45, 360)
    p.keyboard.send_keys("{VK_ESCAPE}")

def buyItem(x, y) :
    mouse.moveMouse(x, y)
    sleep(delay)
    mouseDown()
    sleep(delay)
    mouse.moveMouse(slot[0][0], slot[0][1])
    sleep(delay)
    mouseUp()
    mouse.moveMouse(399, 292)
    mouseClick()
    mouse.moveMouse(307, 366)
    mouseClick()
    mouse.moveMouse(394, 299)
    mouseClick()
    sleep(delay)

def closeBSIfOpen() :
    sleep(0.1)
    print('check if bank or shop is open')
    if checkShop() :
        k.send_keys("{VK_ESCAPE}")
    if checkBank() :
        k.send_keys("{VK_ESCAPE}")

def checkBank():
    return mouse.get_freeze_dialog() == DIALOG['bank']

def checkShop():
    return mouse.get_freeze_dialog() == DIALOG['shop']

def checkItemBank():
    return mouse.get_item_bank_status() == 1

def checkInven():
    if img.checkImage("./img/item.jpg"):
        return True
    return False

def checkCash():
    if img.checkImage("./img/cash.jpg"):
        return True
    return False
