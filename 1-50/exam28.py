# 参数num是一个字符串
# 返回一个布尔值，判断这个数字是不是镜像的
class Solution:
    def isStrobogrammatic(self, num):
        map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        i, j = 0, len(num) - 1
        while i <= j:
            if not num[i] in map or map[num[i]] != num[j]:
                return False
            i, j = i + 1, j - 1
        return True
if __name__ == "__main__":
    num = "69"
    solution = Solution()
    print("初始值是：", num)
    print("结果是：", solution.isStrobogrammatic(num))
