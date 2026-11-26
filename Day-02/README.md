# Python Day 2 – Fundamentals

##  Topics Learned

- Print Statement
- Comments
- Variables
- Data Types
  - Integer (`int`)
  - Float (`float`)
  - String (`str`)
- Type Conversion
- User Input (`input()`)
- Output (`print()`)

---

## 1. Print Statement

The `print()` function is used to display information on the screen.

### Syntax

```python
print("Hello World")
```

### Example

```python
print("Hello, Welcome to Python!")
print("I am learning Python")
```

### Output

```text
Hello, Welcome to Python!
I am learning Python
```

---

## 2. Comments

Comments are used to explain the code. Comments are ignored during program execution.

### Single-Line Comment

A single-line comment starts with the `#` symbol.

```python
# This is a single-line comment
print("Hello Python")
```

### Inline Comment

An inline comment is written on the same line as a statement.

```python
print("Hello Python")  # Display a message
```

### Multi-Line Comments

Multi-line comments can be written using multiple `#` symbols or triple quotes.

```python
'''
This is a multi-line comment.
I am learning Python.
'''
print("Python")
```

---

## 3. Variables

A variable is a name used to store a value.

### Example

```python
name = "Manikanta"
age = 19
salary = 25000.50
```

Here:

- `name` stores a string value.
- `age` stores an integer value.
- `salary` stores a float value.

### Rules for Naming Variables

1. A variable name must start with a letter or underscore.
2. A variable name cannot start with a number.
3. Variable names can contain letters, numbers, and underscores.
4. Spaces are not allowed in variable names.
5. Python keywords cannot be used as variable names.

### Valid Variable Names

```python
name
student_age
product_price
employee_id
```

### Invalid Variable Names

```python
2name
student age
class
```

---

## 4. Data Types

Data types define the type of value stored in a variable.

### Integer (`int`)

An integer is a whole number without a decimal point.

```python
age = 19
number = 100

print(age)
print(type(age))
```

Output:

```text
19
<class 'int'>
```

### Float (`float`)

A float is a number that contains a decimal point.

```python
price = 99.50
salary = 25000.75

print(price)
print(type(price))
```

Output:

```text
99.5
<class 'float'>
```

### String (`str`)

A string is a sequence of characters enclosed in quotation marks.

```python
name = "Manikanta"
course = "B.Sc Computer Science"

print(name)
print(type(name))
```

Output:

```text
Manikanta
<class 'str'>
```

---

## 5. Type Conversion

Type conversion means converting a value from one data type to another.

### Integer Conversion – `int()`

The `int()` function converts a value into an integer.

```python
number = "25"
number = int(number)

print(number)
print(type(number))
```

Output:

```text
25
<class 'int'>
```

### Float Conversion – `float()`

The `float()` function converts a value into a float.

```python
number = 25
number = float(number)

print(number)
print(type(number))
```

Output:

```text
25.0
<class 'float'>
```

### String Conversion – `str()`

The `str()` function converts a value into a string.

```python
age = 19
age = str(age)

print(age)
print(type(age))
```

Output:

```text
19
<class 'str'>
```

---

## 6. User Input

The `input()` function is used to take input from the user.

**Important:** The `input()` function returns the entered value as a string by default.

### Example

```python
name = input("Enter your name: ")

print("Welcome", name)
```

Output:

```text
Enter your name: Manikanta
Welcome Manikanta
```

### Taking Integer Input

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

### Taking Float Input

```python
salary = float(input("Enter your salary: "))

print(salary)
print(type(salary))
```

---

## 7. Input and Type Conversion Example

```python
num_1 = int(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

result = num_1 + num_2

print(result)
```

### Explanation

- `input()` takes values from the user.
- `int()` converts the first input into an integer.
- `float()` converts the second input into a float.
- The converted values are stored in variables.
- The result is displayed using `print()`.

---

## 💻 Practice Problems

1. Write a program to print your name, age, college, course, and goal.
2. Write a program demonstrating single-line, inline, and multi-line comments.
3. Create variables to store Product ID, Product Name, Customer ID, and Customer Name.
4. Create variables to store Employee ID, Salary, and Department Name.
5. Display the values and data types of your variables using `type()`.
6. Take the user's name and age as input and display them.
7. Take two numbers from the user and convert them into appropriate data types.
8. Take three subject marks and calculate the total and average.
9. Take Product Price and Quantity and calculate the Total Bill.
10. Take a number as a string, convert it into an integer, and add 10.
11. Take two numbers as strings, convert them into integers, and perform addition.
12. Take Principal, Rate, and Time and calculate Simple Interest.
13. Convert total seconds into minutes and remaining seconds.
14. Convert Rupees into Paise.
15. Create five different variables and display their values and data types.

---

## 🎯 Day 2 Goal

My goal is to understand Python fundamentals, variables, data types, type conversion, and input/output through hands-on practice.

**Learning Python one day at a time! 🚀**
