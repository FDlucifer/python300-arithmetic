# 判断平方数
class Solution:
    def isPerfectSquare(self, num):
        l = 0
        r = num
        while (r - l > 1):
            mid = (l + r) / 2
            if (mid * mid <= num):
                l = mid
            else:
                r = mid
        ans = l
        if (l * l < num):
            ans = r
        return ans * ans == num
if __name__ == "__main__":
    num = 20
    print("初始值: ", num)
    solution = Solution()
    print("结果: ", solution.isPerfectSquare(num))