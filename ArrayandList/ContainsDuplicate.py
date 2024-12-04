#listede tekrar eden değer varsa true yoksa false döndür.
#time O(N^2) space O(1)

List=[1,2,3,4,5]

for i in range (0,len(List)):
    for j in range(0,len(List)):
        print(i,j)

################################################################
#time O(Nlogn) space O(1)
#sort list yapacağız yani ilk dizip sonra kontrol edeceğiz.

List=[1,2,3,4,5]

################################################################
#time O(N) space O(n)
MyList=[1,2,3,4,5,6,5]
def solution():
    hashSet=set()
    for num in MyList:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False

print(solution())
################################################################
#time O(N) space O(n)
MyList2=[1,2,3,4,5,6,5]
def solution2():
    return len(MyList2) != len(set(MyList2))


print(solution2()) 