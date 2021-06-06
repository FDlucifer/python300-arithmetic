class Solution:
    def aplusb(self, a, b):
        while b != 0:
            a, b = (a^b)&0xffffffff, (a&b) << 1
        return a

if __name__ == "__main__":
    temp = Solution()
    num1 = 8
    num2 = 18
    print(("输入:" + str(num1) + " " + str(num2)))
    print(("输出:" + str(temp.aplusb(num1, num2))))