class Solution:
    def reverse(self, x):
        is_negative = x < 0
        x = abs(x)
        s = 0

        while x > 0:
            digit = x % 10
            s = s * 10 + digit
            x = x // 10

        if is_negative:
            s = -s
        if s < -2**31 or s > 2**31 - 1:
            return 0

        return s
