import sys
import time

def decrypting(Final_encrypted):
    listhex = [Final_encrypted[i:i+2] for i in range(0, len(Final_encrypted), 2)]
    listint = []
    declol = []
    decOrd_Val = []
    a = ord("a")   #change if it will be different coding
    Index_Value = 0
    Amount_Chars = 0
    decValue = []
    stringdecValue = ""
    for i in range(0, len(listhex)):
        string = str(listhex[i])
        first_char = string[0:1]
        Amount_Chars += 1
        if (first_char == '0'):
            listhex[i] = string[1:]
        listint.append(int(listhex[i], 16))
        if Index_Value == 0:
            declol.append(deGGGotate(listint[Index_Value]))
            decOrd_Val.append(declol[Index_Value] ^ int(a))
            decValue.append(chr(decOrd_Val[Index_Value]))
            Index_Value += 1
        else:
            declol.append(deGGGotate(listint[Index_Value]))
            decOrd_Val.append(listint[Index_Value-1] ^ declol[Index_Value])
            decValue.append(chr(decOrd_Val[Index_Value]))
            Index_Value += 1
    for i in decValue:
        stringdecValue = stringdecValue + i
    print("decrypted message is: " + stringdecValue)
def deGGGotate(value):
    xbit = (value & 1)  << 7
    return(value >> 1) | xbit

def sign():
    title = '''
░█████╗░██╗░░░██╗░██╗░░░░░░░██╗░█████╗░██████╗░  ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░██████╗░
██╔══██╗╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝░╚████╔╝░░╚██╗████╗██╔╝███████║██████╔╝  ██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║██████╔╝
██║░░██╗░░╚██╔╝░░░░████╔═████║░██╔══██║██╔══██╗  ██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║  ██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝'''
    sign2 = '''
█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   █▀ █ █▀ █ █▀▄ █▀█ █▀█
█▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▄█ ░█░   ▄█ █ ▄█ █ █▄▀ █▄█ █▀▄

'''
    sign = '''
█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   █▀ █ █▀ █ █▀▄ █▀█ █▀█ █▄▄ █▀█
█▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▄█ ░█░   ▄█ █ ▄█ █ █▄▀ █▄█ █▀▄ █▄█ ▀▀█

'''
    print(bcolors.OKCYAN + title)
    print(bcolors.WARNING + sign)

class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'

def main():
    sign()

    Final_encrypted = input(bcolors.HEADER + "Enter your crypted value: ")
    decrypting(Final_encrypted)


if __name__ == '__main__':
    main()

