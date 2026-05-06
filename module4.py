# Read N (positive integer)
N = int(input("Enter a positive integer N: "))

# Read N numbers
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Read X (integer) and find its index
X = int(input("Enter X to search for: "))

# Search for X in the list
index = -1
for i in range(N):
    if numbers[i] == X:
        index = i + 1  # 1-based indexing
        break

# Output the result
print(index)
