import random
a = random.randrange(1, 11)
b = random.randrange(1, 11)
print(f"Side A is {a}cm tall. Side B is {b}cm wide.")
def calc():
    return a * b
area = calc()
print(f"The Area Of The Rectriangle is {area}.")