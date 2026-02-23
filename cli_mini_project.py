# CLI login system
correct_username ="Admin"
correct_password = "123"
attempts = 5
while attempts>0:
    
    entered_username=input("Enter your username: ")
    entered_password =input(" Enter your password: ")
    if not entered_password.isdigit():
       attempts-=1
       print(f"Invalid input. Numbers only.\nattempts left{attempts}")
       continue

    if correct_username == entered_username and entered_password == correct_password: 
       print("Access is granted ")
       break
    else:
       attempts-=1
       print(f"wrong password or username. please Try again! \nYour Remaining attempts are: {attempts}")
if attempts == 0:
   print("Your account is blocked")
  
