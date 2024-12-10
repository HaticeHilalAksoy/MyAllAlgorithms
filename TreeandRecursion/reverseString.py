"""
space O(1)

"""

s=["h","e","l","l","o"]
s[0] #'h'
s[len(s)-1] #'o'
def reverseRecursive(s,start:int,end:int):
    if start > end:
        return #son hai artık bu döndür demek.
    s[start], s[end] = s[end], s[start]
    reverseRecursive(s, start+1, end-1)
reverseRecursive(s, 0, len(s)-1)
print(s) #['o', 'l', 'l', 'e', 'h']


s= ["a","b","c","d","e"]
reverseRecursive(s, 0, len(s)-1)
print(s) #['e', 'd', 'c', 'b', 'a']