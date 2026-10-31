def selection_sort(values):
    arr = values.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def bubble_sort(values):
    arr = values.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    salary = float(input("Enter salary: "))
    salaries.append(salary)

selection_result = selection_sort(salaries)
bubble_result = bubble_sort(salaries)

print("Selection Sort (ascending):", selection_result)
print("Bubble Sort (ascending):", bubble_result)

print("Top 5 highest salaries:")
for salary in bubble_result[-5:][::-1]:
    print(salary)
