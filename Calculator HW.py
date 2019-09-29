print("This is your SIMPLE calculator!")
bContinue=True
while True == bContinue:
    x = ""
    while False == x.isdigit():
        x= input(" Type your first number: ")
    
    y = ""
    while False == y.isdigit():
        y= input(" Type your second number: ")

    print ("Your first number is " +str(int(x)))
    print("Your second number is " + str(int(y)))
        
    print("Here are your choices:")
    print("Addition +")
    print("Subtraction -")
    print("Multiplication *")
    print("Division /")

    bCheckOperation = True
    while True == bCheckOperation:
        choice= input("Enter either +, -, *, /: ")

        if choice == "+":
            print("x + y =")
            print(int(x) + int(y))
            bCheckOperation = False
        elif choice == "-":
            print("x - y =")
            print(int(x) - int(y))
            bCheckOperation = False
        elif choice == "*":
            print("x * y =")
            print(int(x) * int(y))
            bCheckOperation = False
        elif choice == "/":
            print("x / y =")
            print(int(x) / int(y))
            bCheckOperation = False
        else:
            print("Please enter a valid input")

    z =input( "Do you want do perfrom another operation? yes/no ")

    if z== "no":
        bContinue=False


