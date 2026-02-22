user = {}
while True:
    print("""
1️⃣  Register User
2️⃣  Login System
3️⃣  View All Users
4️⃣  Delete User
5️⃣  Exit Option
""")
    name = input("Enter your option: \n>> ")
    if not name.isdigit():
        print("Invalid input ❗")
        continue
    name = int(name)
    if name == 1:
        mark = input("Enter your username: ").lower().strip()
        passwords = input("Enter your password: ")
        if mark in user:
           print("Username already exists!")
           continue
        user[mark] = passwords
        print("✅ You're successfully Registered! \n For login enter 2:")
    elif name == 2:
       username = input("Enter your username: ").lower().strip()
       user_password = input("Enter your password: ") 
       if username in user:
           if user[username] == user_password:
               print("✅ Login Successful")
           else:
               print("❌ Incorrect password!")
       else:
           print("❌ Username not found!")
    elif name == 3:
        if not user:
          print("No users registered yet.")
          continue
        for username in user:
            print(username)
    elif name == 4:
        delete_username = input("Enter Username to delete: ")
        #if max == user.get(f"{mark}"):
        if delete_username in user:
            my_user = input("""Are sure you want to delete this User❓
                 1. Yes 
                 2. No (press '2' or any other key to cancel)
                 >>""")
            if not my_user.isdigit():
                print("Invalid Input❗")
                continue
            my_user = int(my_user)
            if my_user == 1:
                user.pop(delete_username)
                print("✅ User is deleted successfully ")
            elif my_user == 2:
                continue
        else:
            print("Username is not Found❗ ")
    elif name == 5:
        break       
    