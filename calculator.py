import math
while True:
    op = input()

    if op == "exit":
        break
    if op =="sin" or op == "log" or op == "fact" or op == "cot" or op == "tan" :
        a = int(input())
    else:
        a = int(input())
        b = int(input())

    if op == "+":
        result = a + b

    elif op == "-":
        result = a - b

    elif op == "*":
        result = a * b

    elif op == "/":
        result = a / b 

    elif op == "^":
       result = a ** b 

    elif op == "log":
      result = math.log(a)      

    elif op =="tan":
        result =math.tan(a)

    elif op =="sin":
        result =math.sin(a)

    elif op == "cot":
        result = 1/math.tan(a)

    elif op == "fact":
        result = math.factorial(a)

    else: 
        result = "motvaje nashodam🙄"

    print (result)