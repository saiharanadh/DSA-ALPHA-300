def First_nonrepeatingelement(arr):
    count={}

    for num in arr:#this loop will count the frequencies of elements
        if num in count:
            count[num]= count[num] +1
        else:
            count[num] = 1

    for num in arr:#this will find the first no =n repeating element which appear fist
        if count[num] == 1:
            return num

        
    return -1
print(First_nonrepeatingelement([1,1,2,5,8,8]))
"""the time complexity is still O(n) because we have used two loops sperately o(n)+o(n)=o(n) so the time compleity is o(n)"""
"""Brute force approach :we can use two nested loops and if i==j increase count and if arr[i]==1 then it will return arr[i] thefirst non repeating element"""