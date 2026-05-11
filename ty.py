from multiprocessing.dummy import Array
from random import choice
from typing import List, Optional
import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    # 238. Product of Array Except Self
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        right, left = 1, 1
        for i in range (n):
            answer[i] *= left
            left *= nums[i]
             
        for i in range (n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
    
    # 134. Gas Station
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        
        if sum(gas) >= sum(cost):
            current_gas = 0
            start = 0
                
            for i in range (n):
                current_gas += gas[i] - cost[i]
                if current_gas < 0:
                    current_gas = 0
                    start = i + 1
            return start
        else: return -1
         

    # 135. Candy  
    def candy(self, ratings):
        n =  len(ratings)
        candies = [1] * n
        for i in range (1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range (n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i],candies[i+1]+1)

        return sum(candies)

    # 42. Trapping Rain Water
    def trap(self, height):
        '''n = len(height)
        max_local = []
        # min_local = []
        sign = '+'
        answer = 0

        for i in range (1, n):
            if height[i] > height[i-1] and sign == '-':
                # min_local.append(i-1)
                sign = '+'
            elif height[i] < height[i-1] and sign == '+':
                max_local.append(i-1)
                sign = '-'
        if sign == '+':
            max_local.append(n-1)
        # else:
        #     min_local.append(n-1)
        
        it = 1
        while it != len(max_local)-1:
            if height[max_local[it-1]] > height[max_local[it]] < height[max_local[it+1]]:
                max_local.pop(it)
                
            else : it += 1

        for x in range (len(max_local)-1):
            l = max_local[x]
            r = max_local[x+1]

            subtrahend = height[l:r+1]

            minimum = min(height[l], height[r])
            for i in range (len(subtrahend)):
                if subtrahend[i] > minimum:
                    subtrahend[i] = minimum
            
            minuend = [subtrahend[0]] * (r - l + 1)
            
            difference = [a - b for a, b in zip(minuend, subtrahend)]
            answer += sum(difference)

            
        return answer '''
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        answer = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                answer += left_max - height[l]   
            else:
                r -= 1
                right_max = max(right_max, height[r])
                answer += right_max - height[r]
        return answer



    # two pointers special

    # 5. Longest Palindromic Substring
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        def expand_from_center(s: str, left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1


        start, end = 0, 0
        n = len(s)
        
        for i in range (n):
            odd = expand_from_center(s, i, i)
            even = expand_from_center(s, i, i+1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
            
        return s[start:end+1]

    # 11. Container With Most Water
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = min(height[left], height[right]) * (right - left)
        left_max = height[left]
        right_max = height[right]
        max_water = water
        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])

            water = min(height[left], height[right]) * (right - left)
            if water > max_water:
                max_water = water

        
        return max_water

    # 15. 3Sum
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # def sorting_array(nums: list[int]) -> list[list[int]]:
        # indices = {}
        # for i in range (len(nums)):


        nums.sort()

        triplets = []
        
        for left in range (len(nums)):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            middle = left+1
            right = len(nums)-1
            while middle < right:
                summ = nums[left] + nums[middle] + nums[right] 
                if summ < 0:
                    middle += 1
                elif summ > 0: 
                    right -= 1
                elif summ == 0:
                    triplets.append([nums[left], nums[middle], nums[right]] )
                    middle += 1
                    while nums[middle] == nums[middle-1] and middle < right:
                        middle += 1

            

        return triplets
    
    # 16. 3Sum Closest
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        difference = []
        for left in range (len(nums)-1):
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                summ = nums[left] + nums[middle] + nums[right]
                if (len(difference) > 0 and abs(summ - target) < difference[-1]) or len(difference) == 0:
                    difference.append(abs(summ - target))
                    answer = summ

                if summ < target:
                    middle += 1
                elif summ > target: 
                    right -= 1
                else:
                    return answer
        return answer

    # 18. 4Sum
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        quadruplets = []
        
        for a in range (len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range (a+1, len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c = b+1
                d = len(nums)-1
                while c < d:
                    summ = nums[a] + nums[c] + nums[d] + nums[b]

                    if summ == target:
                        quadruplets.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                    elif summ < target:
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                    elif summ > target: 
                        d -= 1
                        while nums[d] == nums[d+1] and c < d:
                            d -= 1

            

        return quadruplets

    # 19. Remove Nth Node From End of List
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast, slow = head, head

        for i in range (n):
            fast = fast.next
        if not fast: return head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
            
    # 31. Next Permutation
    def nextPermutation(self, nums):
        n = len(nums)
        arr = []
        k, l = None, None
        for i in range (n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break
        if k is None:
            nums.sort()
        else:
            for j in range (n-1, -1, -1):
                if nums[j] > nums[k]:
                    l = j
                    break
            nums[k], nums[l] = nums[l], nums[k]
            arr = nums[k+1:n]
            arr.reverse()
            nums[k+1:] = arr
        
    # 61. Rotate List
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        tail.next = head
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

    # 75. Sort Colors
    def sortColors(self, nums):
        zeros, twos = 0, len(nums)-1
        p = 0
        while p <= twos:
            if nums[p] == 0:
                nums[zeros], nums[p] = nums[p], nums[zeros]
                zeros += 1
            if nums[p] == 2:
                nums[twos], nums[p] = nums[p], nums[twos]
                twos -= 1
            else: p += 1
        


'''# 380. Insert Delete GetRandom O(1) 
class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val):
        if val not in self.indices:
            self.indices[val] = len(self.nums)
            self.nums.append(val)

            return True
        else:
            return False
        

    def remove(self, val):
        if val in self.indices:
            i = self.indices[val]
            last = self.nums[-1]
            self.nums[i] = last
            self.indices[last] = i
            self.nums.pop() 
            del self.indices[val]            

            return True
        else:
            return False


    def getRandom(self):
        return choice(self.nums)
        '''

def build_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

        
def main():    
    solution = Solution()
    # head = build_linked_list([1,2,3,4,5])
    solution.sortColors(
[2,2,2,1,1,0,0,1,0,1,0,2,1,0,2,1,0,2,1,1]



    )


if __name__ == "__main__":
    main()