  # Python Foundations Journey
  
---

This repository tracks my progress through a 90-day elite backend challenge.

---

## Day 2 - Mini Project: Temperature Converter

---

### Description
Enter the temperature in Celsius.

### Output will display:
- Temperature in Kelvin
- Temperature in Fahrenheit
  

---

## Day 3 – Mini Project: Login System

---

### Description
This project simulates a simple login system in the terminal.  
The system limits the number of password attempts and blocks access after repeated failures, introducing basic authentication logic.

---

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

---

### Description
This project generates a multiplication table for a number entered by the user.   

---
### Usage

1. Run the program in a terminal:
2. Enter the number you want to multiply.
3. Enter the range up to which you want the multiplication table.
4. The program validates inputs to ensure they are numeric and positive.
5. The multiplication table will display in a readable format.
   
---


## Day 5 - Mini Project: Shopping List Manager

---

### Description
This project is a simple Command Line Interface (CLI) application that allows users to manage a shopping list.

The program runs in a loop and lets:
- Add items
- Remove items
- View the current list 
- Exit the program

---

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

---

## Day 6 - Mini Project: User Management System

---

### 📌 Description

This project is a Command Line Interface (CLI) based User Management System built using Python dictionaries.

The program allows to:

- Register new users
- Login with credentials
- View all registered users
- Delete existing users
- Exit the system

This project focuses on mastering dictionary-based data modeling and persistent state management.

---

## 🚀 Features

### 1️⃣ Register User
- Username is normalized using `.strip()` and `.lower()`
- Prevents duplicate usernames
- Stores data in dictionary (`users[username] = password`)

### 2️⃣ Login System
- Verifies if username exists
- Validates password
- Handles incorrect password and unknown user cases safely

### 3️⃣ View All Users
- Displays all registered usernames
- Handles empty user database

### 4️⃣ Delete User
- Confirms before deletion
- Removes user safely using `pop()`
- Prevents errors if user does not exist

### 5️⃣ Exit Option
- Cleanly exits the program

---

### 📅 Progress Note

Day 6 focuses on structured data modeling using dictionaries.
This marks the transition from simple scripting to backend-style logic.

---

## Day 7 – Mini Project: Calculator (Functions-Based)

---

### 📌 Description

The calculator performs multiple mathematical operations while applying proper function structure, parameter passing, and return values.

This project focuses on mastering function design, scope separation, and clean control flow.

---

## 🚀 Features

### 1️⃣ Addition

* Uses a dedicated function
* Accepts two numeric parameters
* Returns computed result

### 2️⃣ Subtraction

* Structured as an independent function
* Clean parameter passing
* Returns difference

### 3️⃣ Division

* Handles division by zero safely
* Returns `None` when invalid
* Error handled in control flow

### 4️⃣ Multiplication

* Isolated mathematical logic
* Returns product of inputs

### 5️⃣ Exponentiation

* Computes power operation
* Clean and reusable implementation

### 6️⃣ Exit Option

* Exit confirmation system
* Prevents accidental termination
* Maintains clean loop control

---

## 🧠 Technical Focus

* Proper use of `def`
* Parameterized functions
* Return values instead of internal printing
* Separation of computation logic from UI logic
* Defensive input validation
* Structured program flow using a loop controller

---

## 📅 Progress Note

Day 7 focuses on mastering function architecture and clean program structure.

This marks the shift from procedural scripting to modular programming design — a foundational skill for backend development.
