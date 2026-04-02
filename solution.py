class Solution(object):
    # 1768. Merge Strings Alternately
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)
    
    # 389. Find the Difference
    # def findTheDifference(self, s: str, t: str) -> str:
    #     i = 0
    #     j = 0
    #     res = ''
    #     while (i<len(t)):
    #         for j in range(len(s)):
    #             if (t[i] == s[j]):
    #                 res = ''
    #             j += 1

    #     return res


def main():    
    solution = Solution()
    solution.mergeAlternately("adad", "lkjh")
    # solution.findTheDifference("abc", "abcd")
