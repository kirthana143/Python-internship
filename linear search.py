def search(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return-1
arr=[2,3,4,10,40]
target=40
n=len(arr)
result=search(arr,n,target)
if(result==-1):
    print("element is not present in the array")
else:
    print("element is present at index",result)



