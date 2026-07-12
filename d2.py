
# This is a single-line comment
print("Hello, World!")  # print() displays output

"""
This is a multi-line comment.
Often used to describe what a file or function does.
"""

name = input("What is your name? ")  # input() always returns a string
print("Hello,", name)
print(f"Hello, {name}!")  # f-string preview (covered fully on Day 4)



age = 25            # int
price = 19.99        # float
name = "Alice"        # str
is_student = True     # bool

print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_student)) # <class 'bool'>

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# Reassigning changes the type freely
value = 10
value = "now I'm a string"
print(value)



# Type casting
num_str = "42"
num = int(num_str)       # string -> int
pi_str = "3.14"
pi = float(pi_str)        # string -> float
age = 25
age_str = str(age)        # int -> string
print(bool(0), bool(1), bool(""), bool("hi"))  # falsy vs truthy values

# Arithmetic operators
a, b = 17, 5
print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4   (true division)
print(a // b)  # 3     (floor division)
print(a % b)   # 2     (remainder)
print(a ** b)  # 1419857 (power)

# Comparison & logical operators
print(a > b and b > 0)   # True
print(a == 17 or b == 100)  # True
print(not (a > b))       # False

# Shortcut assignment
counter = 0
counter += 1   # same as counter = counter + 1
print(counter)



s = "Hello, Python!"

# Indexing
print(s[0])     # H
print(s[-1])    # !

# Slicing
print(s[0:5])   # Hello
print(s[7:])    # Python!
print(s[::-1])  # !nohtyP ,olleH  (reversed string)
print(s[::2])   # every 2nd character

# Methods
print(s.upper())          # HELLO, PYTHON!
print(s.lower())          # hello, python!
print("  padded  ".strip())  # "padded"
print(s.split(", "))      # ['Hello', 'Python!']
print("-".join(["a", "b", "c"]))  # a-b-c
print(s.replace("Python", "World"))  # Hello, World!
print(s.find("Python"))   # 7 (index where found)

# f-strings
name = "Alice"
score = 95.567
print(f"{name} scored {score:.1f} points")   # Alice scored 95.6 points
print(f"Doubled: {score * 2}")               # expressions allowed inside {}


age = 20

if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
else:
    category = "adult"
print(category)

# Nested conditionals
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Not positive")

# Ternary expression
x = 10
label = "even" if x % 2 == 0 else "odd"
print(label)  # even


# for loop with range()
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):  # 2,4,6,8
    print(i)

# for loop over a string
for ch in "abc":
    print(ch)

# while loop
count = 0
while count < 5:
    print("count is", count)
    count += 1

# break and continue
for i in range(10):
    if i == 7:
        break          # stop the loop entirely
    if i % 2 == 0:
        continue        # skip even numbers
    print(i)  # prints 1, 3, 5