#50 + PASS otherwise FAIL
#90 to 100 ===> A  ==> Even + Odd -
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL

mark = int(input("Enter the mark:"))

if mark < 50:
    print("Fail")
elif mark > 50:
    print("Pass")

##could not bring range command here
