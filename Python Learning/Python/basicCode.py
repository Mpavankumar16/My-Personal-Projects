import math

age =23
x,y,z = 1,2,3
x=y=z=5

print("You are "+str(age)+" years old")
print("You are", age,"years old")
print(f"You are {age} years old")

#Integer age = 23
#Float   gpa = 9.8
#String  string = "name"
#Boolean student = True
type(21.3)
age  = float(21)
print(age)
#Type casting value 0 to bool will give false and any other number will give true
#Type casting value String will give true and empty string will give false

#Only need 2 pointers after decimal
val  = 2 * math.pi * 5
print(f"The cirucmference of circle is {round(val,2)}")

#Format specifiers
price = 12.2865
print(f"{price:.2f}")
print(f"{price:10}")#10 spaces ahead
print(f"{price:010}")#0 Padded instead of spaces
# < left justify and > right justify ^for center

#Excepiton handling
try:
    val = 10/0
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except Exception:
    print("You can't do that")
else:
    print("If not exception occured then we run")
finally:
    print("Will always run")


#Walrus operator :=
while inp :=input() !="q":
    print("Enter q or I will keep on printing")

