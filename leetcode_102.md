# 二叉树的层序遍历

题目：给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7]

```c++
   3
  / \
 9  20
    / \
   15  7
```

返回其层次遍历结果为：

```c++
[
    [3],
    [9,20],
    [15,7]
]
```

**思想**：层次遍历的话就是以队列为核心，由于和一般的层次遍历相比，这道题的不同在于输出的时候是以每一层为单位输出为嵌套数组形式的，因此我们要把属于这一层的所有输出之后，再去输出下一层。

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > res;
        if(!root) return res
        queue<TreeNode*> Q;
        Q.push(root);
        while(!Q.empty()){
            int len_q=Q.size();
            res.push_back(vector<int> ());
            //将每一层的节点值保存
            for(int i=0;i<len_q;i++){
                TreeNode* temp=Q.front();
                Q.pop();
                res.back().push(temp->val);
                if(temp->left) 
                    Q.push(temp->left);
                if(temp->right) 
                    Q.push(temp->right);
            }
        }
        return res;
    }
};
```
