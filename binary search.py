def binary_search(arr,s):
    low=0
    high=len(arr)
    loc=-1
    for i in arr:
        mid=int((low+high)/2)
        if s in arr:
            if arr[mid]>s:
                high=mid-1
            elif arr[mid]<s:
                low=mid+1
            else:
                 loc=mid

        else:
              print (s,"not in list")
              exit(0)
    #print("loc: ",loc)

    if(loc==-1):
       print("element not found.")
    else:
        print("element found in location:  ",loc)
arr=[2,4,6,8,10,12,14,16,18,20]
r=55
binary_search(arr,r)
