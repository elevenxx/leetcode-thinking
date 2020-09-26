#include <iostream>
#include <string>
using namespace std;


void centerDisperse(const string &s, int left, int right, int& start, int& maxlen);
int longestPalindrome(string s);

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int ans;
    ans = longestPalindrome(s);
    cout << ans << endl;
    return 0;
}


void centerDisperse(const string &s, int left, int right, int& start, int& maxlen) {
    while(left >= 0 && right < s.size() && s[left] == s[right]) {
        left--;
        right++;
    }
    if (right - left - 1 > maxlen) {
        start = left + 1;
        maxlen = right - left - 1;
    }
}

int longestPalindrome(string s) {
    int start = 0, maxlen = 0;
    for (int i=0; i<s.size(); i++) {
        centerDisperse(s, i, i, start, maxlen);
        centerDisperse(s, i, i+1, start, maxlen);
    }
    return maxlen;
}