# https://leetcode.com/problems/merge-strings-alternately/submissions/1490972820/?envType=study-plan-v2&envId=leetcode-75

def mergeAlternately(word1, word2):
    res = []
    i, j = 0, 0
    m = len(word1)
    n = len(word2)

    while i < m and j < n:
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])

    return "".join(res)


print(mergeAlternately("abc", "def123"))
