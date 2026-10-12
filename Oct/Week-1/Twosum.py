def Twosum(arr,target):
    hashmap = {}#create an empty dictionary to store the values
    for i in range(len(arr)):
        complement = target - arr[i]#this line calculates the required number needed to reach the target
        # here the comlpement is the required number

        if complement in hashmap:
            #check whether complement is in hashmap
            return [hashmap[complement],i]#it will give the indx of the complenemt and present number
        else:
            hashmap[arr[i]] = i

    return [-1,-1]

print(Twosum([1,2,3,9],10))
"""brute force approach:
take two for loops 1st loop i=0 and second loop j=j+1 the check whether the target is available or not
if available return i,j if not return -1,-1
Optimal approach is hash map"""