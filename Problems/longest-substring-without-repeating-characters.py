class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_list = []
        max_length = 0
        for i in s:
            if i in check_list:
                check_list = check_list[check_list.index(i) + 1 :]
            check_list.append(i)
            max_length = max(max_length, len(check_list))
        return max_length
