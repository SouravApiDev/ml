
i = 1
while i < 2:
    a = float(input("1st Number:- "))
    op = input("Oparator:- ")
    b = float(input("2nd Number:- "))
    if op == "+":
        print("result",a,op,b,"=",a + b)
    elif op == "-":
        print("result",a,op,b,"=", a - b)
    elif op == "*":
        print("result",a,op,b,"=", a * b)
    elif op == "/":
        print("result",a,op,b,"=", a / b)
    else:
        print("Oparator error__")
