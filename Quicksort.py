

def partition (arr,low,high):
    p = low
    for i in range(low+1, high):
        if arr[i] < arr[low]:
            p = p+1
            arr[p], arr[i] = arr[i], arr[p]
    arr [low], arr[p] = arr[p], arr[low]
    return p

def quick_sort(arr, low, high):
  
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


arr=[5,1,8,4,12,20,1]
quick_sort(arr,0,len(arr))
print (arr)
