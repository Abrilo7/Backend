input_range1 = input("Enter the range you want: ")
x1 = input("Enter the value you want to multiply: ")

if not input_range1.isdigit() or not x1.isdigit():
    print("Input is invalid. Enter numbers only.")
else:
    input_range = int(input_range1)
    x = int(x1)

    if input_range <= 0:
        print("Range has to be positive.")
    else:
        for i in range(1, input_range + 1):
            print(f"{x} x {i} = {x * i}")
    

    
