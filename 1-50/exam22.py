# 参数为一个数组
# 返回一个数组
class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        stack, res = [], [ -1 for i in range(len(nums))]
        for i in range(len(nums)):
            if stack and nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    pop_index = stack.pop()
                    res[pop_index] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            if stack and nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    pop_index = stack.pop()
                    res[pop_index] = nums[i]
            stack.append(i)
            if nums[stack[0]] == nums[stack[-1]]:
                break
        return res

# 主函数
if __name__ == "__main__":
    nums = [1,2,3,4,2,4,1,-1]
    # 创建对象
    solution = Solution()
    print("输入的数组是：",nums)
    print("计算后的结果：",solution.nextGreaterElements(nums))