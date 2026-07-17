
#function

def calculation(a,b):
    return a+b, a-b, a*b

x,y,z = calculation(10,5)

print(x)
print(y)
print(z)

def calc(a,b,c,d):
    return(a+b, a-b, a*b, a/b )


p,q,r,s= 1,2,3,4
print(p)
print(q)
print(r)
print(s)







#list
fruits = ["Apple", "Banana", "Orange", "Mango"]
print (fruits[0])
print (type(fruits))
print(fruits[0:4])
print(fruits[0:-4])


#list comprehension
numbers = [1,2,3,4]

square = [x*x for x in numbers]

print(square)



#tuples


t = ("rahul", "honey")
print(t)
print(type(t))
print(len(t))


t = (0,1,2,3,4,5,6,7,8,9,10)

print(t[1:4])
print(t[:3])
print(t[2:])
print(t[::-1])

print(t.count(1))



#f-string

name = "Aashika"
age = 20

print(f"My name is {name} and I am {age} years old.")


x = 8
y = 4

print(f"Addition = {x+y}")
print(f"Subtraction = {x-y}")
print(f"Multiplication = {x*y}")
print(f"Division = {x/y}")


#docstring

def greet():
    """
    This function prints a greeting.
    """
    print("Hello")
    print(type(greet))




def greet():
    """
    Prints Hello.
    """
    print("Hello")

print(greet.__doc__)


import this