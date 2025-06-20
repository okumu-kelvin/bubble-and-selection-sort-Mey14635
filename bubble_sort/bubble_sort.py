def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
#the first loop is to check how many time will go through the array
    for i in range(len(unsorted_list)-1,0,-1):
#the second loop is to do the comparison then swap them
        for j in range(i):
                #To do the swap we add a temporary variable to store the variable
            if unsorted_list[j]>unsorted_list[j+1]:
                temp=unsorted_list[j]
                unsorted_list[j]=unsorted_list[j+1]
                unsorted_list[j+1]=temp
    return unsorted_list

nums=[5, 4, 3, 2, 1, 0]
bubble_sort(nums)
print(nums)
