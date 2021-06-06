# 参数A是一个整数数组
# 返回一个整数

class Solution:
    def singleNumberII(self, A):
        n = len(A)
        d = [0 for i in range(32)]
        for x in A:
            for j in range(32):
                if (((1 << j) & x) > 0):
                    d[j] += 1
        ans = 0
        for j in range(32):
            t = d[j] % 3
            if (t == 1):
                ans = ans + (1 << j)
            elif (t != 0):
                return -1
        return ans
if __name__ == '__main__':
    temp = Solution()
    List1 = [4,6,4,6,3,4,6]
    List2 = [2,1,1,1,1,1,1]
    print(("输入：" + str(List1)))
    print(("输入：" + str(temp.singleNumberII(List1))))
    print(("输入：" + str(List2)))
    print(("输入：" + str(temp.singleNumberII(List2))))