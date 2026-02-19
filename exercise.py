#Check weather the number is negative or positive
"""number = int(input("Enter number: "))
if number > 0:
    print(" The number is Positive ")
elif number < 0:
    print(" The number is Negative ")    
else:
    print("The number is Zero")
if number%2 == 0:
    print("It's even number")
else:
    print("It's odd number")   
if 0<number<13:
    print("child")
elif 13 <number< 19:
    print("Teenage")   
elif 20<number<59:
    print("Adult")   
elif number>60:
    print("Senior") 
elif number<0:
    print("invalid")
else:
    print("Zero") """
correct_password = 1234   
attempts=5

while attempts>0:
    entered_password = int(input("Enter password: "))
    if entered_password == correct_password:
        print("access is granted")
        break 
    else:
        attempts -= 1
        print(f"wrong password: attempts left {attempts}")
if attempts<=0:
    print("your account is bloced")