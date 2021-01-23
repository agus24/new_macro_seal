import win32process
import win32api
import pymem
import helper
import sys
import time
import itemStatus

def getProcess():
    processes = pymem.process.list_processes()
    for value in processes:
        if value.szExeFile == b'SO3D.exe':
            return value
        pass

pm = pymem.Pymem()
process = getProcess()
pid = process.th32ProcessID
#pid = 672
pc = pymem.process.open(pid)

baseAddressMouse = int(0x400000) + int(0x00DD5F24)
baseAddressStat = int(0x400000) + int(0x003DA400)
pointerMouse = pymem.memory.read_int(pc, baseAddressMouse)
pointerStat = pymem.memory.read_int(pc, baseAddressStat)

mouseX = (pointerMouse) + int(0x2c0)
mouseY = (pointerMouse) + int(0x2c4)

mpw = (pointerStat) + int(0x450)
defend = (pointerStat) + int(0x454)
mspd = (pointerStat) + int(0x468)
hp = (pointerStat) + int(0x46c)

def moveMouse(x, y):
    pymem.memory.write_short(pc, mouseX, x)
    pymem.memory.write_short(pc, mouseY, y)

def getPosition():
    print("X: " + str(pymem.memory.read_short(pc, mouseX)))
    print("Y: " + str(pymem.memory.read_short(pc, mouseY)))

def getStatList():
    print("mpw : " + str(pymem.memory.read_short(pc, mpw)))
    print("defend : " + str(pymem.memory.read_short(pc, defend)))
    print("mspd : " + str(pymem.memory.read_short(pc, mspd)))
    print("hp : " + str(pymem.memory.read_short(pc, hp)))

def makeStatHp(value):
    print("hp : "+value)

def forcePid(identifier):
    pid = identifier

def getItemQty():
    slot_1 = (pointerStat) + 1056
    slot_2 = (pointerStat) + 1056 + 116
    slot_3 = (pointerStat) + 1056 + 116 + 116
    slot_4 = (pointerStat) + 1056 + 116 + 116 + 116
    slot_5 = (pointerStat) + 1056 + 116 + 116 + 116 + 116

    sys.stdout.write(
        "slot : " + str(pymem.memory.read_short(pc, slot_1)) +
        "  slot : " + str(pymem.memory.read_short(pc, slot_2)) +
        "  slot : " + str(pymem.memory.read_short(pc, slot_3)) +
        "  slot : " + str(pymem.memory.read_short(pc, slot_4)) +
        "  slot : " + str(pymem.memory.read_short(pc, slot_5)) + "\r"
    )
    sys.stdout.flush()
    # print("slot : 300")
    
def getPid():
    return pid

def setPid(id):
    pid = pid
    pc = pymem.process.open(pid)

def getItemValue():
    item = []
    for i in range(0, 40):
        calc = (pointerStat) + 1056 + (116 * i)
        item.append({
            "slot": i,
            "address": calc,
            "qty": pymem.memory.read_short(pc, calc),
            "plus": pymem.memory.read_short(pc, calc - 8),
            "item_id": pymem.memory.read_short(pc, calc - 12)
        })
    return item

def getUserId():
    baseAddr = int(0x400000) + int(0x003DB34C)
    pointer = pymem.memory.read_int(pc, baseAddr)
    print(pointer)
    idAddress = pointer + int(0x1268)
    return  pymem.memory.read_string(pc, idAddress, 16)

def spamSkill():
    baseAddr = int(0x400000) + int(0x003DB34C)
    pointer = pymem.memory.read_int(pc, baseAddr)
    spamAddr = pointer + int(0x1D00)
    val = pymem.memory.write_int(pc, spamAddr, 3)

def getItemStatus():
    mpw = (pointerStat) + int(0x450)
    defend = (pointerStat) + int(0x454)
    mspd = (pointerStat) + int(0x468)
    hp = (pointerStat) + int(0x46c)
    dmg = (pointerStat) + int(0x44c)

    status = itemStatus.item(
        mpw = pymem.memory.read_short(pc, mpw),
        defend = pymem.memory.read_short(pc, defend),
        mspd = pymem.memory.read_short(pc, mspd),
        hp = pymem.memory.read_short(pc, hp),
        dmg = pymem.memory.read_short(pc, dmg),
    )
    return status

def setTarget(target):
    baseAddr = int(0x400000) + int(0x00DE3250)
    pymem.memory.write_int(pc, baseAddr, target)

def getCurrentTarget():
    baseAddr = int(0x400000) + int(0x003DB34C)
    pointer = pymem.memory.read_int(pc, baseAddr)
    addr = pointer + int(0x1260)
    return pymem.memory.read_int(pc, addr)

def scan(data):
    module = pymem.ressources.structure.MODULEINFO(pc)
    pymem.pattern.scan_pattern_page(pc, module, data)