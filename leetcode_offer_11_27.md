7.24 打卡

# LC Offer 11 旋转数组的最小数字

题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1

思路：二分查找法

- 如果nums[mid]<nums[high], 在左半部分查找最小值
- 如果nums[mid]>nums[high], 在右半部分查找最小值
- 如果nums[mid]==nums[high], 不确定选择左右不分，于是先把high向左移动，进行下一轮选择

代码为：

```c++
int minArray(vector<int>& numbers) {
    int low=0,high=numbers.size()-1;
    while(low<high){
        int middle=low+(high-low)/2;
        if(numbers[middle]<numbers[high]){
            high=middle;
        }else if(numbers[middle]>numbers[high]){
            low=middle+1;
        }else{
            high--;
        }
    }
    return numbers[low];
}
```

# LC Offer 27 二叉树的镜像

题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

思路：递归思想，将左子树与右子树进行交换

代码：

```c++
public:
    TreeNode* mirrorTree(TreeNode* root) {
        if(root!=NULL){
            TreeNode* temp=root->left;
            root->left=mirrorTree(root->right);
            root->right=mirrorTree(temp);
            return root;
        }else{
            return NULL;
        } 
    }
```