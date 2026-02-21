  # Python Foundations Journey
  

This repository tracks my progress through a 90-day elite backend roadmap.

---

## Day 2 - Mini Project: Temperature Converter

### Description
Enter the temperature in Celsius.

### Output will display:
- Temperature in Kelvin
- Temperature in Fahrenheit
  
### It practices:
- Variables
- Input/output
- Arithmetic operations
- Float handling
- f-string formatting
  
---

## Day 3 – Mini Project: CLI Login System

### Description
This project simulates a simple login system in the terminal.  
It practices:

- Conditional statements (`if`, `elif`, `else`)
- Boolean logic (`and`, `or`, `not`)
- Loops (`while`)
- Input validation
- Security-aware design (generic error messages, attempt limits)

The system limits the number of password attempts and blocks access after repeated failures, introducing basic authentication logic.

### Features

1. **Username and Password Input**  
   - The system asks for a username and password in the terminal.
2. **Input Validation**  
   - Password input is checked to ensure it contains only numbers.
   - Invalid input counts as a failed attempt.
3. **Attempt Limit**  
   - Users have a maximum of 5 attempts to enter the correct credentials.
4. **Security Awareness**  
   - Generic error message is used (`"wrong password or username"`) to prevent attackers from knowing which part was incorrect.
5. **Account Blocking**  
   - When all attempts are used, the account is blocked.
     
---

## Day 4 - Mini Project: Multiplication Table Generator

### Description
This project generates a multiplication table for a number entered by the user.  
It practices:

- Loops (`for` loop)  
- Range handling (`range()` function)  
- Input validation  
- Basic arithmetic  
- Conditional logic (to ensure positive range and numeric input)  
- Formatted output using f-strings  

### Usage

1. Run the program in a terminal:
2. Enter the number you want to multiply.
3. Enter the range up to which you want the multiplication table.
4. The program validates inputs to ensure they are numeric and positive.
5. The multiplication table will display in a readable format.
   
---


## Day 5 - Mini Project: CLI Shopping List Manager

### Description
This project is a simple Command Line Interface (CLI) application that allows users to manage a shopping list.

The program runs in a loop and lets users:
- Add items
- Remove items
- View the current list 
- Exit the program

This project focuses on practicing:
- Lists
- Loops (`while`)
- Conditional statements
- Input validation
- List methods (`append`, `remove`)
- Basic user experience handling


### Features

#### 1️⃣ Add Item
Users can add new items to the shopping list.
- Input is cleaned using `.strip()` to remove extra spaces.
- Input is converted to lowercase using `.lower()` for consistency.

#### 2️⃣ Remove Item
Users can remove an item by name.
- The program checks if the item exists before removing it.
- Prevents crashes when item is not found.

#### 3️⃣ View List
Displays all current items in the shopping list.

#### 4️⃣ Input Validation
- Menu only accepts numbers.
- Prevents invalid menu selections.


