# 参数n是一个整数
# 输出是一个整数

class Solution:
    def trailingZeros(self, n):
        sum = 0
        while n != 0:
            n //= 5
            sum += n
        return sum
if __name__ == "__main__":
    n = 11
    print("初始值：", n)
    solution = Solution()
    print("结果：", solution.trailingZeros(n))