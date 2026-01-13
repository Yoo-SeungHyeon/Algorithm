#include <string>
#include <vector>
#include <unordered_set>
#include <cmath>

using namespace std;

int solution(int N, int number) {
    if (N == number) return 1;

    vector<unordered_set<int>> s(9);

    int base = 0;
    for (int i = 1; i <= 8; ++i) {
        base = base * 10 + N;
        s[i].insert(base);
    }

    for (int i = 1; i <= 8; ++i) {
        for (int j = 1; j < i; ++j) {
            for (int a : s[j]) {
                for (int b : s[i - j]) {
                    s[i].insert(a + b);
                    s[i].insert(a - b);
                    s[i].insert(a * b);
                    if (b != 0) s[i].insert(a / b);
                }
            }
        }
        if (s[i].find(number) != s[i].end()) {
            return i;
        }
    }

    return -1;
}