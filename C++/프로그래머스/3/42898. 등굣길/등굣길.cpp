#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    vector<vector<int>> map(n+1, vector<int>(m+1, 0));
    
    for (int k = 0; k < puddles.size(); k++) {
        map[puddles[k][1]][puddles[k][0]] = -1;
    }
    
    map[1][1] = 1;
    
    for (int j = 1; j <= n; j++) {
        for (int i = 1; i <= m; i++) {
            if (map[j][i] == -1) {
                map[j][i] = 0;
            } else if (map[j][i] == 0) {
                map[j][i] = (map[j-1][i] + map[j][i-1]) % 1000000007;
            }
        }
    }
    
    return map[n][m];
}