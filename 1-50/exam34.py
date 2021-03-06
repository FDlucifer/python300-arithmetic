# 参数n是一个整数
# 参数str是一个字符串， 由1~n的整数随机组成，其中丢失了一个整数
# 返回一个整数
class Solution:
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.find(n, str, 0, used)
    def find(self, n, str, index, used):
        if index == len(str):
            results = []
            for i in range(1, n + 1):
                if not used[i]:
                    results.append(i)
            return results[0] if len(results) == 1 else -1
        if str[index] == '0':
            return -1
        for l in range(1, 3):
            num = int(str[index: index + l])
            if num >= 1 and num <= n and not used[num]:
                used[num] = True
                target = self.find(n, str, index + l, used)
                if target != -1:
                    return target
                used[num] = False
        return - 1
if __name__ == '__main__':
    n = 20
    str = "19201234567891011121314151618"
    print("n = ", n)
    print("str = ", str)
    solution = Solution()
    print("缺少的数字是：", solution.findMissing2(n, str))