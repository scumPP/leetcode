7.23 打卡

# LC Offer 09  两个栈实现队列的增删

思路：由于栈和队列的特点，在删除时要注意借助另一个栈来删除。

代码：

```c++
stack<int> s1,s2;
CQueue() {
    while(!s1.empty()){
        s1.pop();
    }
    while(!s2.empty()){
        s2.pop();
    }
}
void appendTail(int value) {
    s1.push(value);
}
int deleteHead() {
    //int value;
    if(s2.empty()){
        while(!s1.empty()){
            s2.push(s1.top());
            s1.pop();
        }
    }
    if(s2.empty()){
        return -1;
    }else{
        int value=s2.top();
        s2.pop();
        return value;
    }
}
```

# LC Offer 10  青蛙跳台阶

题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

思想：DP，将问题分解。当青蛙跳的只剩最后一个台阶时，目前有f(n-1)种跳法；当青蛙跳的只剩下两个台阶时，目前有f(n-2)中跳法；因此递归方程为：
$dp[n]=dp[n-1]+dp[n-2]$

代码为：

```c++
int numWays(int n) {
    if(n<=1) return 1;
    vector<int> dp(n+1);
    dp[0]=1;
    dp[1]=1;
    for(int i=2;i<=n;i++){
        dp[i]=(dp[i-1]+dp[i-2])%1000000007;
    }
    return dp[n];
}
```