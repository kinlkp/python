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

def maxProfit(prices):
    """
    You are given an array prices where prices[i] is the price of a given 
    stock on the ith day. You want to maximize your profit by choosing a 
    single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.
    """
    # if not prices:
    #     return 0
    # m = nums.index(min(nums))
    # max = 0
    # for i in range(m, len(nums)):
    #     if nums[i] > nums[m]:
    #         d = nums[i] - nums[m]
    #         if d > max:
    #             max = d
    # return max
    # if not prices:
    #     return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
            # print(min_price)
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

def lengthOfLastWord(str1):
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    """
    a = str1.split(" ")
    i = -1
    while True:
        if len(a[i])  == 0:
            i -= 1
        else:
            return len(a[i])


def romanToInt(str1):
    a = list(str1)
    for k, v in enumerate(a):
        if v == 'I':
            a[k] = 1
        elif v == 'V':
            a[k] = 5
        elif v == 'X':
            a[k] = 10
        elif v == 'L':
            a[k] = 50
        elif v == 'C':
            a[k] = 100
        elif v == 'D':
            a[k] = 500
        else:
            a[k] = 1000
    print(a)

       
if __name__ == '__main__':
    str1 = "III"
    o = romanToInt(str1)
    print(o)