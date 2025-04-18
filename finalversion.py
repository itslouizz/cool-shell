import os
import webbrowser
import sys
import subprocess
import socket
from getpass import getpass

def masked_input(prompt):
    import msvcrt
    print(prompt, end='', flush=True)
    chars = []
    while True:
        ch = msvcrt.getch()
        if ch == b'\r':
            print()
            break
        elif ch == b'\x08':
            if chars:
                chars.pop()
                print('\b \b', end='', flush=True)
        else:
            chars.append(ch)
            print('*', end='', flush=True)
    return b''.join(chars).decode('utf-8')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_info():
    clear()
    print("\033[31mWork in progress\nOnly for educational purposes\nJoin Discord: https://discord.gg/tvnVMwrhnC\033[0m")
    input("\nPress Enter to continue...")

def basic_multitool():
    while True:
        clear()
        choice = input("\033[31mBasic Multitool\n--\n[1] Calculator\n[2] Ping URL\n[3] Back\n~~> \033[0m")
        
        if choice == "1":
            clear()
            try:
                expr = input("Enter calculation (e.g., 2+2): ")
                print("Result:", eval(expr))
            except:
                print("Invalid calculation")
            input("\nPress Enter to continue...")
        elif choice == "2":
            clear()
            url = input("Enter URL to ping: ")
            try:
                param = '-n' if os.name == 'nt' else '-c'
                subprocess.run(['ping', param, '4', url])
            except:
                print("Ping failed")
            input("\nPress Enter to continue...")
        elif choice == "3":
            break

def port_scanner():
    clear()
    target = input("Enter URL or IP to scan: ")
    try:
        target_ip = socket.gethostbyname(target)
        print(f"\nScanning {target} ({target_ip})")
        print("Common ports scan may take a moment...\n")
        
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")
            sock.close()
    except:
        print("Invalid target or connection error")
    input("\nPress Enter to continue...")

def hacks_menu():
    while True:
        clear()
        choice = input("\033[31mHacks Menu\n--\n[1] Port Scanner\n[2] Coming soon\n[3] Back\n~~> \033[0m")
        if choice == "1":
            port_scanner()
        elif choice == "3":
            break

while True:
    clear()
    try:
        if os.name == 'nt':
            key = masked_input("\033[31mLicense Key: \033[0m")
        else:
            key = getpass("\033[31mLicense Key: \033[0m")
    except:
        key = input("\033[31mLicense Key: \033[0m")
        
    if key == "karla":
        break

def options_menu():
    while True:
        clear()
        choice = input("\033[31mOptions Menu\n--\n[1] Info\n[2] Basic Multitool\n[3] Hacks\n[4] exsample 4\n[5] exsample 5\n[6] exsample 6\n[7] exsample 7\n[8] exsample 8\n[9] exsample 9\n[10] exsample 10\n[11] Back\n~~> \033[0m")
        
        if choice == "1":
            show_info()
        elif choice == "2":
            basic_multitool()
        elif choice == "3":
            hacks_menu()
        elif choice == "11":
            break
        elif choice in [str(x) for x in range(4, 11)]:
            pass

while True:
    clear()
    choice = input("\033[31mcool shell 0.09\n--\n[1] Options\n[2] Discord\n[3] Exit\n~~> \033[0m")
    
    if choice == "1":
        options_menu()
    elif choice == "2":
        webbrowser.open("https://discord.gg/tvnVMwrhnC")
    elif choice == "3":
        sys.exit(0)