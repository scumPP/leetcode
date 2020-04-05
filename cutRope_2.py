'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
与上道题唯一不同在于本题目涉及 “大数越界情况下的求余问题”

由于语言特性，理论上 Python 中的变量取值范围由系统内存大小决定（无限大），因此在 Python 中其实不用考虑大数越界问题。
'''
def cuttingRope(n: int) -> int:
        if n<4:return n-1
        a,b=n//3,n%3
        if b==0:
            return (3**a)%(1000000007)
        elif b==1:
            return (3**(a-1))*4%(1000000007)
        else:
            return (3**a)*2%(1000000007)
print(cuttingRope(10))