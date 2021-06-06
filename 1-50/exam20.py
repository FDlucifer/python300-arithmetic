# 参数A是一个整数数组
# 参数target是一个整数
# 参数k是一个整数
# 返回值是一个整数数组

class Solution:
    def kClosestNumbers(self, A, target, k):
        # 找到 A[left] < target, A[right] >= target
        # 最接近target的两个数，肯定是相邻的
        right = self.find_upper_closest(A, target)
        left = right - 1
        # 两个指针从中间往两边扩展，依次找到最接近K个数
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        return results
    def find_upper_closest(self, A, target):
        # 找到A中第一个大于等于target的数字
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        # 找不到的情况
        return end + 1
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
if __name__ == '__main__':
    temp = Solution()
    A = [4,2,5,6,3,4,5,9]
    target = 4
    k = 4
    print(("输出：" + str(temp.kClosestNumbers(A, target, k))))