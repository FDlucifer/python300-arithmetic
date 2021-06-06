# 给出一个含有正整数和负整数的数组，将其重新排列成一个正负数交错的数组
# 参数A是一个整数数组
# 没有返回值

class Solution:
    def subfun(self, A, B):
        ans = []
        for i in range(len(B)):
            ans.append(A[i])
            ans.append(B[i])
        if (len(A) > len(B)):
            ans.append(A[-1])
        return ans
    
    def rerange(self, A):
        Ap = [i for i in A if i>0]
        Am = [i for i in A if i<0]
        if (len(Ap) > len(Am)):
            tmp = self.subfun(Ap, Am)
        else:
            tmp = self.subfun(Am, Ap)
        for i in range(len(tmp)):
            A[i] = tmp[i];
if __name__ == '__main__':
    temp = Solution()
    List1 = [-1,-2,-3,4,5,6]
    List2 = [2,-4,6,8,-10]
    print(("输入：" + str(List1)))
    temp.rerange(List1)
    print(("输出：" + str(List1)))
    print(("输入：" + str(List2)))
    temp.rerange(List2)
    print(("输出：" + str(List2)))
