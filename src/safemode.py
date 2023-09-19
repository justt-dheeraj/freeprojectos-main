# code by audiotore (github)

import os
import time
import utils

login_pass = open('user/password.pass')
login_name = open('user/username.pass')
l_p = login_pass.read()
l_u = login_name.read()

utils.cls()
print("Okay!")
utils.cls()
print("Booting into safemode")
time.sleep(3)
print("Booted!")

utils.cls()

print("FREEProjectOS [REPAIR MODE]")
print("Type [help] to get some REPAIR commands.")
print("") # Space.

while True:
	command = input(str(">>>: "))

	if command == 'help':
		print("execute.antivirus [alpha] - Executes antivirus")
		print("reset.username - Reset username to something else.")
		print("reset.password - Reset password to something else.")
		print("about.safemode - Information about safemode.")
		print("reboot - reboot the system.")
		print("shutdown - shutdown the system.")
		print("clear - clear the screen.")

	elif command == 'execute.antivirus':
		print("Scanning... (May take a bit)")
		time.sleep(15)

		path = 'Kernel.py'
		path2 = 'home.py'
		path3 = 'file.py'
		path4 = 'edit.py'
		path5 = 'brows.py'

		check_file = os.path.isfile(path)
		check_file2 = os.path.isfile(path2)
		check_file3 = os.path.isfile(path3)
		check_file4 = os.path.isfile(path4)
		check_file5 = os.path.isfile(path5)

		if check_file and check_file2 and check_file3 and check_file4 and check_file5 == True:
			print("Scanning complete!")
			print("No viruses found!")

		else:
			print("Virus detected! BREAKING!")
			print("Always make sure you download FreeProjectOS from the offical link!")
			print("In this case do these steps: ")
			print("1. delete FREEProjectOS from the desktop entirely!")
			print("2. Download from the offical link of FREEProjectOS.")
			time.sleep(10)
			exit() # Break from the OS.

	elif command == 'reset.username':
		print("Please confirm your username.")

		while True:
			username_change = input(str("current username: "))

			if username_change == l_u:
				print("vaild!")
				username_change2 = input(str("new username: "))

				# Erase username.pass and replace it with the
				# new username :)
				with open('user/username.pass', 'w') as f:
					f.writelines(username_change2)

				print("username changed successfully!")
				print("Press [Enter] to apply changes.")
				input()
				os.startfile("safemode.py")
				exit()
				

			else:
				print("Wrong username try again!")

	elif command == 'reset.password':
		print("Please confirm your password.")

		while True:
			password_change = input(str("current password: "))

			if password_change == l_p:
				print("vaild!")
				password_change2 = input(str("new password: "))

				# Samething as password.
				with open('user/password.pass', 'w') as f:
					f.writelines(password_change2)

				print("password changed successfully!")
				print("Press [Enter] to apply changes.")
				input()
				os.startfile("safemode.py")
				exit()

			else:
				print("Wrong password try again!")

	elif command == 'about.safemode':
		print("Safemode otherwise known as \"FreeProjectOSPE\"")
		print("Is an bare bones version of the regular OS")
		print("\"FreeProjectOS\". FreeProjectOSPE is designed to be")
		print("a backup OS to help repair FreeProjectOS (the main OS).")
		print("") # Space.
		print("Tip: Always run a antivirus once a week.")
		print("") # Space.

	elif command == 'clear':
		utils.cls()
		print("FREEProjectOS [REPAIR MODE]")
		print("Type [help] to get some REPAIR commands.")
		print("") # Space.

	elif command == 'shutdown':
		print("System is going down!")
		print("Shutting down..")
		time.sleep(2)
		break		

	elif command == 'reboot':
		utils.cls()
		print("REBOOTING...")
		time.sleep(2)
		os.startfile('Kernel.py')
		break

	else:
		print("Invaild command!")