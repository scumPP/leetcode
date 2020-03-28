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

##递归+备忘录的方法
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

###动态规划的方法
def cuttingRope_Dp(n):
    dp=[0 for _ in range(n+1)]
    dp[2]=1
    for i in range(3,n+1):
        for j in range(0,i):
            dp[i]=max(dp[i],max(j*(i-j),j*dp[i-j]))
    return dp[n]

print(cuttingRope_Dp(10))

'''
基于贪心规则的方法：
第一优先级： 3；把数字 n 拆成尽可能多的 3之和；
特殊情况： 拆完后，如果余数是 1；则应把最后的 3 + 1 替换为 2 + 2，因为后者乘积更大；
第二优先级： 2；留下的余数如果是 2，则保留，不再拆为 1+1。

作者：jyd
链接：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
def foundRule(n):
    if n<3:
        return n-1
    a,b=n//3,n%3
    
    if b==0:
        return pow(3,a)
    elif b==1:
        return pow(3,a-1)*4
    else:
        return pow(3,a)*2
print(foundRule(10))
