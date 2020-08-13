7.21 打卡

# 剑指Offer 03 数组中重复的数字

题目：在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

思路：如果没有重复的话，正常情况下排序后就是数组下标对应数组的值，因此，只要在排序过程中发现有重复的返回即可

代码

```c++
int findRepeatNumber(vector<int>& nums) {
    for(int i=0;i<nums.size();i++){
        while(nums[i]!=i){
            if(nums[i]==nums[nums[i]]){
                return nums[i];
            }else{
                swap(nums[i],nums[nums[i]]);
            }
        }
    }
    return -1;
}
```

# 剑指Offer 04 二维数组中的查找

题目：在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路：由于题目的规则，这个数组中的左下角和右上角是两个特殊的位置，即：

```c++
nums[n-1][0]代表此列最大的值，此行最小的值
nums[0][m-1]代表此列最小的值，此行最大的值
```

因此我们可以从其中一个入手，就能得到固定的移动规律：

```c++
比如从左下角入手：
当nums[i][j]>target, 向上走
当nums[i][j]<target, 向右走
```

代码如下：

```c++
bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
    if(matrix.size()==0 || matrix[0].size()==0)
        return false;
    int num_row=matrix.size();
    int num_col=matrix[0].size();
    int row=num_row-1,col=0;
    while(row>=0 && col<num_col){
        if(matrix[row][col]==target){
            return true;
        }else if(matrix[row][col]>target){
            row--;
        }else{
            col++;
        }
    }
    return false;
}
```

# 剑指Offer 05 替换空格

题目：请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

思路：此题考点是字符和字符串的区别，替换的内容“%20”是字符串，但是由于以字符型时替换，因此要注意一个个替换。

代码：

```c++
string replaceSpace(string s) {
    string ss="";
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            ss.push_back('%');
            ss.push_back('2');
            ss.push_back('0');
        }else{
            ss.push_back(s[i]);
        }
    }
    return ss;
}
```

# 剑指Offer 06 从尾到头打印链表

题目：输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

思路：使用栈保存，再输出。

代码：

```c++
vector<int> reversePrint(ListNode* head) {
    ListNode *p=head;
    stack<int> s;
    vector<int> res;
    while(p){
        s.push(p->val);
        p=p->next;
    }
    while(!s.empty()){
        res.push_back(s.top());
        s.pop();
    }
return res;
}
```