import os
import mouseSeal as mouse
import keyboard
import pywinauto as p
from time import sleep
import macro
import imgread as img
from constants import *


print(os.path.basename(__file__))
print(mouse.getUserId())
inventory = []
k = p.keyboard
target = 0


def sellItem(item_list):
    print('Selling Item..')
    mouse.moveMouse(555, 227)
    sleep(0.5)
    macro.mouseClick()
    sleep(0.5)
    while mouse.get_freeze_dialog() != DIALOG['shop']:
        k.send_keys('{ENTER}')
        sleep(0.5)
        mouse.moveMouse(394, 296)
        macro.mouseClick()
        sleep(0.5)
    sleep(0.5)

    for item in item_list:
        macro.sell(SELL_INVENTORY[item][0], SELL_INVENTORY[item][1])

    close_item_shop()
    sleep(1)
    print("escape")


def buyPotion() :
    macro.buyPot()
    sleep(0.1)
    print("bank : " + str(macro.checkBank()))
    print("shop : " + str(macro.checkShop()))
    sleep(0.1)


def check_potion(inventory):
    for inven in inventory:
        if inven['item_id'] == POT_MERAH or inven['item_id'] == POT_BIRU:
            if inven['qty'] <= 75:
                buyPotion()


def check_item(inventory):
    dont_sell = [SRS, NS, POT_MERAH, POT_BIRU]
    dont_sell.extend(CANNOT_SELL_ITEMS)
    item_list = []
    equipments = []
    for inven in inventory:
        if inven['item_id'] not in dont_sell:
            print("check ini")
            if inven['qty'] >= 250:
                print("check qty")
                item_list.append(inven['slot'])

            if inven['item_id'] != 0 and inven['qty'] == 0:
                print("check equipment")
                equipments.append(inven['slot'])

    if len(equipments) > 5:
        item_list.extend(equipments)

    if len(item_list):
        print('Item Full Detected.')
        sellItem(item_list)
        print("Hunt Continue..")


def check_srs_ns(inventory):
    should_move = [SRS, NS]
    item_list = []
    for inven in inventory:
        if inven['item_id'] in should_move:
            item_list.append(inven['slot'])

    if len(item_list) > 5:
        move_to_bank(item_list)


def move_to_bank(item_list):
    open_bank()
    for item in item_list:
        mouse.moveMouse(BANK_INVENTORY[item][0], BANK_INVENTORY[item][1])
        sleep(0.5)
        mouseDown()
        sleep(0.5)
        mouse.moveMouse(117, 227)
        sleep(0.5)
        mouseUp()
        mouse.moveMouse(419, 319)

    mouse.moveMouse(499, 299)
    mouseClick()
    close_bank()


def close_bank():
    while mouse.get_freeze_dialog() == DIALOG['bank']:
        k.send_keys("{VK_ESCAPE}")
        sleep(0.5)

def close_item_shop():
    while mouse.get_freeze_dialog() == DIALOG['shop']:
        k.send_keys("{VK_ESCAPE}")
        sleep(0.5)


def open_bank():
    while mouse.get_freeze_dialog() != DIALOG['bank']:
        mouse.moveMouse(790, 228)
        sleep(0.5)
        mouseClick()
        sleep(0.5)
        k.send_keys('{ENTER}')
        sleep(0.5)

    # password
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys( '{1 down}' '{1 up}' )
    sleep(0.5)
    k.send_keys('{ENTER}')


def start_hunt():
    mouse.moveMouse(391, 325)
    k.send_keys('{q down}' '{q up}')
    k.send_keys('{SPACE}')
    k.send_keys('{F1}')
    k.send_keys('{F2}')
    k.send_keys('{F3}')
    sleep(1)
    k.send_keys('{SPACE}')
    k.send_keys('{SPACE}')
    k.send_keys('{SPACE}')
    k.send_keys('{SPACE}')
    macro.mouseClick()

while True:
    if keyboard.is_pressed('-') :
        print("Start Spam Hunt..")
        while True:
            start_hunt()

            inventory = mouse.getItemValue()
            check_potion(inventory)
            check_srs_ns(inventory)
            check_item(inventory)

            if keyboard.is_pressed('c') :
                print('stopping.')
                break

    if keyboard.is_pressed(']'):
        print(mouse.getPosition())
        sleep(0.2)