#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    
    for (int i = 0; i < wires.size(); i++) {
        
        queue<int> q;
        q.push(1);
        
        vector<int> visit(n + 1, 0);
        visit[1] = 1;
        
        int count = 1;
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for (int j = 0; j < wires.size(); j++) {
                if (i == j) continue; 
                
                int neighbor = -1;
                if (wires[j][0] == node) neighbor = wires[j][1];
                else if (wires[j][1] == node) neighbor = wires[j][0];
                
                if (neighbor != -1 && visit[neighbor] == 0) {
                    q.push(neighbor);
                    visit[neighbor] = 1;
                    count++;
                }
            }
        }
        
        if (abs(2 * count - n) < answer) {
            answer = abs(2 * count - n);
        }
    }
    
    return answer;
}