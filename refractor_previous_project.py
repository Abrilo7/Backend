#calculator mini project using reusable function
def sum_calculator(num1,num2):
    return num1 + num2
    

def sub_calculator(num1,num2):
    return num1 - num2
    

def div_calculator(num1,num2):
    if num2==0:
        return None
    return num1 / num2
    

def mul_calculator(num1,num2):
    return num1 * num2
    

def exp_calculator(num1,num2):
    return num1 ** num2

while True:
    print("""Press
          1️⃣ .Addition
          2️⃣ .Substraction
          3️⃣ .Division
          4️⃣ .Multiplication
          5️⃣ .Exponent
          6️⃣ .Exit""")
    try:
        choice = int(input(">> "))
    except ValueError:
        print("❌ Invalid input! ")
        continue
    
    if choice == 6:
        
        print("""Are sure you want to Exit❓
          1️⃣. Yes
          2️⃣. No(press any number you want 'except 1' )
              """)
        try:
            terminate = int(input(">> "))
        except ValueError:
            print("❌ Invalid input! ")
            continue
        if terminate == 1:
            print("Goodbye🙏")
            break
        else:
            print('✅ Exit cancelled')
            continue
    try:
        num1 = input("Enter the first number: \n>> ")
        num2 = input("Enter the second number: \n>> ")
    except ValueError:
        print("❌ Invalid input! ")
        continue 
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("❌ Invalid input")
        continue
    if choice == 1:
        summation = sum_calculator(num1,num2)
        print(f"✅ {num1} + {num2} = {summation}")
    elif choice == 2:
        substraction = sub_calculator(num1,num2)
        print(f"✅ {num1} - {num2} = {substraction}")
    elif choice == 3:
        division = div_calculator(num1,num2)
        if division is None:
            print("❌ Error: Cannot divide by zero!")
            continue

        print(f"✅ {num1} / {num2} = {division} ")
    elif choice == 4:   
        multiplication = mul_calculator(num1,num2)
        print(f"✅ {num1} x {num2} = {multiplication} ")
    elif choice == 5:
        exponent = exp_calculator(num1,num2)
        print(f"✅ {num1} ^ {num2} = {exponent}")


    