'''
Find PI to the Nth Digit - 
Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
'''
f = open("assets/Pi/pi.txt", "r")
pie = f.read()
pie_max = int(input("Number Of PI Numbers [Max 1mil]: "))
if pie_max == 1:
    print("3")
elif pie_max == 2:
    print("3.1")
elif pie_max > 1000000:
    print("The Limit Is 1 Million!")
    quit()
else:
    print(pie[0:pie_max + 1])


    