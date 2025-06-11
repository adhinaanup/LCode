import collections

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        INF = 10 ** 10
        N = len(s)

        def calc(a, b):
            ca = cb = 0
            highest = -INF
            q = collections.deque()

            # best[i][j]
            # ca has i % 2 parity
            # cb has j % 2 parity
            # best[i][j] is the "best" known prefix given i = ca % 2, j = cb % 2
            best = [[INF] * 2 for _ in range(2)]
            q.append((0, 0, 0))
            prefix = 0

            for x in s:
                if x == a:
                    ca += 1
                    prefix += 1
                elif x == b:
                    cb += 1
                    prefix -= 1

                q.append((ca, cb, prefix))

                while len(q) > k:
                    if q[0][1] == cb:
                        break
                    qa, qb, p = q.popleft()
                    best[qa % 2][qb % 2] = min(best[qa % 2][qb % 2], p)

                # currently at ca, cb
                # to make ca odd, we want the opposite
                highest = max(highest, prefix - best[(1 - ca % 2)][cb % 2])
                # print(a, b, best, prefix, highest)

            return highest

        best = -INF
        cs = set(s)
        for a in cs:
            for b in cs:
                if a != b:
                    best = max(best, calc(a, b))
                    # print(a, b, calc(a, b))
        return best

'''You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

subs has a size of at least k.
Character a has an odd frequency in subs.
Character b has an even frequency in subs.
Return the maximum difference.

Note that subs can contain more than 2 distinct characters.

 

Example 1:

Input: s = "12233", k = 4

Output: -1

Explanation:

For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

Example 2:

Input: s = "1122211", k = 3

Output: 1

Explanation:

For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

Example 3:

Input: s = "110", k = 3

Output: -1'''
