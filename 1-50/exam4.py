# 求平方根

class Solution:
    def sqrt(self, x):
        l, r = 0, x
        while l + 1 < r:
            m = (r + l) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m
            else:
                l = m
        if l * l == x:
            return l
        if r * r == x:
            return r
        return l

if __name__ == "__main__":
    temp = Solution()
    x1 = 5
    x2 = 101
    print(("输入:" + str(x1)))
    print(("输出:" + str(temp.sqrt(x1))))
    print(("输入:" + str(x2)))
    print(("输出:" + str(temp.sqrt(x2))))