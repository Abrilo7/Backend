from book_management import *
while True:
    print("""press
Library Menu
    1. Show Books
    2. Borrow Book
    3. Return Book
    4. Display Information
    5. Exit
""")
    try:
        option = int(input("Enter Option: \n>> "))
    except ValueError:
        print("Enter Valid Option: \n>> ")
        continue
    if option == 5:
        print("Goodbye! ")
        break
    if option == 1:
        print("-"*40)
        for index, book in enumerate(books):
            print(f"{index + 1}. {book.title}")
        print("-" * 40)
        continue
    try:
        choice = int(input("Enter the number for the book you want: \n>>"))
    except ValueError:
        print("Invalid input!")
        continue
    if choice < 1 or choice > len(books):
        print("Invalid book number.")
        continue
    selected_book = books[choice-1]
    if option == 2:
        selected_book.borrow_book()
    elif option == 3:
        selected_book.return_book()
    elif option == 4:
        selected_book.display_info()
    else:
        print("Option is not Available!")
        continue