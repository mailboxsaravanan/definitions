#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times

a = (1,4,5,6,7,8)
b = (5,6,7,8,9)

print(a)
print(b)
# could not find common elements between two tuples


c =a+b

print(list(dict.fromkeys(c)))
print(c.index(9))
print (3*c[0:])

