
""""""""""""""""""""""""""""""""""
deletion of element in array
"""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
deletion of element at begining of array
"""""""""""""""""""""""""""""""""""""""""""""""""""

arr=[1,2,3,4,5]

#using inbuilt function
del arr[0]
print(arr)

#using custom function
arr=[1,2,3,4,5]

arr_new=arr[1:]
print(arr)

arr.append(6)
print(arr_new)

"""""""""""""""""""""""""""""""""""""""""""""""""""
deletion of element  of array at given position
"""""""""""""""""""""""""""""""""""""""""""""""""""
arr=[1,2,3,4,5]

pos=5
n=len(arr)

for i in range(pos,n):
    arr[i-1]=arr[i]

n=n-1
for i in range(0,n):
    print(arr[i],end=" ")


"""""""""""""""""""""""""""""""""""""""""""""""""""
deletion of first occurance of  element in array
"""""""""""""""""""""""""""""""""""""""""""""""""""
arr=[20,20,20,4,20]
element=20
n=len(arr)

found=False
for i in range(0,n):
    if arr[i]==element:
        found=True
    if found and i!=n-1 :
        arr[i]=arr[i+1]

if found:
    n=n-1

for i in range(0,n):
    print(arr[i],end=" ")


"""""""""""""""""""""""""""""""""""""""""""""""""""""
deletion of all occurance of  element in array
"""""""""""""""""""""""""""""""""""""""""""""""""""""
arr=[1,20,20,4,20]
element=20
n=len(arr)

k=0

for i in range(len(arr)):

    if arr[i]!=element:
        arr[k]=arr[i]
        k=k+1

print("--")
print(arr[0:k])


"""""""""""""""""""""""""""""""""""""""""""""""""""""
deletion of end  element in array
"""""""""""""""""""""""""""""""""""""""""""""""""""""
arr=[1,2,3,4]

n=len(arr)

print(arr[0:n-1])










