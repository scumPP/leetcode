7.22 打卡

# LC Offer 07 重建二叉树

题目：输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

思路：**分治递归**

- 通过前序结果可以确定二叉树的根，并可以找出对应的左右子树，如此往复就是递归的过程。
- 递归解析：
  - 递归出口：当子树遍历为空
  - 递归式： Recurrent(当前根在前序结果中的索引，当前根对应的左子树的左边界，当前根对应的左子树的右边界)

代码为：

```c++
struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x):val(x),left(NULL),right(NULL){}
};

vector<int> pre_index;
vector<int> in_index;

int find_index_in_inorder(int index){
    int res=0;
    for(int i=0;i<in_index.size();++i){
        if(pre_index[index]==in_index[i]){
            res=i;
            break;
        }
    }
    return res;
}

TreeNode* Recurrent(int root_index,int left_index,int right_index){
    if(left_index>right_index)
        return NULL;
    int root_index_in_order=find_index_in_inorder(root_index);
    TreeNode *root=new TreeNode(in_index[root_index_in_order]);
    root->left=Recurrent(root_index+1,left_index,root_index_in_order-1);
    root->right=Recurrent(root_index+root_index_in_order-left_index+1,root_index_in_order+1,right_index);
    return root;
}

TreeNode* buildTree(vector<int> &preorder,vector<int> &inorder){
    per_index=preorder;
    in_index=inorder;
    return Recurrent(0,0,inorder.size()-1);
}
```
