class Calculator:

    def addition(self):
        print("answer=", a + b)

    def subtraction(self):
        print("answer=", a - b)

    def multiplication(self):
        print("answer=", a * b)

    def division(self):
        print("answer=", a / b)


a = float(input("Enter first number:"))
b = float(input("Enter first number:"))

obj = Calculator()

choice = 1
while choice != 0:
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. STOP")
    choice = int(input("Enter your choice:"))
    if choice==5:
        break
    elif choice == 1:
        obj.addition()
    elif choice == 2:
        obj.subtraction()
    elif choice == 3:
        obj.multiplication()
    elif choice == 4:
        obj.division()
    else:
        print("Invalid choice")
