###insertion of element at begining
"""
insert element 100 in the begining of array.

"""
arr=[1,2,3,4,5]
element = 100
#######using built in function
arr.insert(0,element)
print(arr)

#######using custom logic
arr=[1,2,3,4,5]

#adding one element at last
arr=arr+[0]

for i in range(len(arr)-2,-1,-1):
    arr[i+1]=arr[i]

arr[0]=element
print(arr)


###insertion of element at given postiton
"""
insert element 100 at position 1.

"""
element = 100
pos=5
arr=[1,2,3,4,5]

arr.append(0)
if pos==len(arr)-1:
    arr[-1]=element
else :
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
        if i==pos:
            break
arr[pos]=element
print(arr)