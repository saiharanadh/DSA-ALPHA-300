def SingleNumber(arr):
    hashmap = {}

    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] += 1#increase the frequency if the element exists
        else:
            hashmap[arr[i]] = 1#initialize the frequency as 1

    for i in range(len(arr)):
        if hashmap[arr[i]] == 1:
            return arr[i]#return the element that appears only once

    return -1#if no single element is found
print(SingleNumber([2,2,1]))