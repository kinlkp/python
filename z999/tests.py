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

def removeElement(nums):
    """
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. 
    Then return the number of elements in nums which are not equal to val.
    """
    k = 0  # Initialize the counter for elements not equal to val
    val = 3
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
    # t = 3
    # i = 0
    # while True:
    #     print(nums, i)
    #     if i > len(nums) - 1:
    #         break
    #     if nums[i] == t:
    #         del nums[i]
    #         i = 0
    #     else:
    #         i += 1
    # return len(nums)
    

def majorityElement(nums):
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """
    # count = 0
    # candidate = None
    # for num in nums:
    #     if count == 0:
    #         candidate = num
    #     count += (1 if num == candidate else -1)
    #     print(candidate, count)
    # return candidate
    from collections import Counter
    c = Counter(nums)
    max = 0
    o = None
    for i in c.most_common():
        if i[1] > max:
            max = i[1]
            o = i[0]

    return o

                    
if __name__ == '__main__':
    nums = [3,2,3]
    o = majorityElement(nums)
    print(o)