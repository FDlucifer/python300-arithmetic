# 参数A是一个整数数组
# 返回一个整数

class Solution:
    def singleNumber(self, A):
        ans = 0;
        for x in A:
            ans = ans ^ x
        return ans
if __name__ == '__main__':
    temp = Solution()
    List1 = [4,6,4,6,3]
    List2 = [2,1,1,1,1]
    print(("输入：" + str(List1)))
    print(("输入：" + str(temp.singleNumber(List1))))
    print(("输入：" + str(List2)))
    print(("输入：" + str(temp.singleNumber(List2))))