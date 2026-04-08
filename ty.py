from multiprocessing.dummy import Array
from typing import List
import math



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
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for cs in s: c ^= ord(cs) #ord is ASCII value
        for ct in t: c ^= ord(ct)
        return chr(c) #chr = convert ASCII into character
        
    # 28. Find the Index of the First Occurrence in a String
    def strStr(self, haystack: str, needle: str) -> int:
        # letters = []
        # needle_count = 0
        # if len(needle)>len(haystack):
        #     return -1
        # for n in range(0, len(haystack), 1):
        #     letters.append(haystack[n]) 
        # for n in range(0, len(haystack), 1):
        #     if haystack[n] == needle[0]:
        #         for i in range(0, len(needle), 1):
        #             if n<=len(haystack)-len(needle):
        #                 if haystack[n+i] == needle[i]:
        #                     needle_count +=1
        #                 else:
        #                     needle_count = 0
        #                     break

        #         if needle_count == len(needle):
        #             return n
        # if needle_count == 0:
        #     return -1

        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1

        index = haystack.find(needle)

        return index

    # 242. Valid Anagram           
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False

        # count = [0]*26
        # for x in s:
        #     count[ord(x)-ord('a')] += 1
        # for x in t:
        #     count[ord(x)-ord('a')] -= 1
        # for val in count:
        #     if val != 0:
        #         return False
        # return True

        if len(s) != len(t):
            return False
        
        xor_sum = 0
        frequency = [0] * 26
        
        for i in range(len(s)):
            xor_sum ^= ord(s[i]) ^ ord(t[i]) # XOR both characters
            frequency[ord(s[i]) - ord('a')] += 1 # Increment for s
            frequency[ord(t[i]) - ord('a')] -= 1 # Decrement for t
        
        if xor_sum != 0: # If XOR isn't zero, they're not anagrams
            return False
        
        if any(freq != 0 for freq in frequency): # Check frequency counts
            return False
        
        return True

    # 459. Repeated Substring Pattern
    def repeatedSubstringPattern(self, s: str) -> bool:
        # check = 0
        # for x in s:
        #     check ^= ord(x)

        # if check != 0:
        #     return False
        
        return s in (s+s)[1:-1]
    
    # 283. Move Zeroes
    def moveZeroes(self, nums: List[int]) -> None:
        
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums
    
    # 66. Plus One
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        while digits[0] == 0 and len(digits) > 1:
            digits.pop(0)

        for i in range(len(digits)-1, -1, -1):
            if digits[i] + one == 10:
                digits[i] = 0
                one = 1
            else:
                digits[i] += 1
                one = 0
                break
        if one:
            digits.append(1)
            digits[0], digits[len(digits)-1] = digits[len(digits)-1], digits[0]
        return digits
    
    # 1822. Sign of the Product of an Array
    def arraySign(self, nums: List[int]) -> int:
        arr = []
        for x in nums:
            if not x:
                return 0
            elif x < 0:
                arr.append(-1)
        if len(arr) % 2:
            return -1
        else:
            return 1

    # 1502. Can Make Arithmetic Progression From Sequence
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        if len(arr)==2:
            return True
        for i in range (1, len(arr)-1):
            if not (arr[i] == (arr[i-1]+arr[i+1])/2):
                return False
            
        return True

        # length = len(arr)
        # min_val = min(arr)
        # max_val = max(arr)

        # diff = (max_val - min_val) / (length - 1)

        # for i in range(length):
        #     expected = min_val + i * diff
        #     if expected not in arr:
        #         return False

        # return True

        # 896. Monotonic Array
    
    def isMonotonic(self, nums: List[int]) -> bool:
        arr = []
        positive = False
        negative = False
        for i in range(len(nums)-1):
            arr.append(nums[i]-nums[i+1])
        for j in arr:
            if j == 0:
                continue
            elif j > 0:
                positive = True
            else:
                negative = True
        
        if negative and positive:
            return False
        else:
            return True

    # 342. Power of Four
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        b = math.log(n, 4)
        if math.trunc(b) != 0 and not (b % math.trunc(b)):
            return True
        else:
            return False

    # 58. Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        len = 0
        for x in reversed(s):
            if ord(x) == 32 and len == 0:
                continue
            if 97<=ord(x)<=122 or 65<=ord(x)<=90:
                len += 1
            else:
                return len
        return len

    # 88. Merge Sorted Array
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        if n == 0:
            return
        j = 0
        for i in range(len(nums1)):
            if nums1[i]>=nums2[j]:
                for x in range(m+j-1,i,-1):
                    nums1[x+1],nums1[x] = nums1[x],0
                nums1[i+1] = nums2[j]

                j+=1

                if nums1[i]> nums1[i+1]:
                    nums1[i+1], nums1[i] =  nums1[i], nums1[i+1]
            elif (nums1[i] == 0 and i > m+j-1) or (m == 0):
                nums1[i] = nums2[j]
                j+=1

            
            if j == n:
                return

    # 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums), nums


    # 26. Remove Duplicates from Sorted Array
    # 80. Remove Duplicates from Sorted Array II
    def removeDuplicates(self, nums: List[int]) -> int:
        # k, i, now = 1, 1, nums[0]
        # while i < len(nums):
        #     if nums[i] == now:
        #         nums.pop(i)
        #     else:
        #         k += 1
        #         now = nums[i]
        #         i += 1
        # return k

        # k, i, now = 1, 1, nums[0]
        # while i < len(nums):
        #     if nums[i] == now and k == 2:
        #         nums.pop(i)
        #     elif nums[i] != now:
        #         k = 1
        #         now = nums[i]
        #         i += 1
        #     else:
        #         k += 1
        #         i += 1
        # return i

        # k = 2

        # for i in range(2, len(nums)):
        #     if nums[i] != nums[k - 2]:
        #         nums[k] = nums[i]
        #         k += 1 

        # return k

        count = {}
        k = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] <= 2:
                nums[k] = num
                k += 1

        return k                   

    # 169. Majority Element
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] > len(nums) / 2:
                return x


    # 189. Rotate Array
    def rotate(self, nums: List[int], k: int) -> None:
        # k %= len(nums)
        # arr = []
        # j = 0
        # for i in range(0, len(nums)):
        #     if len(nums)-k-i>0:
        #         arr.append(nums[i])
        #     else:
        #         arr.insert(j,nums[i])
        #         j+=1
        # for i in range(0, len(nums)):
        #     nums[i] = arr[i]

        # k %= len(nums)
        # if k != 0:
        #     nums[:k] = nums[-k:]
        # return

        
        k %= len(nums)
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


    # 121. Best Time to Buy and Sell Stock
    # 122. Best Time to Buy and Sell Stock II
    def maxProfit(self, prices):
        # buy = prices[0]
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     elif prices[i] - buy > profit:
        #         profit = prices[i] - buy
        # return profit
            
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    
    # 55. Jump Game
    def canJump(self, nums):
        # jumps = [0] * len(nums)
        # jumps[-1] = 1
        j = len(nums) - 1
        for i in range (len(nums)-2, -1, -1):
            if nums[i] >= j - i:
                j = i
                # jumps[i] = 1
        if not j or len(nums) == 1:
            return True
        else: 
            return False

    # 45. Jump Game II
    def jump(self, nums):
        # j = len(nums) - 1
        # max_i = j
        # count = 0
        # while j > 0:
        #     for i in range (j-1, -1, -1):
        #         if nums[i] >= j - i:
        #             max_i = i
        #     j = max_i
        #     count += 1
        # return count
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        curr_end = 0   # end of current jump range
        max_reach = 0  # farthest index we can reach while scanning this range

        # We only need to process until n-2, because once we can reach last index,
        # we stop. No need to jump from the last index itself.
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            # Time to take one jump: we finished scanning current range.
            if i == curr_end:
                jumps += 1
                curr_end = max_reach

                # Optimization: if this jump can reach/past last index, done.
                if curr_end >= n - 1:
                    break

        return jumps        


    # 274. H-Index
    def hIndex(self, citations):
        # citations = sorted(citations, reverse=True)
        # i = 0
        # n = len(citations)
        # while i < n and citations[i] > i:
        #     i += 1
        # return i

        n = len(citations)
        count = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        
        return 0


        
def main():    
    solution = Solution()
    solution.hIndex(
[1,3,1]
      )

if __name__ == "__main__":
    main()