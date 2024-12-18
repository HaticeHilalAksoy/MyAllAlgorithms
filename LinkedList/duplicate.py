#diziyi modify edersek x ve y pointerı koyarız sıralarız O(nlogn) de yaparız
#iki for lop a sokarsak O(N^2) de olur
# time O(N) SPACE O(1) de yapacağız
#floyd cycle detection algorithm

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Algorithm
        slowPointer = 0
        fastPointer = 0
        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            if slowPointer == fastPointer:
                break
        
        secondSlowPointer = 0
        
        while True:
            slowPointer = nums[slowPointer]
            secondSlowPointer = nums[secondSlowPointer]
            if slowPointer == secondSlowPointer:
                return slowPointer
        
        
        '''
        O(n^2)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]
        '''