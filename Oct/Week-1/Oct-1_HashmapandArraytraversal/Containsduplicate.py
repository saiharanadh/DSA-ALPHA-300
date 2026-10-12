def ContainsDuplicate(arr):
    hashmap = {}

    for i in range(len(arr)):
        if arr[i] in hashmap:
            #check whether the current element is already in hashmap
            return True
        else:
            hashmap[arr[i]] = i

    return False#if no duplicate is found

print(ContainsDuplicate([1,2,3,1]))
"""brute force approach :
use two loops compare every pair of elements if found  return true else false
time complexity:O(n2)
Optimal is hashmap"""