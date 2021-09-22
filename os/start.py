from config import username
from config import password
from commands import *
import sys
from termcolor import colored, cprint
clear()
if username == 'user1':
	print('The username is still set to the default, edit ./os/config.py to update the username')
	newline()
	print('	Leaving the username as the default leaves your system open to a major security risk!!!!!')
	newline()
	dismiss = input("Press enter to continue to ETC")
clear()
if password == 'password1':
	print('The password is still set to the default, edit ./os/config.py to update the password')
	newline()
	print("	Leaving the password as the default leaves your system open to a major security risk!!!!!")
	newline()
	dismiss = input("Press enter to continue to ETC")
clear()
import console