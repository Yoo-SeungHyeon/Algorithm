#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    int answer = 1;
    
    unordered_map<string, int> hash_map;
    
    for (const auto& cloth: clothes) {
        hash_map[cloth[1]]++;
    }
    
    vector<int> temp = {};
    
    for (const auto& map: hash_map) {
        answer *= (map.second + 1);
    }
    
    
    
    return answer - 1;
}