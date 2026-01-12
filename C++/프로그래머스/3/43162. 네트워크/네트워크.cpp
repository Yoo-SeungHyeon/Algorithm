#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> check(200, 0);

void bfs(int node, vector<vector<int>> comput){
    queue<int> q;
    q.push(node);
    
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        check[now] = 1;
        
        vector<int> node_vector = comput[now];
        
        for (int i = 0; i < node_vector.size(); i++) {
            if (comput[now][i] == 1 && check[i] == 0) {
                q.push(i);
                check[i] = 1;
            }
        }
        
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for (int i = 0; i < computers.size(); i++) {
        if (check[i] == 0) {
            answer++;
            bfs(i, computers);
        }
    }
    
    return answer;
}