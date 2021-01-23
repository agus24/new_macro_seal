import mouseSeal as mouse
import keyboard
from time import sleep
import macro
import pywinauto as p
import datetime

start = True
k = p.keyboard

def runInden() :
    run = True
    delay = 0.05
    i = 0
    while run :
        if macro.checkCash() != True :
            k.send_keys(
                "{VK_LMENU down}"
                "{a down}"
                "{a up}"
                "{VK_LMENU up}"
            )
        if macro.checkInven() != True :
            k.send_keys(
                "{VK_LMENU down}"
                "{i down}"
                "{i up}"
                "{VK_LMENU up}"
            )
        mouse.moveMouse(553, 234)
        macro.mouseClick()
        sleep(delay)
        mouse.moveMouse(550, 51)
        sleep(delay)
        macro.mouseClick()
        sleep(delay)
        k.send_keys("{ENTER}")
        mouse.moveMouse(396, 290)
        sleep(delay)
        macro.mouseClick()
        sleep(delay)
        mouse.moveMouse(50, 27)
        sleep(delay)
        macro.mouseClick()
        sleep(delay)
        mouse.moveMouse(48, 374)
        sleep(delay)
        macro.mouseClick()
        sleep(delay)
        mouse.moveMouse(340, 147)
        sleep(delay)
        macro.mouseDown()
        sleep(delay)
        mouse.moveMouse(295, 167)
        sleep(delay)
        macro.mouseUp()
        sleep(delay)
        mouse.moveMouse(167, 323)
        sleep(delay)
        macro.mouseClick()
        sleep(delay)
        k.send_keys(
            "{ENTER}"
            "{ENTER}"
        )
        sleep(delay)
        if keyboard.is_pressed("c") :
            run = False
            print("stop")
            pass
        if i >= 2000 :
            print("stop")
            run = False
        i = i+1
        # k.send_keys(
        #     "{VK_LMENU down}"
        #     "{i down}"
        #     "{i up}"
        #     "{a down}"
        #     "{a up}"
        #     "{VK_LMENU up}"
        # )
        sleep(0.5)
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
        f = open("stats/inden.txt", "a")
        f.write(text)
        f.close()
        if status.hp >= 3 :
            print("Opt Found")
            run = False

print("ready..")
while start:
    if keyboard.is_pressed("-") :
        runInden()
    if keyboard.is_pressed("]") :
        mouse.getPosition()
        sleep(0.1)
