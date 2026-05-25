class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(ch for ch in s if ch.isalnum()).lower()
        print(clean_s)
        print(clean_s[::-1])
        if clean_s == clean_s[::-1]:
            return True
        else:
            return False
        