import sys

n=19
DynamicArray= []

for i in range(n):
    Length= len(DynamicArray)
    Byte=sys.getsizeof(DynamicArray)
    print(f"Length = {Length} Byte = {Byte}")
    DynamicArray.append(n)




    """
    Optimization in List
    """