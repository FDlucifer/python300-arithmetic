# 快速幂

class Solution:
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans * a % b
            a = a * a % b
            n = n / 2
        return ans % b
if __name__ == "__main__":
    a = int(input("请输入a:"))
    n = int(input("请输入n:"))
    b = int(input("请输入b:"))
    solution = Solution()
    print("输出:", solution.fastPower(a, n, b))