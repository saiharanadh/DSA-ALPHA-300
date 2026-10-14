def Majorityelement(arr):
    count = {}
    n = len(arr)
    
    for num in arr:
        if num in count:    
            count[num] = count[num]+1
        else :
            count[num]=1
        
        if count[num] > n// 2:
            return num

    return -1
"""
here we can use second method which is boyer morey voting algorithm
candidate=None
count=0
for num in arr:
    if count==0:
        candidate=num
    if candidate==num:
        count =+1
    else:
        count=-1

return candidate
"""

print(Majorityelement([2,2,1,1,3,3,2,2,2]))


