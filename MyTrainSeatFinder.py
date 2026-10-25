seats = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
target = 130

guess = input("How many steps to find seat 130? ")
input("Start Binary Search. Press Enter ")
low = 0
high = len(seats) - 1
steps = 0

while low <= high:
    input("Check middle seat. Press Enter ")
    mid = (low + high) // 2
    steps += 1

    print("Checking seat:", seats[mid])
    if seats[mid] == target:
        print("Seat found!")
        break
    elif target < seats[mid]:
        high = mid - 1
    else:
        low = mid + 1
print("Steps taken:", steps)
print("Your guess:", guess)

input("Watch complexity grow. Press Enter ")
for n in [10, 100, 1000]:
    input("n = " + str(n) + ". Press Enter ")
    print("  O(1) =", 1, " O(n) =", n,
          " O(n^2) =", n * n)

input("Full complexity ladder. Press Enter ")
print("O(1) = 1")
print("O(log n) = 10")
print("O(n) = 1,000")
print("O(n^2) = 1,000,000")