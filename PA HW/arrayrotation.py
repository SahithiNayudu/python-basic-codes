arr = [1, 2, 3, 4, 5]
k = int(input("Enter no of times to rotate: "))
k = k % len(arr)
rotate = arr[k:] + arr[:k]
print("Rotated list:", rotate)
