def min(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


def sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = min(arr)
        newArr.append(arr.pop(smallest))
    return newArr


my_list = [1, 9, 10, 3, 5, 23, 24, 33, 7, 12, ]
print(sort(my_list))
