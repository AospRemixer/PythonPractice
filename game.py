import random

max_number = int(input('Enter the max number [Minimum 15]: '))
num = random.randrange(1, max_number - 15)
random = random.randrange(1, 5)
random2 = random.randrange(1, 5)
random3 = random.randrange(1, 5)
hint1 = random.randrange(1, num + (random))
hint2 = random.randrange(num, max_number)
hint3 = random.randrange(1, num + (random3))
hint4 = random.randrange(1, num)

if max_number in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
    print("Please Pick a number over 15!")
else:
    print(f"The Number is {hint1} or less!")

guess1 = int(input('What Is Your Guess: '))
if guess1 == num:
    print(f"Your Correct! The number was {num}")
else:
    print(f"The number is {hint2} or more!")
guess2 = int(input('What Is Your Guess: '))
if guess2 == num:
    print(f"Your Correct! The number was {num}")
else:
    print(f"The number is {hint3} or less!")
guess3 = int(input('What is Your Guess: '))
if guess3 == num:
    print(f"Your Correct! The number was {num}")
else:
    print("You have one more guess!")
    print(f"The number is {hint4} or less!")
guess4 = int(input('What is Your Last Guess: '))
if guess4 == num:
    print(f"Your Correct! The number was {num}")
else:
    print('💀 Game Over 💀')
    print(f'The number was {num}')