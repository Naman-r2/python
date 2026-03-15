def partition(arr, s, e):
    pivot = arr[e]
    i = s - 1 

    for j in range(s, e):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[e] = arr[e], arr[i+1]
    return i + 1

def quick_sorth(arr, s, e):
    if s < e:
        pivotIndex = partition(arr, s, e)
        quick_sorth(arr, s, pivotIndex - 1)
        quick_sorth(arr, pivotIndex + 1, e)

def quick_sort(arr):
    quick_sorth(arr, 0, len(arr) - 1)
    return arr  

print(quick_sort([5,4,3,2,7]))