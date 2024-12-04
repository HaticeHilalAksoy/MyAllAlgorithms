#stack ile yapacağız.
#stack ile yapılan her şey liste ile de yapılabilir.
# C,D,+ ve int değerler olacak.
# int görünce push et stack e, c görünce pop et

myInput=["5","2","C","D","+"]

def Solution():
    myStack=[]
    for char in myInput:
        if char=="C":
            myStack.pop()
        elif char=="+":
            myStack.append(myStack[-1]+ myStack[-2])
        elif char=="D":
            myStack.append(myStack[-1]*2)
        else:
            myStack.append(int(char)) #char string veriliyor int o yuzden çevir
    return sum(myStack)
print(Solution()) 

