# num = int(input("Number: "))

# if num > 5:
#     print("Greater by 5.")
# elif num < 5:
#     print("Less than 5.")
# else:
#     print("Equal to 5.")


#merge sort in python

def merge(arr, s, mid, e):

    s1 = mid - s + 1
    s2 = e - mid

    a1 = list(0 for _ in range(0, s1))
    a2 = list(0 for _ in range(0, s2))
    
    for i in range(0, s1):
        a1[i] = arr[s+i]
    
    for i in range(0, s2):
        a2[i] = arr[mid + 1 + i]
    
    i = 0
    j = 0
    k = s

    while i<s1 and j<s2:
        if(a1[i] < a2[j]):
            arr[k] = a1[i]
            k+=1
            i+=1
        else:
            arr[k] = a2[j]
            k+=1
            j+=1
    
    while i<s1:
        arr[k] = a1[i]
        k+=1
        i+=1
    
    while j<s2:
        arr[k] = a2[j]
        k+=1
        j+=1



def mergeSort(arr, s, e):
    if(s>=e): return


    mid = s + (e-s)//2

    mergeSort(arr, s, mid)
    mergeSort(arr, mid+1, e)

    merge(arr, s, mid, e)


arr = [3, 4,1, 3333, 9, 11, 1]
# print(arr)

mergeSort(arr, 0, len(arr)-1)
# print(arr)

# s = set([1, 2,2,4])
# print(s)

from functions import cube
for i in range(10):
    print(f"Square of {i} is {cube(i)}")