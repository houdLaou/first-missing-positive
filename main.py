
def first_missing_positive(nums):
    n = 1

    while n in nums:
        n += 1

    return n


print(first_missing_positive([0, -2, 1, 2]))  # the outbut will be 3

