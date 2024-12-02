#sana verilen dizide sadece bir sayı tekrar etmiyor. o tekrar etmeyeni bul. içinde tek eleman da olabilir.

nums=[0]
#edge case:
def get_first_element(nums):
    # edge case:
    if len(nums) == 1:
        return nums[0]
print(get_first_element(nums))

# time: O(n) space: O(1) (listeden 1 kere geçmek demek)
#XOR mantığı 0 0 ->0 1 1->0 0 1 ->1 1 0->1
#bit manupilation 

def singleNums():
    mylist=[1,1,2,2,3,4,3]
    result=0
    for num in mylist:
        result= num ^ result
    return result
print(singleNums())
    
###
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result=num^result
        return result