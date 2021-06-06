# 要求不使用乘法，除法，和mod运算符，实现两个整数相除，如果溢出，返回 2147483647

# 采用utf-8 编码格式

class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            ans = -ans
        if ans > INT_MAX:
            return INT_MAX
        return ans
if __name__ == '__main__':
    temp = Solution()
    x1 = 130
    x2 = 12
    print(("输入:" + str(x1) + " " + str(x2)))
    print(("输出:" + str(temp.divide(x1,x2))))