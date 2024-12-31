def longestCommonPrefix(strs):
    res = ''
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return res
        else:
            res += first[i]

    return res


print(longestCommonPrefix(["flower", "flow", "flight"]))
