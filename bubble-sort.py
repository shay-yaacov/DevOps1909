
def bubble_sort1(arr):  #no recursion

   for j in range(len(arr)-1):
       for i in range(len(arr)-1-j):
           if arr[i] > arr[i+1] :
               arr[i], arr[i+1] = arr[i+1], arr[i]
   return arr



def bubblesort(l,n): #recursion
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    if n>1:
        bubblesort(l,n-1)
    return l


arr= [10,8,6,3,1,2,6]

for x in range (len(arr)):
    print (x)
    
arr2= [4,8,1,7,0]

print(bubble_sort1(arr))
print (bubblesort(arr2,len(arr2)))