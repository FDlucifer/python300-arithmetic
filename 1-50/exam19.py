# 参数nums1是一个长度为m，数字是0 - 9的整数数组
# 参数nums2是一个长度为n，数字是0 - 9的整数数组
# 参数k是一个整数，且k <= m+n
# 返回值是一个整数数组

class Solution:
    def maxNumber(self, nums1, nums2, k):
        len1, len2 = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = self.merge(self.getMax(nums1, x), self.getMax(nums2, k - x))
            res = max(tmp, res)
        return res
    def getMax(self, nums, t):
        ans = []
        size = len(nums)
        for x in range(size):
            while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                ans.pop()
            if len(ans) < t:
                ans.append(nums[x])
        return ans
    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
if __name__ == '__main__':
    temp = Solution()
    List1 = [1,-1,-2,1]
    List2 = [3,-2,2,1]
    k = 3
    print("输入：" + str(List1))
    print("输入：" + str(List2))
    print("输入：" + str(k))
    print("输出：" + str(temp.maxNumber(List1, List2, k)))