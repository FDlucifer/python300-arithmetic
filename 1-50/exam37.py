# 参数n是一个正整数
# 参数primes是一个给定的素数列表
# 返回一个整数，是第n个超级丑数
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        import heapq
        length = len(primes)
        times = [0] * length
        uglys = [1]
        minlist = [(primes[i] * uglys[times[i]], i) for i in range(len(times))]
        heapq.heapify(minlist)
        while len(uglys) < n:
            (umin, min_times) = heapq.heappop(minlist)
            times[min_times] += 1
            if umin != uglys[-1]:
                uglys.append(umin)
        heapq.heappush(minlist, (primes[min_times] * uglys[times[min_times]], min_times))
        return uglys[-1]
if __name__ == "__main__":
    n = 6
    primes = [2, 7, 13, 19]
    print("初始值：", n)
    print("质数集合：", primes)
    solution = Solution()
    print("第{}个丑数:".format(n), solution.nthSuperUglyNumber(n, primes))