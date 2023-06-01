pos = 0
def sort(arr):
    for i in range(n-1,0,-1):       #   we are going in reverse order
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]=temp


def binsearch(arr,n,m):        # Defined binsearch method/function for executing binary search
    min = 0
    max = n-1
    while min<=max:             # the condition for binary search is that the list must be sorted
        mid = (min+max)//2
        if arr[mid] == m:
            globals()['pos']=mid
            return True
        else:
            if arr[mid]<m:
                min = mid +1
            else:
                max = mid +1
    return False

from array import *
arr = array('i',[])
try:
    n = int(input("Hey user please the length of Array "))
    for i in range(n):
        x = int(input("Enter the value in unsorted sorted form "))
        arr.append(x)
    m=int(input("Enter the value to be searched "))
    sort(arr)

    if binsearch(arr,n,m):
        print("Found at ",pos+1)
    else:
        print("Not found")

except ValueError as e:
    print("Wrong Input Given, Please enter an Integer value")



