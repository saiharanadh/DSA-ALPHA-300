def Intersectionoftwoarrays(arr1, arr2):
    seen = {}
    result = []

    for num in arr1:
        seen[num] = True

    for num in arr2:
        if num in seen:
            already_added = False

            for x in result:
                if x == num:
                    already_added = True
                    break

            if not already_added:
                result.append(num)

    return result

print(Intersectionoftwoarrays([1,2,2,1,7], [2,2,3,3,4]))