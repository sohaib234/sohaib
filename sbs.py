
try:
    full_name = ""

    full_name = input("enter your full name: ")

    gmail = "gamersohaib507@gmail.com" #contact on email
    gess = ""
    gesse = 20000
    op =0
    oute = False

    while gess != gmail and not(oute):
        if gesse > op:
            gess = input ("enter your gmail: ")
            op += 1
        else:
            oute = True

    if oute:
        print("invalid")
    else:
        print("gmail valid")
    
    code = "sbs"
    guess = ""
    guess_limit = 2
    guess_op = 0
    out = False

    while guess != code and not(out):
        if guess_limit > guess_op:
             guess = input("enter your password: ")
             guess_op += 1
        else:
            out = True

    if out:
        print("your password is false!")
    else:
        print("calculator")
        num1 = float(input("enter a num: "))
        op= input("enter a op: ")
        num2 = float(input("enter another num: "))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1- num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "*":
            print(num1 * num2)
        else:
            print("just: +,-,/,* ")
        print("Iwa choookran")
except:
    print("invalid!")


