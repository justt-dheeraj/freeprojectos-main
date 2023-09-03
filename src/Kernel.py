# code by audiotore (github)

import time
import os
import utils

# Always execute KernelOS.py to start the OS.
# This contains our setup including setting up basic
# stuff like our username and password.

# If we are developing KernelOS then executing it manually by the
# cmd would be fine because when you get an error message it won't
# Close giving you no time to read the error message and which line
# python doesn't like.

utils.cls() # Just in case theres any gunk before the OS starts.
print("Booting.")
time.sleep(1)
print("Booting..")
time.sleep(1)
print("Booting...")
time.sleep(1)

utils.cls()
print("""

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
███████╗██████╗░███████╗███████╗██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗░█████╗░░██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
█████╗░░██████╔╝█████╗░░█████╗░░██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░██║░░██║╚█████╗░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║███████╗███████╗██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═════╝░
""")

time.sleep(5)
utils.cs()
print("""
[1] Safe mode. (FreeProjectOS PE)
[2] Boot normally.
""")

safeselect = input(str(">>>: "))

if safeselect == '1':
	print("Okay!")
	os.startfile("safemode.py")
	exit()

if safeselect == '2':
	print("Okay!")
	time.sleep(1)
	utils.cls()
	# Move on and continue booting kernelOS.

# The proper way of booting kernelOS really is clicking on the py file.
# "KernelOS.py"

print("""
███████╗██████╗░███████╗███████╗██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗░█████╗░░██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
█████╗░░██████╔╝█████╗░░█████╗░░██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░██║░░██║╚█████╗░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║███████╗███████╗██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═════╝░""")

print("""
[1] Continue with setup.
[2] I've already done the setup.
""")

setup = input("[?]: ")

if setup == '1':
	name = input(str("Please enter your User Name To Be Displayed: "))
	pas = input(str("Please enter your Password to login: "))

	lines = [name]
	# Using "pass" as the extension type to provide some level of encryption.
	# Since file explorer by default doesn't recongize pass as a text file.
	with open('user/username.pass', 'w') as f:
		f.writelines(lines)

	lines2 = [pas]
	with open('user/password.pass', 'w') as f:
		f.writelines(lines2)

	print("") # Space.
	print("Would you like to enable Virtual Aassistant?")
	print("[Yes/No] Type y for yes and n for no (no capital letters)")

	while True:
		virtual = input(str(">>>: "))

		if virtual == "y":
			with open('user/virtual.txt', 'w') as f:
				f.writelines("1")

			print("Okay!")
			print("Done!")
			break

		elif virtual == "n":
			with open('user/virtual.txt', 'w') as f:
				f.writelines("0")

			print("Okay!")
			print("Noted.")
			break

		else:
			print("Invaild command sorry!")

	print("FreeProjectOS setup complete!")
	print("Redirecting you to home...")
	input("Press Enter to Close Window: ")

if setup == '2':
	# Read our username and password
	# Like a goodboy.
	login_pass = open('user/password.pass')
	login_name = open('user/username.pass')
	l_p = login_pass.read()
	l_u = login_name.read()

	while True:
			login = input(str("Please Enter The Password To " + l_u + ": "))
			if login == l_p:
				os.startfile("home.py")
				break

			else:
				print("Invaild password, Try again!")

else:
	print("Invaild command!")
