#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    unordered_map<string, int> hash_map;
    
    for (const auto& parti: participant) {
        hash_map[parti]++;
    }
    
    for (const auto& comp: completion) {
        hash_map[comp]--;
    }
    
    for (const auto& map: hash_map) {
        if (map.second > 0) {
            return map.first;
        }
    }
    
    return "";
}