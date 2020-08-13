7.13打卡

# LC 51 N皇后问题

题目：n皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

**提示**：每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：

```c++
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
```

思路：经典回溯法

- 以每行为回溯点来进行构造整个回溯函数，因此回溯的出口就是，当前执行的行数等于题目所给的数字n

- 递归函数的思想是如果当前的位置可以放皇后，那么继续，如果不可以，就退回之前的状态。如下：

```c++
backtrack(当前的回溯对象){
    if(符合题目皇后位置的所有要求)
        将当前情况加入到最后结果中
    for(在选择列表里做不同的选择){
        if(当前行的位置不符合题目要求)
            contunue;
        做出选择；    
        backtrack(相应的参数需要改变);
        撤销选择;
    }
}
```

具体代码实现如下：

```c++
    vector<vector<string>> res;
    bool isValid(vector<string>& board,int cur_row,int cur_col){
        for(int i=0;i<board.size();i++){
            if(board[i][cur_col]=='Q')
                return false;
        }
        for(int i=cur_row-1,j=cur_col+1;(i>=0) && (j<board.size());i--,j++){
            if(board[i][j]=='Q')
                return false;
        }
        for(int i=cur_row-1,j=cur_col-1;(i>=0) && (j>=0);i--,j--){
            if(board[i][j]=='Q')
                return false;
        }
        return true;
    }
    void backtrack(vector<string>& board,int cur_row){
        if(cur_row==board.size()){
            res.push_back(board);
            return;
        }
        for(int cur_col=0;cur_col<board.size();cur_col++){
            if(!isValid(board,cur_row,cur_col)){
                continue;
            }
            board[cur_row][cur_col]='Q';
            backtrack(board,cur_row+1);
            board[cur_row][cur_col]='.';
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n,string(n,'.'));
        backtrack(board,0);
        return res;
    }
```

