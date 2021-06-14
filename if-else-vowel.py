#Get one string from user
#extract middle letter of the string
#check whether middle letter is vowel or no

a = str(input("Enter the String:"))
b = len(a)//2
print (a[b])
if a[b] == "a" or a[b] == "A":
    print("Vowel")
elif a[b] == "e" or a[b] == "E":
    print("Vowel")
elif a[b] == "i"or a[b] == "I":
    print("Vowel")
elif a[b] == "o" or a[b] == "O":
    print("Vowel")
elif a[b] == "u"or a[b] == "U":
    print("Vowel")
else:
    print("Not Vowel")
    


