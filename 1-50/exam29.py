# 参数A是一个整数数组
# 返回值是该数组中小于给定整数的元素数量

class Solution:
    def countOfSmallerNumber(self, A, queries):
        A = sorted(A)
        results = []
        for q in queries:
            results.append(self.countSmaller(A, q))
        return results
    def countSmaller(self, A, q):
        # 找到A >= q的第一个数字
        if len(A) == 0 or A[-1] < q:
            return len(A)
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < q:
                start = mid
            else:
                end = mid
        if A[start] >= q:
            return start
        if A[end] >= q:
            return end
        return end + 1
if __name__ == "__main__":
    A = [1, 2, 7, 8, 5]
    print("输入的数组是：", A)
    solution = Solution()
    print("数组中小于给定整数[1,8,5]的元素数量是：", solution.countOfSmallerNumber(A, [1, 8, 5]))