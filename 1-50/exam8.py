# 将整数A转换为整数B需要改变的bit位数

class Solution:
    def bitSwapRequired(self, a, b):
        c = a ^ b
        cnt = 0
        for i in range(32):
            if c & (1 << i) != 0:
                cnt += 1
        return cnt
if __name__ == "__main__":
    temp = Solution()
    a1 = 4; b1 = 45
    a2 = 10; b2 = 26
    print(("输入：" + str(a1) + " " + str(b1)))
    print(("输出：" + str(temp.bitSwapRequired(a1,b1))))
    print(("输入：" + str(a2) + " " + str(b2)))
    print(("输出：" + str(temp.bitSwapRequired(a2,b2))))