#include <string>
#include <vector>
#include <queue>

using namespace std;

int answer = 0;
int canChange(string now, string next) {
    int count = 0;
    for (int i = 0; i < now.length(); i++) {
        if (now[i] != next[i]) {
            count++;
        }
    }
    return (count == 1) ? 1 : 0;
}

void bfs(string begi, string targe, vector<string> word) {
    vector<int> check(word.size(), 0);
    queue<pair<string, int>> q;
    
    q.push({begi, 0}); 

    while (!q.empty()) {
        string now = q.front().first;
        int dist = q.front().second;
        q.pop();

        for (int i = 0; i < word.size(); i++) {
            if (canChange(now, word[i]) && check[i] == 0) {
                if (word[i] == targe) {
                    answer = dist + 1;
                    return;
                }
                
                check[i] = 1;
                q.push({word[i], dist + 1});
            }
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    bfs(begin, target, words);
    
    return answer;
}