shopping_list = ["Bread","Milk","Vegitables","Fruits"] 

while True:
 print("""      press:
          1. To add an item
          2. To remove an item
          3. To veiw a list
          4. Exit
          """)
 item = input(">> ")
 if item.isdigit():
    item = int(item)
    if item == 1:
        mark = input("Enter the item you want to add: ").strip().lower()
        shopping_list.append(mark)
        print("Your item is added sucessfully! ")
    elif item == 2:
        arg = input("Enter the value you want to remove: ").strip().lower()
        if arg in shopping_list:
            shopping_list.remove(arg)
            print("Your item is successfully removed! ")
        else:
            print("Not Found! ")
    elif item == 3:
        print('\nCurrent lists')
        for i in shopping_list:
            print(i)
    elif item == 4:
        break
    else:
        print("I don't understand that... ")
 else:
     print("Invalid input!. Numbers only: ") 
     


