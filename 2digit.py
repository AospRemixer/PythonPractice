txt = input("Digit 1: ")
txt2 = input("Digit 2: ")
estimate = input("Your Estimate: ")
right = "You are right!"
wrong = "Sorry, but your wrong!"

if int(txt) + int(txt2) == int(estimate):
    print(right)
else:
    print(wrong)
