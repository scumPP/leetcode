# 机器人的运动范围

题目：地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例：

```c++
输入：m = 2, n = 3, k = 1
输出：3

输入：m = 3, n = 1, k = 0
输出：1
```

**思想**：广度优先遍历思想，因此需要队列的协助来完成。由于题目的限制条件是大于某个值时是不符合要求的，因此我们只需考虑向下和向右走的情况，即

```C++
[x,y]={1,0}
[x,y]={0,1}
``` 

以上两种情况。   
此外，为了防止重复记录，还要设置一个判断是否访问过的数组。具体代码如下：

```c++
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
```