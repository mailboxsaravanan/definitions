#program2
#Get one string from user
#Find the middle letter
#find ascii value for the middle letter
#check whether ascii value is odd or even

a = str(input("Enter the String:"))
print(ord(a[len(a)//2]))
if ord(a[len(a)//2]) % 2 == 0:
    print("The ASCII Value is Even")
else:
    print("The ASCII Value is ODD")
