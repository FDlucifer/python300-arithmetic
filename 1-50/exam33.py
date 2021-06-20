# 采用utf-8编码格式
# 参数A是一个正整数，有n个数字，A是字符串类型
# 参数k是删除k个数字
# 返回值是字符串

class Solution:
    def DeleteDigits(self, A, k):
        A = list(A)
        while k > 0:
            f = True
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    del A[i]
                    f = False
                    break
            if f and len(A) > 1:
                A.pop()
            k -= 1
        while len(A) > 1 and A[0] == '0':
            del A[0]
        return ''.join(A)
if __name__ == "__main__":
    temp = Solution()
    num_str = "123456789"
    k = 5
    print(("输入：" + num_str + " " + str(k)))
    print(("输出：" + str(temp.DeleteDigits(num_str, k))))