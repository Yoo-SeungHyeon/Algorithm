#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int canDun(int health, vector<int> permu, vector<vector<int>> dun) {
    int result = 0;
    
    for (int i = 0; i < permu.size(); i++) {
        int dunIdx = permu[i];
        
        if (health >= dun[dunIdx][0]) {
            health -= dun[dunIdx][1];
            result++;
        } else {
            break;
        }
    }
    
    return result;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    vector<int> idx(dungeons.size());
    
    for(int i=0; i<dungeons.size(); i++) {
        idx[i] = i;
    }
    
    do {
        int temp = canDun(k, idx, dungeons);
        if (temp > answer) {
            answer = temp;
        }
    } while (next_permutation(idx.begin(), idx.end()));
    
    return answer;
}