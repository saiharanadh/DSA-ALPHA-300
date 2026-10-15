def Maxconsecutiveones(arr):
    curr=0
    max=0
    for num in arr:
        if num==1:
            curr=curr+1
            if curr>max:
                max=curr
        else:
            curr=0
    return max
print(Maxconsecutiveones([1,1,1,0,1,1,1,1,0]))