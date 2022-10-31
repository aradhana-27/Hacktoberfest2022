def selection_sort(arr):
    #put the correct element in ith position
    for i in range(len(arr)-1):
        minIndex=i
        #calculating minimum element for this iteration
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]        


arr=[5,6,1,2,7,9,0,10,11,4]
selection_sort(arr)
print("the sorted array ",arr)