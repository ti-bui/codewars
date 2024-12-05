# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    if len(s) > len(t):
        return False

    counter = 0

    for i in range(len(t)):
        if s[counter] == t[i]:
            counter += 1

        if counter == len(s):
            return True
    return False
