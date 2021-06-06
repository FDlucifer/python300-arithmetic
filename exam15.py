# 输出将n个数合并成一个数后消耗的最小能量
# 参数numbers代表了数字数量
# 返回值是最小的能量消耗
import heapq

class Solution:
    def mergeNumber(self, numbers):
        Q = []
        ans = 0
        for i in numbers:
            heapq.heappush(Q, i)
        while(len(Q) > 1):
            a = heapq.heappop(Q)
            b = heapq.heappop(Q)
            ans = ans + a + b
            heapq.heappush(Q, a + b)
        return ans
if __name__ == '__main__':
    temp = Solution()
    List1 = [1,2,3,4,5]
    List2 = [6,7,8,9,10]
    print(("输入:" + str(List1)))
    print(("输出:" + str(temp.mergeNumber(List1))))
    print(("输入:" + str(List2)))
    print(("输出:" + str(temp.mergeNumber(List2))))