def splitListByEvenOdd(list):
    EvenList = []
    OddList = []
    EvenOddList = []
    for i in list :
        if(i % 2 == 0):
            EvenList.append(i)
        else:
            OddList.append(i)
    EvenOddList.append(EvenList)
    EvenOddList.append(OddList)
    return EvenOddList

def splitListByEvenOdd2():
    OddList = []
    EvenOddList = []
    i = 0
    while i < len(mixedlist):
        if(mixedlist[i] % 2 != 0):
            OddList.append(mixedlist[i])
            mixedlist.remove(mixedlist[i])
        else: 
        	i += 1;
    EvenOddList.append(mixedlist)
    EvenOddList.append(OddList)
    return EvenOddList

mixedlist = [1,5,2,9,62,13] 
print(splitListByEvenOdd(mixedlist))
print(splitListByEvenOdd2())
