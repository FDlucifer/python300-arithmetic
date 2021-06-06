# 四数乘积小于或等于正整数方案

class Solution:
    def numofplan(self, n, a, k):
        sum = [0] * 1000010
        cnt = [0] * 1000010
        for i in range(n):
            if a[i] > k:
                continue
            cnt[a[i]] += 1
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] * a[j] > k:
                    continue
                sum[a[i] * a[j]] += 1
        for i in range(1, k + 1):
            cnt[i] += cnt[i - 1]
            sum[i] += sum[i - 1]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = a[i] * a[j]
                if res > k:
                    continue
                res = k // res
                ans += sum[res]
                if a[i] <= res:
                    ans -= cnt[res // a[i]]
                    if a[i] <= res // a[i]:
                        ans += 1
                if a[j] <= res:
                    ans -= cnt[res // a[j]]
                    if a[j] <= res // a[j]:
                        ans += 1
                if a[i] * a[j] <= res:
                    ans += 1
        return ans // 6
if __name__ == "__main__":
    n = 5
    a = [1,1,1,2,2]
    k = 3
    solution = Solution()
    print("方案总数为：", solution.numofplan(n, a, k))