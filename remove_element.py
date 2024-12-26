# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


print(removeElement([3, 2, 2, 3], 3))
