name = input("Name: ")
password = input("Set Password: ")
confirm_pass = input("Confirm Password: ")

if password == confirm_pass:
    main = input("Password: ")

if main == password:
    print(f"Hello {name}!")

if main != password:
    print(f"Incorrect Password!")

