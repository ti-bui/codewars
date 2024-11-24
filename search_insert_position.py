# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array

def searchInsert(nums, target):
    nums.append(target)
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            return i

# time: O(nlogn)
# space: O(1)
