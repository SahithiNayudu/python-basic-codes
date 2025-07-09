lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
lst = list(set(lst))
if len(lst) < 2:
   print("Second largest does not exist.")
else:
   lst.sort()
   print("Second largest number is:", lst[-2])


