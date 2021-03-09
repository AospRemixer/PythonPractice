import random

max_number = int(input('Enter the max number [Minimum 15]: '))
min_number = 1 
num = random.randrange(1, max_number - 15)
hint1 = random.randrange(min_number, num)
hint2 = random.randrange(num, max_number)
hint3 = random.randrange(min_number, num)
hint4 = random.randrange(num, max_number)

if hint2 <= hint4:
    hint4 = random.randrange(num, max_number)
if hint2 <= hint4:
    hint4 = random.randrange(num, max_number)
if hint2 <= hint4:
    hint4 = random.randrange(num, max_number)
if hint2 <= hint4:
    hint4 = random.randrange(num, max_number)
if hint2 <= hint4:
    hint4 = random.randrange(num, max_number)

if hint1 >= hint3:
    hint3 = random.randrange(min_number, num)
if hint1 >= hint3:
    hint3 = random.randrange(min_number, num)
if hint1 >= hint3:
    hint3 = random.randrange(min_number, num)
if hint1 >= hint3:
    hint3 = random.randrange(min_number, num)
if hint1 >= hint3:
    hint3 = random.randrange(min_number, num)

if max_number in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
    print("Please Pick a number over 15!")
else:
    print(f"The Number is {hint1} or more!")

guess1 = int(input("What Is Your Guess: "))
if guess1 == num:
    print(f"Your Correct! The number was {num}") 
    quit()
else:
    print(f"The number is {hint2} or less!")
guess2 = int(input('What Is Your Guess: '))
if guess2 == num:
    print(f"Your Correct! The number was {num}") 
    quit()
else:   
    print(f"The number is {hint3} or more!")
guess3 = int(input('What is Your Guess: '))
if guess3 == num:
    print(f"Your Correct! The number was {num}")
    quit()
else:
    print("You have one more guess!")
    print(f"The number is {hint4} or less!")
guess4 = int(input('What is Your Last Guess: '))
if guess4 == num:
    print(f"Your Correct! The number was {num}") 
    quit()
else:
    print('💀 Game Over 💀')
    print(f'The number was {num}')