# 参数n是一个整数
# 返回只含素因子的第n个最小的数
import heapq

class Solution:
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for multi in [2, 3, 5]:
                if val * multi not in visited:
                    visited.add(val * multi)
                    heapq.heappush(heap, val * multi)
        return val
if __name__ == "__main__":
    n = 9
    print("输入的n是：", n)
    solution = Solution()
    print("只含素因子2，3，5的第n小的数是:", solution.nthUglyNumber(n))