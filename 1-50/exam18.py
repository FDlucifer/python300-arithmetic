# 找到数组中每个窗口内的最大值
# 参数nums是一个整数数组
# 参数k是一个整数
# 返回值是数组中每个窗口内的最大值

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        dq = deque([])
        for i in range(k - 1):
            self.push(dq, nums, i)
        result = []
        for i in range(k - 1, len(nums)):
            self.push(dq, nums, i)
            result.append(nums[dq[0]])
            if dq[0] == i - k + 1:
                dq.popleft()
        return result
    def push(self, dq, nums, i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
if __name__ == '__main__':
    temp = Solution()
    List1 = [2,5,6,7,3,5,7,9]
    nums1 = 3
    print(("输入：" + str(List1) + " " + str(nums1)))
    print(("输出：" + str(temp.maxSlidingWindow(List1, nums1))))