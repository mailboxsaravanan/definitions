#program8 

#two strings from user
#string 1: python  ==> first + middle + last 
#string 2: ptn

#valid otherwise invalid

a = str(input("String:"))
b = str(input("String:"))

print(a)
print(b)
if a[0]+a[len(a)//2-1]+a[-1] == b:
    print("Valid")
else:
    print("Invalid")

