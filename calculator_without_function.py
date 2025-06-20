num1 = float(input("enter first number : "))
operator = input("enter operator(+,-,*,/ ): ")
num2 = float(input("enter second number : "))
print (num1, operator , num2 )
if operator == "+":
    print ("result: ", num1+num2)
elif operator == "-":
    print ("result: ", num1-num2)
elif operator =="*":
    print ("result : ", num1*num2)
elif operator == "/":
    if num2 != 0 :
         print("result:", num1/num2)
    else:
        print("error: cannot divide by 0 ")
else:
    print("invalid operator")

    