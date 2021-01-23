import mouseSeal as mouse
import keyboard
from time import sleep
import macro
import pywinauto as p
import datetime

start = True
k = p.keyboard

macro = [553, 234]
item = [550, 51]
char_tegah = [399, 304]
char_party = [50, 27]
inven_inden = [340, 147]
slot_inden = [295, 167]
tombol_ok = [167, 323]

#ganti pake key code
hotkey = {
    "macro" : "1",
    "item" : "2",
    "char_tegah" : "3",
    "char_party" : "4",
    "inven_inden" : "5",
    "slot_inden" : "6",
    "tombol_ok" : "7",
}

stop = False
print("Inden jibit Ready")
while start:
    if keyboard.is_pressed(hotkey.macro) : mouse.moveMouse(macro[0], macro[1]) #macro
    if keyboard.is_pressed(hotkey.item) : mouse.moveMouse(item[0], item[1]) #item
    if keyboard.is_pressed(hotkey.char_tegah) : mouse.moveMouse(char_tengah[0], char_tengah[1]) #char tengah
    if keyboard.is_pressed(hotkey.char_party) : mouse.moveMouse(char_party[0], char_party[1]) #char party
    if keyboard.is_pressed(hotkey.inven_inden) : mouse.moveMouse(inven_inden[0], inven_inden[1]) #inven inden
    if keyboard.is_pressed(hotkey.slot_inden) : mouse.moveMouse(slot_inden[0], slot_inden[1]) #slot inden
    if keyboard.is_pressed(hotkey.tombol_ok) : mouse.moveMouse(tombol_ok[0], tombol_ok[1]) #tengah bwt klik ok

    #bwt dapetin posisi mouse sekarang
    if keyboard.is_pressed("]") : 
        mouse.getPosition()
        print("OPT Found")
        sleep(0.1)
    
    
    status = mouse.getItemStatus()
    text = (
        "\ntime " + str(datetime.datetime.today()) + "\n"
        "mpw : " + str(status.mpw) + "\n"
        "defend : " + str(status.defend) + "\n"
        "mspd : " + str(status.mspd) + "\n"
        "hp : " + str(status.hp) + "\n"
        "dmg : " + str(status.dmg) + "\n"
    )
    print(text)
    if status.hp >= 3 :
        print("Opt Found")
        stop = True
    if stop == True :
        print("OPT Found")
        start = False
        break