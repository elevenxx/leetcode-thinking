class Solution:
    def longestPalindrome(s):
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            # if there is no chance to find longer palindrome
            # when i goes near the end of string s
            if 2 * (n - i) + 1 < right - left + 1:
                break

            # l, i as center first, recursive to find longest palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            # if find longer palindrome, then update answer
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return right - left + 1


n = int(input())
s = input()
ans = Solution.longestPalindrome(s)
print(ans)
