# https://leetcode.com/problems/first-bad-version/submissions/1483884494/

def firstBadVersion(self, n: int) -> int:
    first, last = 1, n

    while first < last:
        mid = first + (last-first) // 2

        if isBadVersion(mid):
            last = mid
        else:
            first = mid+1
    return last
