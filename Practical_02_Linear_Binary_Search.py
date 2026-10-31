def linear_search(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1


def binary_search(data, target):
    # Binary search requires the list to be sorted.
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


customer_ids = [102, 205, 150, 123, 301, 110, 175]
target = int(input("Enter customer account ID to search: "))

# Linear search on the original list
position = linear_search(customer_ids, target)
if position != -1:
    print("Linear Search: ID found at position", position)
else:
    print("Linear Search: ID not found")

# Binary search on a sorted copy
sorted_ids = sorted(customer_ids)
print("Sorted customer IDs:", sorted_ids)

position = binary_search(sorted_ids, target)
if position != -1:
    print("Binary Search: ID found at sorted position", position)
else:
    print("Binary Search: ID not found")
