7.17日打卡

# LC 16 最接近的三数之和

题目：给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案

示例：

```c++
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
```

**思路**：

先排序，后使用双指针

- 排序后使得数组从小到大排序

- 然后固定一个数i，利用除了i以外的其他数组中的数字进行加和，我们可以定义两个index分别为j，k。j从前向后遍历，k从后往前遍历，故，可以得到以下的规律。

   - 当sum>target时，移动k

   - 当sum<target时，移动j

代码为

```c++
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int res=1e7;

        auto update = [&](int cur) {
            if (abs(cur - target) < abs(res - target)) {
                res = cur;
            }
        }; //类似于python中的lambda，即用即声明
        for(int i=0;i<nums.size();i++){
            //避免执行重复的值
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int j=i+1;
            int k=nums.size()-1;
            int pre_res=1e7;
            while(j<k){
                int cur_res=nums[i]+nums[j]+nums[k];
                if(cur_res==target){
                    return target;
                }
                update(cur_res);
                if(cur_res<target){
                    int jj=j+1;
                    //避免执行重复的值
                    while(jj<k && nums[jj]==nums[j]){
                        jj++;
                    }
                    j=jj;
                }
                if(cur_res>target){
                    int kk=k-1;
                    //避免执行重复的值
                    while(j<kk && nums[kk]==nums[k]){
                        kk--;
                    }
                    k=kk;
                }
            }
        }
        return res;
    }

```

