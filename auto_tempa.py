import mouseSeal as mouse
import keyboard
import pywinauto as p
from time import sleep
import macro
import imgread as img
import discord
from constants import *
from datetime import datetime
import auto_purchase


print("auto_tempa.py")
user_id = mouse.getUserId()
print(user_id)
# deret sini jgn di ubah
k = p.keyboard
last_atb_slot = 1
max_tempa = 11
force_stop = False

atb_purchase_qty = 20
atb_per_purchase = 15
wrs_brs_diamond_per_purchase = 5
pd_grs_per_purchase = 5


def get_inventory():
    return mouse.getItemValue()


def run_refine():
    global force_stop
    global last_atb_slot

    inventory = get_inventory()
    plus = inventory[0]['plus']

    write_file(f"current atb position : {last_atb_slot}")

    print(f"current atb position : {last_atb_slot}")
    if inventory[0]['item_id'] == 0:
        print("ITEM PECAH!!")
        discord.send_message(f"@everyone **ITEM PECAH!!** id : {user_id}")
        force_stop = True
        write_file(f"ITEM PECAH!!")
        return

    if last_atb_slot == 0:
        print("purchasing ATB")
        write_file(f"Purchasing ATB")
        status, purchase_limit = purchase_item(auto_purchase.ITEM['atb'], atb_purchase_qty)
        sleep(1.5)
        get_atb_from_bank()
        last_atb_slot = 1

    if plus < 9 and plus > 6:
        print(f"refining to {plus+1}")
        write_file(f"Refining to {plus+1}")
        refine_7_to_9(inventory)

    elif plus >= 9 and plus < max_tempa:
        print(f"refining to {plus+1}")
        write_file(f"Refining to {plus+1}")
        refine_9_to_12(inventory)

    elif plus == 12:
        print(f"SUKSES +12 BOI")
        write_file(f"SUKSES +12 BOI!!")
        discord.send_message(f"@everyone SUKSES JADI +12 BOII di id : {user_id}")

    if plus + 1 == get_item_result():
        print("SUKSES TEMPA")
        write_file(f"SUKSES TEMPA")

    if max_tempa == get_item_result():
        discord.send_message(f"@everyone SUKSES TEMPA JADI {max_tempa} di id : {user_id}")
        write_file(f"SUKSES TEMPA KE +{max_tempa}")
        force_stop = True

    if plus == 11:
        write_file(f"Item Sukses jadi +11")
        discord.send_message(f"Item sukses jadi +11 di id : {user_id}")


def refine_7_to_9(inventory):
    global force_stop

    diamond = find_item_position(DIAMOND)
    wrs = find_item_position(WRS)
    brs = find_item_position(BRS)
    qty = 0

    if not wrs:
        print("purchasing wrs")
        purchase_item(auto_purchase.ITEM['wrs'], wrs_brs_diamond_per_purchase)
        qty = qty + wrs_brs_diamond_per_purchase
        sleep(0.5)

    if not brs:
        print("purchasing brs")
        purchase_item(auto_purchase.ITEM['brs'], wrs_brs_diamond_per_purchase)
        qty = qty + wrs_brs_diamond_per_purchase
        sleep(0.5)

    if not diamond:
        print("purchasing diamond")
        purchase_item(auto_purchase.ITEM['diamond'], wrs_brs_diamond_per_purchase)
        qty = qty + wrs_brs_diamond_per_purchase
        sleep(0.5)

    if not wrs or not brs or not diamond:
        print("getting item from bank")
        get_item_from_bank(qty)
        return

    if force_stop:
        print("force_stop triggered")
        force_stop = True
        return

    mouse.moveMouse(396, 290)
    sleep(0.2)
    macro.mouseClick()
    macro.mouseClick()

    move_item(REFINE_INVENTORY[0], REFINE_ITEM)
    move_item(REFINE_INVENTORY[diamond], REFINE_GEM)
    move_item(REFINE_INVENTORY[brs], REFINE_BRS)
    move_item(REFINE_INVENTORY[wrs], REFINE_WRS)
    move_atb()

    mouse.moveMouse(203, 473)
    sleep(0.5)
    macro.mouseClick()
    sleep(8)


def refine_9_to_12(inventory):
    global force_stop

    pd = find_item_position(PD)
    grs = find_item_position(GRS)
    qty = 0

    if not pd:
        print("purchasing pd")
        purchase_item(auto_purchase.ITEM['pd'], pd_grs_per_purchase)
        qty = qty + pd_grs_per_purchase
        sleep(0.5)

    if not grs:
        print("purchasing grs")
        purchase_item(auto_purchase.ITEM['grs'], pd_grs_per_purchase)
        qty = qty + pd_grs_per_purchase
        sleep(0.5)

    if not pd or not grs:
        print("getting item from bank")
        get_item_from_bank(qty)
        sleep(0.5)
        return

    if force_stop:
        print("force_stop triggered")
        force_stop = True
        return

    mouse.moveMouse(396, 290)
    sleep(0.2)
    macro.mouseClick()
    macro.mouseClick()

    move_item(REFINE_INVENTORY[0], REFINE_ITEM)
    move_item(REFINE_INVENTORY[pd], REFINE_GEM)
    move_item(REFINE_INVENTORY[grs], REFINE_GRS)
    move_atb()

    mouse.moveMouse(203, 473)
    sleep(0.5)
    macro.mouseClick()
    sleep(8)


def find_item_position(item_id):
    inventory = get_inventory()
    for inven in inventory:
        if inven['item_id'] == item_id:
            return inven['slot']


def get_item_from_bank(qty):
    mouse.moveMouse(548, 231)
    sleep(0.5)
    macro.mouseClick()
    sleep(0.5)
    k.send_keys('{ENTER}')
    sleep(1)
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys( '{1 down}' '{1 up}' )
    k.send_keys('{ENTER}')
    sleep(0.5)
    for i in range(0, qty + 2):
        if not has_empty_slot():
            print("inven penuh batal tarik barang")
            break
        mouse.moveMouse(BANK_POSITION[i][0], BANK_POSITION[i][1])
        macro.mouseDown()
        mouse.moveMouse(380, 169)
        macro.mouseUp()
        sleep(0.2)
        k.send_keys('{ENTER}')
        sleep(0.2)

    sleep(0.5)
    mouse.moveMouse(292, 83)
    sleep(0.5)
    macro.mouseClick()


def move_item(position1, position2):
    mouse.moveMouse(position1[0], position1[1])
    sleep(0.2)
    macro.mouseDown()
    mouse.moveMouse(position2[0], position2[1])
    sleep(0.2)
    macro.mouseUp()
    sleep(0.2)


def move_atb():
    global last_atb_slot

    move_item(ITEM_CASH[last_atb_slot], REFINE_ATB)
    last_atb_slot = last_atb_slot + 1
    if last_atb_slot > atb_per_purchase:
        last_atb_slot = 0


def get_item_result():
    return get_inventory()[0]['plus']


def has_empty_slot():
    inventory = get_inventory()

    for inven in inventory:
        if inven['item_id'] == 0:
            return True


def get_atb_from_bank():
    k.send_keys(
        "{VK_LMENU down}"
        "{v down}"
        "{v up}"
        "{VK_LMENU up}"
    )
    sleep(0.3)
    k.send_keys('{ENTER}')
    sleep(0.5)
    for i in range(0, atb_purchase_qty + 1):
        mouse.moveMouse(ITEM_BANK[i][0], ITEM_BANK[i][1])
        macro.mouseDown()
        mouse.moveMouse(410, 195)
        macro.mouseUp()
        sleep(0.2)
        k.send_keys('{ENTER}')

    sleep(0.5)
    mouse.moveMouse(292, 76)
    sleep(0.5)
    macro.mouseClick()
    sleep(1)
    k.send_keys(
        "{VK_LMENU down}"
        "{a down}"
        "{a up}"
        "{VK_LMENU up}"
    )
    sleep(0.5)

def purchase_item(item_id, qty):
    global force_stop

    retry_limit = 3
    for i in range(0, retry_limit):
        status, purchase_limit, purchased_qty = auto_purchase.purchase(item_id, qty)
        if not status:
            if purchase_limit:
                force_stop = True
                discord.send_message(f"**Purchase Limit Reached** for id : {user_id}")
                return

            qty = qty - purchased_qty

            print("purchase failed")
            print(f"retrying to purchase {purchased_qty} more item")
            write_file("Purchase Failed")
            write_file(f"retrying to purchase {purchased_qty} more item")

        return

    print("Cannot purchase : something went wrong")
    write_file("Cannot purchase : something went wrong")
    discord.send_message(f"Failed Purchase : something went wrong. ID : {user_id} purchased: {purchased_qty}, remaining: qty")


def write_file(text):
    with open(f"_refine_log_{user_id}.txt", "a") as file:
        time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M')
        file.write(f"[{time}][{user_id}] {text}\n")


help_text = [
    "HOTKEYS: ",
    "[-] start refine",
    "[c] force stop (tahan tombolnya aja sampe berenti)",
    "[/] set atb position (pake kalo atbnya error aja)",
    "[=] print mouse position"
]

settings = [
    "SETTINGS : ",
    f"atb_purchase_qty: {atb_purchase_qty}",
    f"atb_per_purchase: {atb_per_purchase}",
    f"wrs_brs_diamond_per_purchase: {wrs_brs_diamond_per_purchase}",
    f"pd_grs_per_purchase: {pd_grs_per_purchase}",
    "\nFOR PURCHASE: ",
    f"username: {auto_purchase.username}",
    f"password: {auto_purchase.password}",
    f"password_bank: {auto_purchase.password_bank}",
]
print("\n")
print("\n".join(settings))
print("\n")
print("\n".join(help_text))

while True:
    if keyboard.is_pressed('-'):
        sleep(0.5)
        while True:
            run_refine()
            if force_stop:
                force_stop = False
                break

            if keyboard.is_pressed('c'):
                print("stopping")
                break

    if keyboard.is_pressed("="):
        print(mouse.getPosition())
        sleep(0.5)

    if keyboard.is_pressed("/"):
        last_atb_slot = int(input("atb_slot : ") or 1)
        sleep(0.5)
