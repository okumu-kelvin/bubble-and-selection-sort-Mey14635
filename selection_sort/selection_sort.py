def selection_sort(arr):
    # TODO: Implement selection sort
for i in range(n):
    minpos=i
//the first loop go through each index i in the list by not the last one
    for j in range(len(arr)-1):
// minpos will track the index of the smallest value found in the remaining list
        if arr[j]<arr[minpos]:
            minpos=j
     temp=arr[i]
     arr[i]=arr[minpos]
     arr[minpos]=temp
 arr=[5, 4, 3, 2, 1, 0]
 selection_sort(arr)
 print(arr)

 return arr
    pass
