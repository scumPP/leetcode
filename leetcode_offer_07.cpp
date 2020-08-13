#include <iostream>
#include <vector>
using namespace std;

vector<int> pre_index;
vector<int> in_index;

struct TreeNode
{
    int val;
    struct TreeNode *left, *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int find_root_index(int pre_root)
{
    int index = 0;
    for (int i = 0; i < in_index.size(); ++i)
    {
        if (in_index[i] == pre_index[pre_root]){
            index = i;
            break;
        }
            
    }
    return index;
}

TreeNode *recurrent(int pre_root, int inorder_begin, int inorder_end)
{
    if (inorder_begin > inorder_end)
        return NULL;
    TreeNode *root = new TreeNode(pre_index[pre_root]);
    int cur_root = find_root_index(pre_root);
    root->left=recurrent(pre_root + 1, inorder_begin, cur_root - 1);
    root->right=recurrent(pre_root + cur_root - inorder_begin + 1, cur_root + 1, inorder_end);
    return root;
}

TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
{
    pre_index = preorder;
    in_index = inorder;

    int inorder_begin = 0, inorder_end = inorder.size() - 1;
    return recurrent(0, inorder_begin, inorder_end);
}

void print_node(TreeNode *root)
{
    if (root == nullptr)
        return;
    else
    {
        cout << root->val << endl;
        print_node(root->left);
        print_node(root->right);
    }
}

int main()
{
    vector<int> pre = {1,2,3};
    vector<int> in = {2,3,1};
    TreeNode *root = buildTree(pre, in);

    print_node(root);

    return 0;
}