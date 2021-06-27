TheE = "e"
limit = int(input("How Many E's Do You Want To Generate [Limit 100]: "))
if limit > 100:
    print("The Limit Is 100!")
    quit()

print(TheE * limit)