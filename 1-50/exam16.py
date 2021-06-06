# 给定一个字符串，验证其是否为数字
# 参数s是一个字符串
# 返回一个布尔值
# 有限的自动化

class Solution:
    def isNumber(self, s):
        INVALID = 0; SPACE = 1; SIGN = 2; DIGIT = 3; DOT = 4; EXPONET = 5
        # 0是无效的， 1空格， 2符号， 3数字， 4小数点， 5指数， 6输入的数字
        transitionTable = [[-1,0,3,1,2,-1],   # 状态0代表没有输入或是空格
                            [-1,8,-1,1,4,5],   # 状态1输入是数字
                            [-1,-1,-1,4,-1,-1], # 状态2代表前面没有数字只有小数点
                            [-1,-1,-1,1,2,-1],  # 状态3代表符号
                            [-1,8,-1,4,-1,5],   # 状态4代表数字其前方有小数点
                            [-1,-1,6,7,-1,-1],  # 状态5代表输入是e或者E
                            [-1,-1,-1,7,-1,-1], # 状态6代表在符号之后输入e
                            [-1,8,-1,7,-1,-1],  # 状态7代表在数字之后输入e
                            [-1,8,-1,-1,-1,-1]] # 状态8代表在输入有限输入后输入空格
        state = 0; i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ': inputtype = SPACE
            elif s[i] == '-' or s[i] == '+': inputtype = SIGN
            elif s[i] in '0123456789': inputtype = DIGIT
            elif s[i] == '.': inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E': inputtype = EXPONET
            state = transitionTable[state][inputtype]
            if state == -1: return False
            else: i += 1
        return state == 1 or state == 4 or state == 7 or state == 8
if __name__ == '__main__':
    temp = Solution()
    string1 = "3"
    string2 = "25"
    string3 = "casdcasd23423"
    print(("输入:" + string1))
    print(("输出:" + str(temp.isNumber(string1))))
    print(("输入:" + string2))
    print(("输出:" + str(temp.isNumber(string2))))
    print(("输入:" + string3))
    print(("输出:" + str(temp.isNumber(string3))))