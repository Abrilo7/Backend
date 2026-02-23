# calculator mini project using reusable function
def sum_calculator(entered_value1,entered_value2):
    return entered_value1 + entered_value2
    

def sub_calculator(entered_value1,entered_value2):
    return entered_value1 - entered_value2
    

def div_calculator(entered_value1,entered_value2):
    if entered_value2==0:
        return None
    return entered_value1 / entered_value2
    
    

def mul_calculator(entered_value1,entered_value2):
    return entered_value1 * entered_value2
    

def exp_calculator(entered_value1,entered_value2):
    return entered_value1 ** entered_value2
while True:
    print("""Press
          1️⃣ .Addition
          2️⃣ .Substraction
          3️⃣ .Division
          4️⃣ .Multiplication
          5️⃣ .Exponent
          6️⃣ .Exit""")
    entered_value = input(">> ")
    if not entered_value.isdigit():
         print("❌ Invalid input. Numbers only")
         continue
    entered_value = int(entered_value)
    if entered_value == 6:
        
        print("""Are sure you want to Exit❓
          1️⃣. Yes
          2️⃣. No(press any number you want 'except 1' )
              """)
        terminate = input(">> ")
        if not terminate.isdigit():
            print("❌ Invalid input. Numbers only")
        terminate = int(terminate)
        if terminate == 1:
            print("Goodbye🙏")
            break
        else:
            print('✅ Exit cancelled')
            continue
    entered_value1 = input("Enter the first number: \n>> ")
    entered_value2 = input("Enter the second number: \n>> ")
    if not entered_value1.isdigit():
         print("❌ Invalid input. Numbers only")
         continue
    if not entered_value2.isdigit():
         print("❌ Invalid input. Numbers only")
         continue 
    entered_value1 = float(entered_value1)
    entered_value2 = float(entered_value2)
    if entered_value == 1:
        summation = sum_calculator(entered_value1,entered_value2)
        print(f"✅ {entered_value1} + {entered_value2} = {summation}")
    elif entered_value == 2:
        substraction = sub_calculator(entered_value1,entered_value2)
        print(f"✅ {entered_value1} - {entered_value2} = {substraction}")
    elif entered_value == 3:
        division = div_calculator(entered_value1,entered_value2)
        if division is None:
            print("❌ Error: Cannot divide by zero!")
            continue

        print(f"✅ {entered_value1} / {entered_value2} = {division} ")
    elif entered_value == 4:   
        multiplication = mul_calculator(entered_value1,entered_value2)
        print(f"✅ {entered_value1} x {entered_value2} = {multiplication} ")
    elif entered_value == 5:
        exponent = exp_calculator(entered_value1,entered_value2)
        print(f"✅ {entered_value1} ^ {entered_value2} = {exponent}")


    