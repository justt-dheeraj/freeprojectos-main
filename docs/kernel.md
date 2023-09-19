## kernel.py

This is our FREEProjectOS Kernel.

The FREEProjectOS currently handles the bootloader, accounts, and soon
when I develop it of course memory mangement!

### Note for contributors: Carefully test the kernel for bugs.

Lets have a look at the code:

```py
if setup == '1':
	name = input(str("Please enter your User Name To Be Displayed: "))
	pas = input(str("Please enter your Password to login: "))

	lines = [name]
	with open('user/username.pass', 'w') as f:
		f.writelines(lines)

	lines2 = [pas]
	with open('user/password.pass', 'w') as f:
		f.writelines(lines2)

	print("") # Space.
	print("Would you like to enable Virtual Aassistant?")
	print("[Yes/No]")

	while True:
		virtual = input(str(">>>: "))

		if virtual == "Yes":
			with open('user/virtual.txt', 'w') as f:
				f.writelines("1")

			print("Okay!")
			print("Done!")
			break

		elif virtual == "No":
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


```

This part of the code takes user input. It provides
two options. Either to continue with the setup or
to continue to home with prompting the user for their password
to their account. The input is selected with a number that coreresponds to
a selection. For example when inputting "1" it tells the system to continue on with the setup.

If you want you can add a option by adding it to the "print" prompt then
add it to the list of if statements.

For example:
```py
print("""
[1] Continue with setup.
[2] I've already done the setup.
[3] Exit
""")

setup = input(">>>: ")

if setup == '1':
	# do stuff.

if setup == '2':
	# do stuff.

if setup == '3':
	# do stuff.
```