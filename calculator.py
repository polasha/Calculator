operation= ""
number1 = 0
number2 = 0
answer = 0

def plus_operator(num1, num2):
    num3 = float(num1) + float (num2)
    return num3
    print (num3)

def minus_operator ( num1, num2):
    num3 = float(num1)-float(num2)
    return num3
    print(num3)

def multiplication_operator ( num1, num2):
    num3 = float(num1)* float(num2)
    return num3
    print(num3)

def division_operator ( num1, num2):
    num3 = float(num1)/ float(num2)
    return num3
    print(num3)

def modul_operator ( num1, num2):
    num3 = float(num1) % float(num2)
    return num3
    print(num3)

def exponential_operator ( num1, num2):
    num3 = float(num1) ** float(num2)
    return num3
    print(num3)


def main():
    print ('Welcom to the input screen')
    number1= input('what is your first input data:')
    number2 = input('what is your second input data:')
    operation = input('what do you wnat to do:')

    if operation == "add":
           answer = plus_operator(number1, number2)
           print (answer)

    elif operation == "sub":
            answer = minus_operator(number1, number2)
            print(answer)

    elif operation == "mul":
              answer = multiplication_operator(number1, number2)
              print(answer)

    elif operation == "div":
              answer = division_operator(number1, number2)
              print(answer)

    elif operation == "mod":
               answer = modul_operator(number1, number2)
               print(answer)

    elif operation == "exp":
              answer = exponential_operator(number1, number2)
              print(answer)
    else:
              print ('Enter the function valid ')


main()




