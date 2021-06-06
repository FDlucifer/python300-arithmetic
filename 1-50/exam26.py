# 参数nums是一个数字数组
# 返回值：返回一个单一数字

class Solution:
    def getSingleNumer(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid - 1]:
                if (mid - left + 1) % 2 == 1:
                    right = mid - 2
                else:
                    left = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (right - mid + 1) % 2 == 1:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                return nums[mid]
        return nums[left]

if __name__ == '__main__':
    temp = Solution()
    nums = [1,1,2,2,3,4,4,5,5]
    print(("输入：" + str(nums)))
    print(("输出：" + str(temp.getSingleNumer(nums))))