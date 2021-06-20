# 参数num是一个整数
# 返回一个布尔值，如果是丑数则返回true,否则返回false

class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        while num >= 2 and num % 2 == 0:
            num /= 2;
        while num >= 3 and num % 3 == 0:
            num /= 3;
        while num >= 5 and num % 5 == 0:
            num /= 5;
        return num == 1
if __name__ == '__main__':
    num = 8
    print("初始值：", num)
    solution = Solution()
    print("是否为丑数：", solution.isUgly(num))