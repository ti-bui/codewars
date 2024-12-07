# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

def kidsWithCandies(candies, extraCandies):
    result = []
    max_num = max(candies)
    for i in range(len(candies)):
        greatest = candies[i] + extraCandies
        result.append(greatest >= max_num)
    return result
