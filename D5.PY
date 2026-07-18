
#recursion

#factorial of any given number 
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
     return n* factorial (n-1)
print(factorial(3))



#fibonacci series
def fibonacci(n):
   if ( n==0 or n==1):
      return n
   else:
      return fibonacci(n-1)+fibonacci(n-2)
   
print(fibonacci(34))




#sets

#like this we can create empty set
s=set()
print(type(s))


#set methods

s1 = {1,2,3,4,5,6,7,8,9}
s2 = {2,4,6,8,10,12,14,16}
print(s1.union(s2))
print(s1.update(s2))



s1 = {1,2,3,4,5,6,7,8,9}
s2 = {2,4,6,8,10,12,14,16}
print(s1.union(s2))
s1.update(s2)


s1 = {1,2,3,4,5,6,7,8,9}
s2 = {2,4,6,8,10,12,14,16}
s1.update(s2)
print(s1.intersection(s2))


s1 = {1,2,3,4,5,6,7,8,9}
s2 = {2,4,6,8,10,12,14,16}
s3 = {2,4,5,6,7,8,9}
s3 = s1.symmetric_difference(s2)
print(s3)


#dictionaries

info = {
   'name':"rahul",
   'age':int(19),
   'sex':"M"
}
print(info['name'])


#dictionaries method 
ep1 = {13:23,12:34,123:34}
ep2 = {14:24,15:24}
ep1.update(ep2)
print(ep1)
#ep1.clear()
#print(ep1)

ep1.pop(13)
print(ep1)

ep1.popitem()
print(ep1)