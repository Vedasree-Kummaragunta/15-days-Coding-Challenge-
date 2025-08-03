class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric chars, convert to lowercase
        cleaned = ''.join(map(str.lower, filter(str.isalnum, s)))
        return cleaned == cleaned[::-1]


if __name__ == "__main__":
    s = input("Enter a sentence: ")
    sol = Solution()
    print("Palindrome?" , sol.isPalindrome(s))
