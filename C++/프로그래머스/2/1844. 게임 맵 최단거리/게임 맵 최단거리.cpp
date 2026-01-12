#include <vector>
#include <queue>

using namespace std;

int answer = -1;

void bfs(vector<vector<int>>& map) {
    
    int n = map.size(); // 높이
    int m = map[0].size(); //너비
    
    // 상,하,좌,우
    vector<int> di = {-1,1,0,0};
    vector<int> dj = {0,0,-1,1};
    vector<vector<int>> check(n, vector<int>(m, 0));
    
    queue<vector<int>> q;
    q.push({0,0,1});
    check[0][0] = 1;
    
    while (!q.empty()) {
        vector<int> now = q.front(); // 좌표 (0,0) (1,1)
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            // 맵을 벗어나지 않고, 벽이 아니고, 지나온적이 없는 경우
            int ni = di[i] + now[0];
            int nj = dj[i] + now[1];
            
            if (ni >= 0 && ni < n && nj >= 0 && nj < m){
                if (map[ni][nj] == 1 && check[ni][nj] == 0) {
                    
                    if (ni == n -1 && nj == m - 1) {
                        answer = now[2] + 1;
                        return;
                    }
                    
                    q.push({ni, nj, now[2] + 1});
                    check[ni][nj] = 1;
                }
            }
        }
    }
    return;
}


int solution(vector<vector<int> > maps)
{
    answer = -1;
    bfs(maps);
    return answer;
}