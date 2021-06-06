# 罗马数字转换为整数

class Solution:
    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if s == "":
            return 0

        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum
if __name__ == "__main__":
    temp = Solution()
    string1 = "DCXXI"
    string2 = "XX"
    print(("输入：" + string1))
    print(("输出：" + str(temp.romanToInt(string1))))
    print(("输入：" + string2))
    print(("输出：" + str(temp.romanToInt(string2))))