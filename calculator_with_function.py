def add( a , b ):
    return a+b
def subtract(a , b):
    return a - b 
def multiply(a, b ):
    return a*b
def divide (a ,b ):
    if b !=0 :
        return a/b
    else :
        return" error : cannot divide by 0 "
while True :
    print("\nsimple calculator")
    try:
        num1 = float(input('enter first number :'))
        operator =input("enter operator(+,-,*,/ ):")
        num2 = float(input("enter second number :"))

        if operator == "+":
          result = add(num1,num2 )
        elif operator == "-" :
            result = subtract (num1 , num2)
        elif operator == "*":
            result = multiply(num1 , num2)
        elif operator =="/":
            result = divide (num1 , num2)
        else :
           result =" invalid operator "

        print("result :", result)

    except ValueError :
        print("invalid input ! please enter numbers only .")
    again = input("do you went to calculatr again ? (yes/no ): ").strip().lower()
    if again != "yes":
        print("thank you for using the calculator ! ")
        break
    