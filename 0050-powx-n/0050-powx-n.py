class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        if n < 0:
            return 1.0 / self.myPow(x, -(n + 1) + 1)

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half

        return x * self.myPow(x, n - 1)