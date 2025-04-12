def my_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


data = [1, 2, 10, 9, 3, 7, 0, 99, 27, 85]
print(my_max(data))
assert max(data) == my_max(data)


def neverland(q):
    first = q.pop(2)
    q.sort()
    q.insert(0, first)
    return q


q = [30, 10, 20, 50, 40, 60]
print(neverland(q))   
