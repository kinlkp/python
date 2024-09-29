def removeDuplicates(nums):
    """
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element 
    appears only once. The relative order of the elements should 
    be kept the same. Then return the number of unique elements in nums.
    """
    if not nums:
        return 0

    k = 1  # Start with the first element as unique
            # k = 0 no menaing (unique or duplicate)
    print(nums)
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            print(i, nums)
            k += 1
    return k


if __name__ == '__main__':
    nums = [1,2,3]
    o = removeDuplicates(nums)
    print(o)