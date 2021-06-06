# 参数A是一个整数数组
# 返回两个整数

class Solution:
    def singleNumberIII(self, A):
        s = 0
        for x in A:
            s ^= x
        y = s & (-s)
        ans = [0, 0]
        for x in A:
            if (x & y) != 0:
                ans[0] ^= x
            else:
                ans[1] ^= x
        return ans
if __name__ == '__main__':
    temp = Solution()
    List1 = [2,3,1,1,4]
    List2 = [1,4,2,2,3]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.singleNumberIII(List1))))
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.singleNumberIII(List2))))