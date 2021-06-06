# 找出大于或等于n的最小稀疏数
# 参数x是一个数字
# 返回x后面的下一个稀疏数

class Solution:
    def nextSparseNum(self, x):
        b_x = bin(x)[2:]
        pos = self.find_highest_continue_one(b_x)
        while pos != -1:
            if pos == 0:
                b_x = "1" + "0" * len(b_x)
            else:
                b_x = b_x[:pos - 1] + "1" + (len(b_x) - pos) * "0"
            pos = self.find_highest_continue_one(b_x)
        return int(b_x, 2)
    def find_highest_continue_one(self, s):
        n = len(s)
        for i in range(n - 1):
            if s[i] == s[i + 1] == "1":
                return i
        return - 1

if __name__ == '__main__':
    temp = Solution()
    nums1 = 16
    nums2 = 50
    print(("输入:" + str(nums1)))
    print(("输入:" + str(temp.nextSparseNum(nums1))))
    print(("输入:" + str(nums2)))
    print(("输入:" + str(temp.nextSparseNum(nums2))))