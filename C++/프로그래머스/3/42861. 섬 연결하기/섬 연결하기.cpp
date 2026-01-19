#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    vector<vector<int>> graph(n, vector<int>(n, INF));
    
    for (int i = 0; i < n; i++) graph[i][i] = 0;
    
    for (const auto& edge : costs) {
        graph[edge[0]][edge[1]] = edge[2];
        graph[edge[1]][edge[0]] = edge[2];
    }

    vector<int> min_dist(n, INF);
    vector<bool> visited(n, false);

    min_dist[0] = 0;

    for (int i = 0; i < n; i++) {
        int curr = -1;
        int min_val = INF;

        for (int j = 0; j < n; j++) {
            if (!visited[j] && min_dist[j] < min_val) {
                min_val = min_dist[j];
                curr = j;
            }
        }

        if (curr == -1) break;
        visited[curr] = true;
        answer += min_val;
        for (int next = 0; next < n; next++) {
            if (!visited[next] && graph[curr][next] != INF) {
                if (graph[curr][next] < min_dist[next]) {
                    min_dist[next] = graph[curr][next];
                }
            }
        }
    }

    return answer;
}