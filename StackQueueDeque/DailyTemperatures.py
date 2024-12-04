#azalan stack O(N)O(N)
#lisre kullandık- bir önceki gün ile sıcakklık farkını yazıyoruz.

#ENUMERATE = [[73,0],[74,1],[75,2],[71,3],[69,4]] gibi hale getirir.
'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
"""_summary_


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # initialize with 0s so we don't have to manually add 0s if none is compliant later on
        myStack = [] #storing pair of temperature and corresponding index 
        
        for ix, temperature in enumerate(temperatures):
            while myStack and temperature > myStack[-1][0]:
                stackTemperature, stackIndex = myStack.pop()
                result[stackIndex] = (ix - stackIndex)
            myStack.append([temperature, ix])
        return result
                
"""
temperatures=[73,74,75,71,69,72,76,73]
def solution():
    result=[0]*len(temperatures)
    mystack=[]
    for ix, temperature in enumerate(temperatures):
        while mystack and temperature>=mystack[-1][0]:
            stackTemp, stackIndex= mystack.pop()
            result [stackIndex]=ix-stackIndex
        mystack.append([temperature,ix])
    return result
solution()
print(solution())