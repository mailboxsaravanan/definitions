#program4:
#Get one string from user
#check whether string is palindrome or no

a = str(input("String Please:"))
print(len(a))

if a[:len(a)//2] == a[len(a)//2+1:]:
    print("Polin")
else:
    print("Not poly")

### not correct
