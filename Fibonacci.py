'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

###备忘录法
def fib(n: int) -> int:
        f=[-1 for _ in range(n+1)]
        
        def memorize(m):
            if f[m]!=-1:
                return f[m] 
            if m==0:
                f[0]=0
                return 0
            if m==1:
                f[1]=1
                return 1
            if m==2:
                f[2]=1
                return 1  
            re=0         
            for i in range(2,m+1):
                re=memorize(i-1)+memorize(i-2)
                f[i]=re
            return re
        
        return memorize(n)%1000000007

###动态规划法
def fib_dp(n: int) -> int:
        dp=[-1 for _ in range(n+1)]
        if n==0:
            dp[0]=0
        if n==1:
            dp[1]=1
        if n>1:
            dp[0]=0
            dp[1]=1
            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]

        return dp[n]%1000000007
print(fib_dp(5))