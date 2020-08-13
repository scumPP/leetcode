7.18 打卡

# LC 26 删除排序数组中的重复项

题目：给定一个排序数组，你需要在**原地**删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

**题目要求**：不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

思路：双指针的思路，指针i指向删除之后的索引，指针j指向当前数组的索引，然后进行遍历删除

代码：

```c++
int removeDuplicates(vector<int>& nums) {
    if(nums.size()==0)
        return 0;
    int i=0,j=1;
    for(j=1;j<nums.size();j++){
        if(nums[j]!=nums[i]){
            i++;
            nums[i]=nums[j];
        }

    }
    return i+1;
}
```


# LC 27 移除元素

题目：给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

**题目要求**：不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并**原地**修改输入数组。元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

思路:依旧是双指针，题目明确指出移除后的数组元素顺序可以改变，于是我们可以使用两个指针从数组两边遍历，将需删除的元素与尾指针不需删除的元素进行交换

具体代码：

```c++
int removeElement(vector<int>& nums, int val) {
    if(nums.size()==0)
        return 0;
    int i=0,j=nums.size()-1;  
    while(i<=j){
        if(nums[i]==val && nums.size()==1)
            return 0;
        if(nums[i]==val && nums[j]!=val){
            nums[i]=nums[j];
            j--;
        }
        if(nums[i]==val && nums[j]==val){
            j--;
            continue;
        }
        i++;
    }
    return j+1;
}
```
