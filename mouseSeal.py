import ctypes
import re
import win32process
import win32api
import pymem
import helper
import sys
import time
import itemStatus
import threading
import struct


# from scanner import AddressScan

def getProcess():
    processes = pymem.process.list_processes()
    for value in processes:
        if value.szExeFile == b'SO3D.exe':
            return value
        pass

pm = pymem.Pymem("SO3D.exe")
process = getProcess()
pid = process.th32ProcessID
#pid = 672
pc = pymem.process.open(pid)
module = pm.process_base

scan_result = []
# print(dir(pm.process_base))

# print(
#     pm.process_base.lpBaseOfDll,
#     pm.process_base.SizeOfImage,
#     pm.process_base.EntryPoint
# )

# print(module)

baseAddressMouse = int(0x400000) + int(0x00DD5F24)
baseAddressStat = int(0x400000) + int(0x003DA400)
pointerMouse = pm.read_int(baseAddressMouse)
pointerStat = pm.read_int(baseAddressStat)

mouseX = (pointerMouse) + int(0x2c0)
mouseY = (pointerMouse) + int(0x2c4)

mpw = (pointerStat) + int(0x450)
defend = (pointerStat) + int(0x454)
mspd = (pointerStat) + int(0x468)
hp = (pointerStat) + int(0x46c)


def moveMouse(x, y):
    pm.write_short(mouseX, x)
    pm.write_short(mouseY, y)


def getPosition():
    print("(x, y)")
    print(f"({pm.read_short(mouseX)}, {pm.read_short(mouseY)})")


def getStatList():
    print("mpw : " + str(pm.read_short(mpw)))
    print("defend : " + str(pm.read_short(defend)))
    print("mspd : " + str(pm.read_short(mspd)))
    print("hp : " + str(pm.read_short(hp)))


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
        "slot : " + str(pm.read_short(slot_1)) +
        "  slot : " + str(pm.read_short(slot_2)) +
        "  slot : " + str(pm.read_short(slot_3)) +
        "  slot : " + str(pm.read_short(slot_4)) +
        "  slot : " + str(pm.read_short(slot_5)) + "\r"
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
            "qty": pm.read_short(calc),
            "plus": pm.read_short(calc - 8),
            "item_id": pm.read_short(calc - 12)
        })
    return item


def getUserId():
    baseAddr = int(0x400000) + int(0x003DB34C)
    pointer = pm.read_int(baseAddr)
    print(pointer)
    idAddress = pointer + int(0x1268)
    return  pm.read_string(idAddress, 16)


def spamSkill():
    baseAddr = int(0x400000) + int(0x003DB34C)
    pointer = pm.read_int(baseAddr)
    spamAddr = pointer + int(0x1D00)
    val = pm.write_int(spamAddr, 3)


def getItemStatus():
    mpw = (pointerStat) + int(0x450)
    defend = (pointerStat) + int(0x454)
    mspd = (pointerStat) + int(0x468)
    hp = (pointerStat) + int(0x46c)
    dmg = (pointerStat) + int(0x44c)

    status = itemStatus.item(
        mpw = pm.read_short(mpw),
        defend = pm.read_short(defend),
        mspd = pm.read_short(mspd),
        hp = pm.read_short(hp),
        dmg = pm.read_short(dmg),
    )
    return status


def setTarget(target):
    baseAddr = int(0x400000) + int(0x00DE3250)
    pm.write_int(baseAddr, target)


def getCurrentTarget():
    baseAddr = int(0x400000) + int(0x003DB34C)
    pointer = pm.read_int(baseAddr)
    addr = pointer + int(0x1260)
    return pm.read_int(addr)


def get_freeze_dialog():
    baseAddr = int(0x400000) + int(0x003C1C34)
    return pm.read_int(baseAddr)


def set_freeze_dialog(value):
    baseAddr = int(0x400000) + int(0x003C1C34)
    pm.write_int(baseAddr, value)


def get_item_bank_status():
    baseAddr = int(0x400000) + int(0x00DAAE78)
    return pm.read_int(baseAddr)


def scan_module(pattern):
    print(pymem.ressources.structure.MEMORY_BASIC_INFORMATION)
    return pymem.pattern.pattern_scan_module(pm.process_handle, module, pattern)

def scan_memory(value):
    base_address = module.lpBaseOfDll
    max_address = module.lpBaseOfDll + module.SizeOfImage
    page_address = base_address

    found_address = []
    while page_address < max_address:
        next_page, found = memory_scan(page_address, value)
        if found:
            found_address.extend(found)
        page_address = next_page

    return found_address

def memory_scan(address, value):
    mbi = pymem.memory.virtual_query(pm.process_handle, address)
    next_region = mbi.BaseAddress + mbi.RegionSize
    allowed_protections = [
        pymem.ressources.structure.MEMORY_PROTECTION.PAGE_EXECUTE_READ,
        pymem.ressources.structure.MEMORY_PROTECTION.PAGE_EXECUTE_READWRITE,
        pymem.ressources.structure.MEMORY_PROTECTION.PAGE_READWRITE,
        pymem.ressources.structure.MEMORY_PROTECTION.PAGE_READONLY,
    ]
    if mbi.state != pymem.ressources.structure.MEMORY_STATE.MEM_COMMIT or mbi.protect not in allowed_protections:
        return next_region, None

    found_address = []

    pattern = struct.pack('@i', value)
    i = 0
    while i < mbi.RegionSize:
        if pm.read_int(address + i) == value:
            found_address.append(address + i)
        i += 4

    # if match:
    #     found = address + match.span()[0]

    return next_region, found_address


def read_bytes(handle, address, byte):
    buff = ctypes.create_string_buffer(byte)
    bytes_read = ctypes.c_size_t()
    ctypes.windll.kernel32.SetLastError(0)
    pymem.ressources.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(address), buff, byte, ctypes.byref(bytes_read))

    # print(buff.raw)
    print(buff.value)
    # print(help(buff))
    return buff.raw

# def memory_scan(value, scan_type="4bytes"):
#     global scan_result
#     scan_result = []
#     address = pm.process_base.lpBaseOfDll
#     end = pm.process_base.SizeOfImage
#     step = 4
#     value = int(value)

#     chunk_1 = address
#     chunk_position = int((end - address) / 2)
#     chunk_2 = chunk_position

#     addresses = chunk_address(start=address, end=end, chunk=1000)

#     print(chunk_1)
#     print(chunk_position)
#     print(chunk_2)
#     print(f"addresses : {addresses}")
#     print(f"search value = {value}\n")
#     input("press any key to start")
#     found_address = []
#     thread_list = []

#     for address in addresses:
#         thread_list.append(threading.Thread(target=address_scan, args=[address['start'], address['end'], value, 4]))

#     print(dir(thread_list[0]))
#     print(thread_list)

#     for thread in thread_list:
#         thread.start()

#     for thread in thread_list:
#         thread.join()

#     print(scan_result)

#     return found_address

def address_scan(start, end, value, step=4):
    global scan_result

    found_address = []
    while start <= end:
        try:
            searched = pm.read_int(start)
            if value == pm.read_int(start):
                scan_result.append(start)
                print(f"address found : {start}")

            f = open("_scan_result.txt", "a")
            f.write(f"value : {value} | searched : {searched}\n")
            f.close()

            start = start + step
        except pymem.exception.MemoryReadError:
            continue

    return found_address

def chunk_address(start, end, chunk=4):
    chunk_count = int((end - start) / chunk)

    last_address = start
    addresses = []
    for i in range(0, chunk):
        end = last_address + chunk_count
        addresses.append({
            "start": last_address,
            "end": end
        })
        last_address = end
    
    return addresses


def get_percentage_of_address(end, current):
    result = current / end
    return result

def parse_type(scan_type):
    if scan_type == "4bytes":
        return 4
    elif scan_type == "bytes":
        return 1
    elif scan_type == "2bytes":
        return 2
    elif scan_type == "float":
        return 4