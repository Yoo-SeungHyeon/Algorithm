#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(vector<int> nums, int tar, int depth, int result) {
    if (depth == nums.size()) {
        if (result == tar) {
            answer++;
        }
        return;
    }

    dfs(nums, tar, depth+1, result + nums[depth]);
    dfs(nums, tar, depth+1, result - nums[depth]); 
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    return answer;
}