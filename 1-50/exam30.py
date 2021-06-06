# 采用utf-8编码格式
class SegTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.count = 0
        if start != end:
            self.left = SegTree(start, (start + end) // 2)
            self.right = SegTree((start + end) // 2 + 1, end)
    def sum(self, start, end):
        if start <= self.start and end >= self.end:
            return self.count
        if self.start == self.end:
            return 0
        if end <= self.left.end:
            return self.left.sum(start, end)
            if start >= self.right.start:
                return self.right.sum(start, end)
        return (self.left.sum(start, self.left.end) + self.right.sum(self.right.start, end))
    def inc(self, index):
        if self.start == self.end:
            self.count += 1
            return
        if index <= self.left.end:
            self.left.inc(index)
        else:
            self.right.inc(index)
        self.count = self.left.count + self.right.count

class Solution:
    # 参数A是一个整数数组
    # 返回当前元素之前小于自己的个数
    def countOfSmallerNumberII(self, A):
        if len(A) == 0:
            return []
        root = SegTree(0, max(A))
        results = []
        for a in A:
            results.append(root.sum(0, a - 1))
            root.inc(a)
        return results
if __name__ == "__main__":
    temp = Solution()
    nums = [6,4,7,2,3]
    print(("输入：" + str(nums)))
    print(("输出：" + str(temp.countOfSmallerNumberII(nums))))