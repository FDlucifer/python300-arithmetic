# x的n次幂

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1//x
            n = -n
        ans = 1
        tmp = x
        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //= 2
        return ans
if __name__ == "__main__":
    temp = Solution()
    num1 = 1234
    num2 = 3
    print(("输入:" + str(num1) + " " + str(num2)))
    print(("输出:" + str(temp.myPow(num1,num2))))