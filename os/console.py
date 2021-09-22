from typing import NamedTuple
from config import username
from config import password

print("Starting ETC")
print("Loading Values")
true = "true"
false = "false"
null = "null"
startuplogin = true
inputusername = null
inputpassword = null
loop = true
global passondata
errordefualt = "Press enter to return to the console"
osversion = "0.0.2"
print("Loading Additional Packages")
import os
print("Defining Definitions")
from commands import *
def vardump():
    print("Var Dump: " + str(passondata) + str(" ") + str(input))

def systemapp():
    if passondata == "help":
        newline()
        print("List of commands:")
        newline()
        print("help | Displays a list of commands")
        print("help_adv | Displays a list of advanced commands (requires mouse to scroll)")
        print("version | Displays the version of ETC that you are currently using")
        print("shutdown | Shutdown ETC")
        print("reboot | Reboot ETC")
        print("credits | Displays credits")
        print("clear | Clears the screen")
        newline()
    elif passondata == "credits":
        newline()
        print('Third Party Tools:')
        print(' Termcolor | Volvox Development Team (c)')
        print('ETC Development Team:')
        print(' github/bcat1023')
        newline()
        print('Thanks to all the people who helped to create ETC')
    elif passondata == "clear":
        clear()
    elif passondata == "version":
        newline()
        print("Your running ETC: " + str(osversion))
        newline()
    elif passondata == "shutdown":
        newline()
        print("Shutting down...")
        quit()
    elif passondata == "program404":
        newline()
        print("The application could not be found in /os/apps")
        vardump()
        input(errordefualt)
        newline()
    elif passondata == "reboot":
        newline()
        print("Rebooting...")
        clear()
        os.system("python ./start.py")
        quit()
    elif passondata == "help_adv":
        newline()
        print('Sorry this feature isn\'t ready quite yet')
        print("An error within a internal system app occurred and the application has closed, you have been returned to the console")
        vardump()
        input(errordefualt)
    else:
        print("An error within a internal system app occurred and the application has closed, you have been returned to the console")
        vardump()
        input(errordefualt)

def error():
    print("An error within a internal system app occurred and the application has closed, you have been returned to the console")
    vardump()
    input(errordefualt)

def consoleload():
    clear()
    print("Welcome " + str(username) + str(" Type \"help\" to see a list of commands"))
    while loop:
        command = input(username + str(": "))
        global passondata
        passondata = command
        systemapp()


def credintialsend():
    clear()
    print("Loading...")
    clear()
    print("Logged in")
    print("Prepering Console")
    consoleload()


def login():
    print("Please log into your account")
    login = "true"
    while login:
        inputusername = input("Enter your username: ")
        if inputusername == username:
            inputpassword = input("enter your password: ")
            if inputpassword == password:
                clear()
                print("Loading..")
                credintialsend()
                login = "false"
            else:
                print("Incorrect Password")
        else:
            print("Incorrect username")
print("Preparing ETC")
while startuplogin:
    print("Starting ETC Session")
    login()
    startuplogin = "false"
