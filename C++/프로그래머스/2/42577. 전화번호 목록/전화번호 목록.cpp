#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    unordered_map<string, int> hash_map;
    
    for (const auto& phone: phone_book) {
        hash_map[phone] = 1;
    }
    
    for (const auto& phone: phone_book) {
        string temp = "";
        for (int i = 0; i < phone.size(); i++) {
            temp += phone[i];
            if (temp != phone && hash_map[temp]) {
                return false;
            }
        }
    }
    
    return true;
}