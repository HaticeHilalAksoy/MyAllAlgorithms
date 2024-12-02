#içinde 10 tane eleman varsa 5 tane aynı olan gibi düşün. içinde her zaman yüzde elliden fasla olan numarayı döndür.

# time o(n) space o(n)
# hashmap gibi düşün
mylist=[2,3,1,1,1,1,2,3,4,1,4,4,4,4,4,4,4,4,4,4]

def majelem():
    hashmap={} #sözlük
    result=0
    maxnum=0
    for num in mylist:
        hashmap[num]= 1+ hashmap.get(num, 0)
        if hashmap[num]>maxnum:
            result=num
        maxnum=max(maxnum, hashmap[num])
    return result
print(majelem()) 


# time O(n) space o(1)
#boyer Moore
list=[2,2,1,1,1,2,2]

def boyerMoore():
    result=0
    count=0
    for num in list:
        if count==0:
            result=num
        if num==result:
            count+=1
        else:
            count-=1
    return result

print(boyerMoore())

