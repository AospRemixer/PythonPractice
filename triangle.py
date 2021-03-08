def method(x: float, y: float):
    return (x * y) / 2 

height = float(input("Height: "))
base = float(input("Base: "))

print("(", height, "+", base, ")", "÷", 2,"=", method(height, base))