import mouseSeal as mouse
import keyboard
import pywinauto as p
from time import sleep
import macro
import imgread as img
from logger import Logger


print("cegelcmd.py")
user_id = mouse.getUserId()
inventory = []
k = p.keyboard
target = 0
force_stop = False

logger = Logger(user_id, "cegelcmd_")


def sellItem():
    logger.log("Selling Item")
    while not macro.checkShop():
        mouse.moveMouse(555, 227)
        sleep(0.5)
        macro.mouseClick()
        sleep(0.5)
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
    logger.log("escape")


def buyPotion():
    logger.log("buying potion")
    macro.buyPot()
    sleep(0.1)
    logger.log("bank : " + str(macro.checkBank()))
    logger.log("shop : " + str(macro.checkShop()))
    sleep(0.1)


def run_cegel():
    global force_stop
    macro.closeBSIfOpen()
    mouse.setTarget(target)
    # logger.log(f"target : {str(target)}")
    inventory = mouse.getItemValue()
    k.send_keys('{SPACE}')
    k.send_keys('{F1}')
    k.send_keys('{SPACE}')
    k.send_keys('{SPACE}')
    if inventory[32]['qty'] < 150 or inventory[33]['qty'] < 150:
        buyPotion()
        sleep(0.5)
    for i in range(0, 8):
        if inventory[i]['qty'] >= 250:
            logger.log('Item Full Detected.')
            sellItem()
            logger.log("Hunt Continue..")
    if keyboard.is_pressed('c'):
        logger.log('stopping.')
        force_stop = True


while True:
    if keyboard.is_pressed('-'):
        logger.log("Start Cegel Hunt..")
        force_stop = False
        i = 0
        while True:
            if force_stop:
                break
            run_cegel()
    if keyboard.is_pressed('='):
        logger.log('Script Stopped.')
        start = False
        break
    if keyboard.is_pressed("/"):
        logger.log(mouse.getCurrentTarget())
        target = mouse.getCurrentTarget()
        mouse.setTarget(mouse.getCurrentTarget())
        sleep(0.2)

    if keyboard.is_pressed(']'):
        mouse.getPosition()
        sleep(0.2)
