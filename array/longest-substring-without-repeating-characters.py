"""
input: a string s
output: the length of the longest substring without repeating characters

sliding window tech and a dictionary

using a dic to store the mapping from char to its position in s
using j pointer to expand the window size
if current char exists in the window and in the dic, then shrink the window size
"""


def lengthOfSubstring(s):
    i, j, n = 0, 0, len(s)
    seen, ans = {}, 0
    while j < n:
        if s[j] in seen and seen[s[j]] >= i:
            i = seen[s[j]] + 1
        seen[s[j]] = j
        ans = max(ans, j-i+1)
        j += 1
    return ans


if __name__ == "__main__":
    s = input()
    ans = lengthOfSubstring(s)
    print(ans)