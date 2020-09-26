#include <iostream>
#include <string>
#include <vector>
using namespace std;

int lengthOfLongestSubstring(string s);

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int ans;
    ans = lengthOfLongestSubstring(s);
    cout << ans << endl;
    return 0;
}

int lengthOfLongestSubstring(string s) {
    // sliding window tech
    // a map to store character's latest position in s
    // here use a vector instead of map
    // because there are 128 chars at most
    vector<int> m(128, 0);
    int ans = 0;
    int i = 0;

    // for each character in s, store its position
    // if current char is in the latest window, then update left boundary
    // each time the right boundary goes further, check max length
    for (int j = 0; j < s.size(); j++) {
        i = max(i, m[s[j]]);
        m[s[j]] = j + 1;
        ans = max(ans, j - i + 1);
    }
    return ans;
}