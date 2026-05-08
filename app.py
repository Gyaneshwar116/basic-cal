from helpers import *
n1=int(input("n1:"))
n2=int(input("n2:"))

print("select the below num")
print("select num 1 for addition")
print("select num 2 for sub")
print("select num 3 for mul")
print("select num 4 for power/exp")
print("select num 5 for divison")
print("select num 6 for floor div")
operator=int(input())
if operator ==1:
    print(add(n1,n2))
elif operator ==2:
    print(sub(n1,n2))
elif operator ==3:
    print(mull(n1,n2))
elif operator ==4:
    print(division(n1,n2))
elif operator ==5:
    print(power(n1,n2))
elif operator ==6:
    print(floor(n1,n2))
else:
    print("invalid input please enter the correct input")