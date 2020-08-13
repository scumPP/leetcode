7.26  打卡

#LC Offer 12 矩阵中的路径

题目：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）

```c++
 [["a","b","c","e"],
 ["s","f","c","s"],
 ["a","d","e","e"]]
```

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

思路：回溯递归。首先在矩阵中找到和目标字符串第一个相同的位置，然后进行回溯。

- 回溯出口是当目前的字符都已匹配完毕
- 做出的选择是当前路径经过的下一个位置
- 注意不能走重复的路，因此要设置一个矩阵记录是否访问过

代码：

```c++
    bool backtrack(vector<vector<char>>& board,vector<vector<bool>>& isVisited,string& word,int cur_pos,int row,int col){
        if(cur_pos==word.size()){
            return true;
        }
        isVisited[row][col]=true;
        cur_pos++;
        int dx[4]={-1,1,0,0};
        int dy[4]={0,0,1,-1};
        for(int m=0;m<4;m++){
            int cur_row=row+dx[m];
            int cur_col=col+dy[m];
            if (cur_row<0 || cur_row>=board.size() || cur_col<0 || cur_col>=board[0].size() || board[cur_row][cur_col]!=word[cur_pos-1] || isVisited[cur_row][cur_col]){
                continue;
            }else{
                if (backtrack(board,isVisited,word,cur_pos,cur_row,cur_col))
                    return true;
            }  
        }
        isVisited[row][col]=false;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<bool>>isVisited(board.size(),vector<bool>(board[0].size(),0));
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(board[i][j]==word[0]){
                    bool res=backtrack(board,isVisited,word,1,i,j);
                    if(res==true){
                        return true;
                    }
                }
            }
        }
        return false;    
    }
```