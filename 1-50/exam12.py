# 给定一个正整数n，如果n为偶数，将n替换为n/2，如果n为奇数，将n替换为n+1或n-1，那么将n转换为1，最少替换次数为多少？

# 采用utf-8编码格式
# 参数n是一个正整数
# 返回值是最少的替换次数
# 直接使用DFS算法
# 类似于因式分解

class Solution:
    def integerReplacement(self, n):
        memo = {}
        # if n == 1:
        # return 0
        self.dfs(n, memo)
        print(memo[n])
        return len(memo[n]) - 1
    def dfs(self, n, memo):
        temp = []
        if n in memo:
            return memo[n]
        if n == 1:
            temp.append(1)
            memo[1] = temp
            return temp
        if n % 2 == 0:
            temp.append(n)
            cur = self.dfs(n // 2, memo)
            temp.extend(cur)
            memo[n] = temp
            return temp
            # temp.pop()
        else:
            temp2 = temp.copy()
            n2 = n
            temp.append(n)
            cur = self.dfs((n + 1), memo)
            temp.extend(cur)
            temp2.append(n)
            cur2 = self.dfs((n2 - 1), memo)
            temp2.extend(cur2)
            if len(temp) < len(temp2):
                memo[n] = temp
                return temp
            else:
                memo[n] = temp2
                return temp2

if __name__ == '__main__':
    temp = Solution()
    nums1 = 8
    nums2 = 18
    nums3 = 23
    print(("输入:" + str(nums1)))
    print(("输出:" + str(temp.integerReplacement(nums1))))
    print(("输入:" + str(nums2)))
    print(("输出:" + str(temp.integerReplacement(nums2))))
    print(("输入:" + str(nums3)))
    print(("输出:" + str(temp.integerReplacement(nums3))))