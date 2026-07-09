


#data types
#integer data types
a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(type(a))
print(type(b))

# float datatypes
weight = 22.33
print(type(weight))

#operations
a = 12.33
b = 32.33

print(a + b)
print(a - b)


# strings 

name = "rahul"
age = '20'

print(name + age)
print(type(name))


# boolean
is_student = True
print(type(is_student))



# TYPECASTING : CONVERTING ONE DATA TYPE INTO ANOTHER



#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

#print(num1 + num2)

#IMPLICIT : PYTHON CONVERTS ITSELF SMALLER DATATYPES INTO LARGER COMPATIBLE WHEN NEEDED
a = 10      # int
b = 2.5     # float

result = a + b

print(result)
print(type(result))

#EXPLICIT
age = "20"

age = int(age)

print(age)
print(type(age))






#STRINGS METHOD

#upper

name = "Python"

name.upper()

print(name.upper())

#lower

name = "Rahul"
name.lower()
print(name.lower())

#rstrip
name = "Rahul!!!!!!!!!!!"
name.rstrip()
print(name.rstrip("name"))

#replace
text = "I like Java"

print(text.replace("Java", "Python"))

#split
text = "I love python"
print(text.split())