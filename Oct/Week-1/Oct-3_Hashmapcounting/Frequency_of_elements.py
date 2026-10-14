def Frequency_of_elements(arr):
    count={}

    for num in arr:
        if num in count:
            count[num]= count[num] +1
        else:
            count[num] = 1
    return count
print(Frequency_of_elements([1,1,2,5,6,8,8,8]))
"""brute force : use two nested loops"""