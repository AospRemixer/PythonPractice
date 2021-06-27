'''
Find PI to the Nth Digit - 
Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
'''
import math
pie = str(math.pi)
pie_max = int(input("Number Of PI Numbers: "))
if pie_max == 1:
    print("3")
elif pie_max == 2:
    print("3.1")
else:
    print(pie[0:pie_max + 1])
print(len(pie))
    