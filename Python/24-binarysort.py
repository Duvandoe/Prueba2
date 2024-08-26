def binarysearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#Ejemplo de busqueda
arr = [2, 3, 4, 10, 40]
target = 4
print(binarysearch(arr,target))
