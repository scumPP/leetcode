#include <iostream>
#include <stack>
#include <stdio.h>
#include <vector>
#include <queue>
#include <utility>
using namespace std;
//计算数字之和
int compute(int number)
{
    int res = 0;
    while (number >= 1)
    {
        int cur_number = number % 10;
        res += cur_number;
        number = number / 10;
    }
    return res;
}

int movingCount(int m, int n, int k){
    int ans = 1; //存放结果个数
    vector<vector<int> > isVisited(m, vector<int>(n,0)); //是否被访问过
    isVisited[0][0] = 1;
    int dx[2] = {0, 1};
    int dy[2] = {1, 0};
    //利用广度优先遍历的思想，因此这里用队列
    queue<pair<int, int>> Q;
    Q.push(make_pair(0,0));
    while(!Q.empty()){
        pair<int,int> temp = Q.front();
        Q.pop();
        int x = temp.first;
        int y = temp.second;
        //向右或者向下走
        for (int i = 0; i < 2;i++){
            int next_x = x + dx[i];
            int next_y = y + dy[i];
            //判断下一步是否符合规则
            if(next_x<0 || next_y<0 || next_x>=m || next_y>=n || isVisited[next_x][next_y] || (compute(next_x)+compute(next_y)>k))
                continue;
            isVisited[next_x][next_y] = 1;
            Q.push(make_pair(next_x,next_y));
            ans++;
        }
    }
    return ans;
}

int main()
{
    int m = 2, n = 3, k = 1;
    int res = movingCount(m,n,k);
    cout << res << endl;
}