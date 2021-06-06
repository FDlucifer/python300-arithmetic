# n的类型是整数
# 返回值的类型是字符串数组

import collections
class Solution:
    def findStrobogrammatic(self, n):
        ROTATE = {}
        ROTATE["0"] = "0"
        ROTATE["1"] = "1"
        ROTATE["6"] = "9"
        ROTATE["8"] = "8"
        ROTATE["9"] = "6"
        queue = collections.deque()
        if n % 2 == 0:
            queue.append("")
        else:
            queue.append("0")
            queue.append("1")
            queue.append("8")
        result = []
        while queue:
            num = queue.popleft()
            if len(num) == n:
                result += [num] if num[0] != "0" or n == 1 else []
            else:
                for key, val in ROTATE.items():
                    queue.append(key + num + val)
        return result
if __name__ == "__main__":
    n = 2
    print("初始值：", n)
    solution = Solution()
    print("结果：", solution.findStrobogrammatic(n))