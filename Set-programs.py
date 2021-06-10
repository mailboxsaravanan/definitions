#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

a = set()
b = set()
print (a)
print (b)
print (type(a))
print (type(b))
##########################################################
a = {7,8,9,1,2,3,4,5,0}
b = {4,5,6,0}
print (a)
print (b)
print (type(a))
print (type(b))

##########################################################
#check whether set2 is subset of set1 or no ## issubset()
a = {7,8,9,1,2,3,4,5,0}
b = {4,5,6,0}
c = {1,2,3,4}
d = b.issubset(a)
e = c.issubset(a)
print (d)
print (e)
##########################################################
#check whether both have common elements are no ? ## intersection
a = {1,2,3,4}
b = {5,6,7,1,2}
c = a.intersection(b)
print(a)
print(b)
print(c)
##########################################################
#remove 8 from set 1 and set 2 ==> find the inferences
a = {7,8,9,1,2,3,4,5,0}
b = {4,5,6,8,0}

a.remove(8)
print (a)
b.remove(8)
print(b)

##########################################################

#discard 8 from set 1 and set 2 ==> find the inferences
a = {7,8,9,1,2,3,4,5,0}
b = {4,5,6,8,0}

a.discard(0)
print (a)

b.discard(0)
print (b)
##This method is different from the remove() method, because the remove()
##method will raise an error if the specified item does not exist, and the
##discard() method will not.


##########################################################
#find collection of both sets ===> set1 and set2

a = {7,8,9,1,2,3,4,5,0}
b = {4,5,6,8,0}

c = a.union(b)
print (c)

##########################################################


