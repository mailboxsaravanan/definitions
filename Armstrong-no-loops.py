

######################
#program11## Armstrong or not

K = int(input())

A1= K // 10
A = K % 10
print(A**3)
B1 = A1 // 10
B = A1 % 10
print(B**3)
C1 = B1 // 10
C = B1 % 10
print (C**3)

if K == A**3 + B**3 + C**3:
    print("arms")
else:
    print("no arms")


###################

#program10

#get one integer from user
#armstrong or no (without using loops)

#153 ===> 1^3 + 5^3 + 3^3
#370 ===> 3^3 + 7^3 + 0^3
#371 ====> 3^3 + 7^3 + 1^3

K = str(input("Enter the Number:"))

Output = int(K[0])**3 + int(K[1])**3 + int(K[2])**3
string = str(Output)
if K == string:
    print("Arms")
else:
    print("No arms")

### but my input must be 3 digit integer




