class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        have = {}
        left = 0
        formed = 0
        required = len(need)

        min_length = float("inf")
        answer = ""

        for right in range(len(s)):
            char = s[right]

            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    answer = s[left:right + 1]

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return answer