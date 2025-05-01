# using test case , find even or odd
# i=1
# test = int(input("Enter a test case: "))
# while i<=test:
#     number = int(input("Enter a number: "))
#     print("Even" if number%2 == 0 else "Ödd")
#     i+=1

def __calculator__(num1,num2,operator):

    if operator == "+" :
        return num1+num2 
        
    elif operator == "-":
        return num1-num2
        
    else:
        return f"{operator} is invalid!"
        
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number: "))
operator = input("Enter + or -  : ")
         
print(f"{num1}{operator}{num2}={__calculator__(num1,num2,operator)}")