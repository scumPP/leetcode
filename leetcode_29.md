# LC 两数相除

题目：给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

**提示**：

- 被除数和除数均为 32 位有符号整数。
- 除数不为 0。
- 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

示例：

```c++
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
```

## 思想

由于不使用乘除法和mod，那么就从简单的加减法入手。
参考了高赞答案——递归，思路大致这样：以10/3为例:

a. 10>3,那么熵res最起码是1
b. 3+3=6<10，此时熵最起码是2;
b. 6+6=12>10，10-6=4，那么4是3的几倍呢？这又回到了除法，即递归开始了;

再讨论特殊情况，即整数溢出情况。
为了防止溢出，需要特殊考虑三种情况：

- 除数为-1时，被除数不是最小的整型时，直接返回被除数的相反数；如果被除数是最小的整型，那么溢出，返回最大整型。

具体代码为：

```c++
int curr_div(int a,int b){
    if(a>b) return 0;
    int count=1;
    int temp=b;
    //此条件就是a-(temp+temp)>=0
    while(temp-a+temp>=0){
        count+=count;
        temp+=temp;
    }
    return count+curr_div(a-temp,b);
}
int divide(int dividend, int divisor) {
    //特殊情况
    if(dividend==0) return 0;
    if(divisor==1) return dividend;
    if(divisor==-1){
        if(dividend>INT_MIN) 
            return -dividend;
        return INT_MAX;
    }
    //记录结果的正负
    int sign=1;
    if((dividend>0 && divisor<0) || (dividend<0 && divisor>0))
        sign=-1;
    //都变成负数，防止溢出
    int a=dividend>0?-dividend:dividend;
    int b=divisor>0?-divisor:divisor;
    int res=curr_div(a,b);
    return sign==1?res:-res;
}
```

