a = "cybersecurity"
b = "datascience"


w = a[0:int(len(a)//2)-1]
z = a[int(len(a)//2):]
y = a[int(len(a)//2-1)].upper()
z=w+y+z


l1 = b[0:int(len(a)//2)-1]
l2 = b[int(len(a)//2):]
l3 = b[int(len(a)//2-1)].upper()
l4 = l1+l3+l2

print(z+l4)




