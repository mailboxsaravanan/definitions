# find emi
# example of 

p = int(input("enter principal amount : "))
n = int(input("enter the year :"))
r = float(input("rate of int: "))

emi = int(p*n*r / 100)

print ("principal {} ; number of years {} ; rate of interest {}".format(p,n,r)) 
print ("EMI per month:", emi)
