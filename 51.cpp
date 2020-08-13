#include <vector>
#include <iostream>
using namespace std;

vector<vector<string>> res;
//vector<string> board(8, string(8, '.'));

bool isValid(vector<string>& board,int row,int col){
    //判断同一列是否有黑皇后
    for (int i = 0; i < board.size();i++){
        if (board[i][col]=='Q'){
            return false;
        }
    }
    //检查右上角
    for (int i = row - 1,  j = col+1; (i >= 0) && (j < board.size());i--,j++){
        if (board[i][j]=='Q')
            return false;
    }
    //检查左上角
    for (int i = row - 1, j = col-1; (i >= 0) && (j >= 0);i--,j--){
        if (board[i][j]=='Q')
            return false;
    }
    return true;
}

void backtrack(vector<string>& board,int cur_row){
    if(cur_row==board.size()){
        res.push_back(board);
        return;
    }
    for (int cur_col = 0; cur_col < board.size();cur_col++){
        if (!isValid(board,cur_row,cur_col))
            continue;
        board[cur_row][cur_col] = 'Q';
        backtrack(board, cur_row+1);
        board[cur_row][cur_col] = '.';
    }
        
}

vector<vector<string>> solveNQueens(int n){
    vector<string> board(n, string(n, '.'));
    if (n==0)
        return res;
    backtrack(board,0);
    return res;
}
int main(){
    //vector<string> board(8, string(8, '.'));
    //vector<vector<int>> array(5);
    // for (int i = 0; i<board.size(); i++){
    //     for (int j = 0; j < board[0].size();j++){
    //         cout << board[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    solveNQueens(4);
    cout <<"after"<<endl;
    for (vector<vector<string>>::iterator it = res.begin(); it != res.end();it++){
        for (vector<string>::iterator its = (*it).begin(); its != (*it).end();its++){
            cout << *its << endl;
        }
        cout << endl;
    }
}