#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums)
{
    int N = nums.size();
    // 가져갈 수 있는 수는 N/2
    unordered_set<int> check(nums.begin(), nums.end());
    
    int answer = check.size();
    
    if (answer > N/2) {
        answer = N/2;
    }
    
    return answer;    
}