def longestPalindrome(s):
    left = right = 0
    n = len(s)
    for i in range(n - 1):
        # if there is no chance to find longer palindrome
        # when i goes near the end of string s
        if 2 * (n - i) + 1 < right - left + 1:
            break

        # one char as center
        # l, i as center first, recursive to find longest palindrome
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1

        # if find longer palindrome, then update answer
        if r - l - 2 > right - left:
            left = l + 1
            right = r - 1

        # two chars as center
        l = i
        r = i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if r - l - 2 > right - left:
            left = l + 1
            right = r - 1

    return right - left + 1


n = int(input())
s = input()
ans = longestPalindrome(s)
print(ans)

"""
manacher
def manacher(s):
    s = "#" + "#".join(s) + "#"
    RL = [0] * len(s)
    MaxRight = 0
    pos = 0
    MaxLen = 0
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2 * pos - i], MaxRight - i)
        else:
            RL[i] = 1
        while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
            RL[i] += 1
        if RL[i] + i - 1 > MaxRight:
            MaxRight = RL[i] + i - 1
            pos = i
        MaxLen = max(MaxLen, RL[i])
    return MaxLen - 1


n = int(input())
s = input()
ans = manacher(s)
print(ans)
"""