"""def sum(arr):
    #base case
    if len(arr) == 0:
        return 0
    else:
        head= arr[0]
        tail = arr[1:]
        return head + sum(tail)

res = sum([2,4,6,8,10])
print(res)"""

"""
def quicksort(arr):
    len_arr = len(arr)

    if len_arr < 1:
        return arr
    else:
        pivot = arr.pop()
        greaterlist = []
        smallerlist = []

        for i in range(0,len_arr-1):
            if arr[i] < pivot:
                smallerlist.append(arr[i])
            else:
                greaterlist.append(arr[i])

        return quicksort(smallerlist)+[pivot]+quicksort(greaterlist)

res = quicksort([45,67,3,6,234,2,6,23,2])
print(res)
"""


"""
def merge(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2

    return _merge(merge(array[:mid]), merge(array[mid:]))


def _merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    merged = []
    r = l = 0

    while len(merged) < len(left) + len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

        if r == len(right):
            merged += left[l:]
            break

        if l == len(left):
            merged += right[r:]
            break
    return merged

res= merge([3,45,6,786,3,4,34,1])
print(res)
"""