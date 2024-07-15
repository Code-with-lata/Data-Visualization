#input numbers through the keyboard
num1 = int (input("Enter first number :"))
num2 = int (input("Enter second num :"))
num3 = int(input("Enter thied num :"))
num4 = int (input("Enter fourth num :"))
if(num1==num2 & num1==num3 & num1==num4):
    print("All are equal")
elif(num1>=num2 & num1>=num3 & num1>=num4):
    print(num1, " is greatest")
elif(num2>=num1 & num2>=num3 & num2>=num4):
    print(num2,"is greatest")
elif(num3>=num1 & num3>=num2 & num3>=num4): 
    print(num3,"is greatest")
else:
    print(num4,"is greatest")   
