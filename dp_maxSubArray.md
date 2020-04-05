# 此篇主要是关于动态规划的题目

## 动态规划的思路

1. 明确dp数组的含义

2. 定义 base case 就是dp[0],dp[0][..]的含义

3. 定义状态转移方程

## 以下是动态规划的题目

### 题目一：最大子序列和————Simple

题目描述：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

求和问题，从我们平时的经验知道，现在我们有两个数字$a$和$b$，想让他们的和最大，那么在已知$a$的情况下，$b>0$时，$a+b$的和总是大于$b<0$时$a+b$的和，因此我们将子序列和可以看为：

当前元素>0时，我们就把它加进去，
当前元素<0时，我们就跳过。

1. 我们将$dp[i]$数组定义为前i个元素的和

2. **状态转移方程**就为：

$$dp[i]=max(dp[i-1],0)+nums[i]$$

也就是说，第i个元素的累加和只与前i-1的元素的和有关系

3. 那么，**base**怎么定义呢？

$dp[0]$，即前1个元素的和就是数组第的一个元素。

代码如下：

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        max_sum=nums[0]

        dp=[0 for _ in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1],0)+nums[i]
            max_sum=max(dp[i],max_sum)

        return max_sum
```

