first_num = int(input('First Number: '))
second_num = int(input('Last Number: '))

for i in range(first_num, second_num + 1):
    if i % 2 == 0:
        print("Even")
    elif i % 2 != 0:
        print("Odd")
    else:
        print(i)
print(i)