# code by audiotore (github)

# This is our home page.
# Actually the user can just pretty much jump to home.py without
# being prompted for the password. Once again bad security oh well.

import time
import os
import random

# The resson why we are reading the
# username and password is because
# It's very important for our BioS.
virtual = open('user/virtual.txt')
login_pass = open('user/password.pass')
login_name = open('user/username.pass')
l_p = login_pass.read()
l_u = login_name.read()
l_v = virtual.read()

if l_v == "1":
	enable = "On"

else:
	enable = "Off"

print("""

███████╗██████╗░███████╗███████╗██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗░█████╗░░██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
█████╗░░██████╔╝█████╗░░█████╗░░██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░██║░░██║╚█████╗░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║███████╗███████╗██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═════╝░""")
print("WELCOME " + l_u)
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("Virtual assistant: " + enable) # Print if its togged on or off.
print("""
[1] To Open Google
[2] To Open Text Editor
[3] To Open File Explorer
[4] To Configure and Open BioS
[5] To learn About KernelOS
[6] To Reboot OS
[7] To Open FREEProjectPaint
[8] To Open Games
[9] To Take A Tour
[10] To Close OS Safley
""")
if enable == "On":
	num1 = random.randint(0, 9)
	if num1 == 1:
		print("Each number represents a different action.")
		print("Example: Type \"1\" if you want to open up google!")

	if num1 == 2:
		print("Did you know you can paint in FREEProjectOS?")

	if num1 == 3:
		print("Tip: You can open up windows apps using the File explorer")

	if num1 == 4:
		print("In case FREEProjectOS is broken you can always go into safemode! (FREEProjectOS PE)")

	if num1 == 5:
		print("If you want to disable Virtual assistant you can toggle me off in the BioS!")

	if num1 == 6:
		print("You should check out my github page!")

	if num1 == 7:
		print("Always look at your input before hitting Enter.")

	if num1 == 8:
		print("Bored? Play some games!")

	if num1 == 9:
		print("Security Tip: Always make sure your copy of FREEProjectOS is up to date!")

select = input("[?]: ")


if select == '1':
	os.startfile("home.py")
	os.startfile("brows.py")

if select == '2':
	os.startfile("home.py")
	os.startfile("edit.py")

if select == '3':
	os.startfile("home.py")
	os.startfile("file.py")

if select == '4':
	while True:
		# Sadly the user can bypass the Password check by going into Kernel.py
		# and saying that they "didn't" do the setup and erase the username and
		# password and set to their own password that they can remember
		# and get into the BioS. Encryping this would be pretty hard otherwise
		# Just put that data into an database Which is expensive. Even so
		# The user can just get into the Python code which is opensource.
		# and change up the code to check the database and instead check the variable
		# that contains what they want the password to be and get into the BioS like that.
		# Or even easier just get into the "user" folder and check the text files to see
		# their values. The only way to really prevent this is too put the user and password
		# files in a special directory most people can't think of searching and converting
		# our python code to an executable so that way the user can't check which directory
		# those files are at. which is the closest I can get too full encryption.
		# But I hate having to close source code of software so I rather not. Plus this is a 
		# small operating system with a popularity of 000000% Whoever is making viruses
		# for FREEProjectOS only must be pretty dumb and wasting their time.
		b_login = input(str("Please Enter The Password To " + l_u + " To Open BioS: "))

		if b_login == l_p:
			# At the moment the BioS doesn't really
			# have any useful features.
			# FREEProjectOS PE has pretty much
			# all these features.
			print("Logged in successfully!")
			print("Opening BioS")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_u)
			print("[2] PASSWORD: " + l_p)
			print("[3] Virtual assistant = " + enable)
			print("[4] Exit BioS")
			print("HOST NAME: " + host_name)
			print("LOCAL IPS: " + host_ip)
			edit_b = input("Enter [?] to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter new username: ")
				with open('user/username.pass', 'w') as f:
					f.writelines(edit_n)
				print("User Name Changed To " + edit_n)
				input("Press Enter to go Back: ")
				os.startfile("home.py")
				exit()

			if edit_b == '2':
				edit_n = input("Enter new password: ")
				with open('user/password.pass', 'w') as f:
					f.writelines(edit_n)

				print("Password Changed To " + edit_n)
				input("Press Enter to go Back: ")
				os.startfile("home.py")
				exit()

			if edit_b == '3':
				print("Do you want to turn or turn off virtual assistant?")
				print("[turnoff/turnon]")
				print("") # Space.

				edit_n = input(">>>: ")

				if edit_n == "turnoff":
					with open('user/virtual.txt', 'w') as f:
						f.writelines("0")

					print("") # Space.
					print("Okay!")
					print("Virtual assistant disabled!")
					input("Press Enter to go Back: ")
					os.startfile("home.py")
					exit()

				if edit_n == "turnon":
					with open('user/virtual.txt', 'w') as f:
						f.writelines("1")

					print("") # Space.
					print("Okay!")
					print("Virtual assistant enabled!")
					input("Press Enter to go Back: ")
					os.startfile("home.py")
					exit()

			if edit_b == '4':
				print("Exiting BioS")
				os.startfile("home.py") # Reset home.
				break

			else:
				print("Invaild option!")

		else:
			print("Wrong password to " + l_u)


if select == '5':
	print("FreeProjectOS is an free and open source")
	print("python operating system")
	print("") # Space.
	print("Press [Enter] to go back.")
	input()
	os.startfile("home.py")

if select == '6':
	os.system('cls')
	print("Rebooting...")
	time.sleep(3)
	os.startfile("Kernel.py")

if select == '7':
	os.startfile("paint.py")
	os.startfile("home.py")

if select == '8':
	os.startfile("games_select.py")

if select == '9':
	os.startfile("home.py")
	os.startfile("tour.py")

if select == '10':
	os.system('cls')
	print("Shutting down...")
	print("Thank you for using FreeProjectOS!")
	time.sleep(3)
	# Since theres no while loop it will exit on its own.
