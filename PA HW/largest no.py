a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a >= b and a >= c:
 print("Largest is first number:", a)
elif b >= a and b >= c:
 print("Largest is second number:", b)
else:
 print("Largest is third number:", c)
