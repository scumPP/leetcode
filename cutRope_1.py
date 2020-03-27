'''
题目：剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
'''


def cuttingRope(n: int) -> int:
        F=[0 for _ in range(n+1)]
        def memorize(n):
            if F[n]!=0:
                return F[n]
            if n==2:
                return 1
            re=-1
            for i in range(1,n):
                re=max(re,max(i*(n-i),i*memorize(n-i)))
            F[n]=re
            return re
        re=memorize(n)
        return re
print(cuttingRope(10))