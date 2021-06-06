# 采用utf-8编码格式
# 参数k,n为两个整数
# 返回值是一个整数
class Solution:
    def digitCounts(self, k, n):
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        for i in range(n + 1):
            j = i
            while True:
                if j % 10 == k:
                    count += 1
                j /= 10
                if j == 0:
                    break
        return count

if __name__ == "__main__":
    temp = Solution()
    k1 = 1
    n1 = 12
    k2 = 2
    n2 = 22
    print(("输入：" + str(k1) + " " + str(n1)))
    print(("输出：" + str(temp.digitCounts(k1,n1))))
    print(("输入：" + str(k2) + " " + str(n2)))
    print(("输出：" + str(temp.digitCounts(k2,n2))))