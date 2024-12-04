# https://leetcode.com/problems/length-of-last-word/submissions/1469792734/

def lengthOfLastWord(s: str) -> int:
    new_s = s.strip().split(' ')
    res = len(new_s[-1])
    return res
