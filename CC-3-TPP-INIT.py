name = input("Enter your name: ")
print("Hello,", name)
print("Let's add some numbers!")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
total = a + b
difference = a - b
product = a * b
if b != 0:
    quotient = a / b
else:
    quotient = None
print("Sum:", total)
print("Difference:", difference)
print("Product:", product)
if quotient is not None:
    print("Quotient:", quotient)
else:
    print("Cannot divide by zero")
print("Done!")
