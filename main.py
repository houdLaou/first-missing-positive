
def first_missing_positive(nums):
    n = 1

    while n in nums:
        n += 1

    return n


print(first_missing_positive([0, -2, 1, 2]))  # 3
print(first_missing_positive([3, 4, -1, 1]))  # 2
print(first_missing_positive([1, 2, 3]))      # 4
print(first_missing_positive([-5, 0, -1]))    # 1
