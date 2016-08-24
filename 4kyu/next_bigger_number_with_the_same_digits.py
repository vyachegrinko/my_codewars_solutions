'''
Description:

You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
'''



##########MY SOLUTION##########
def next_bigger(n):
    numberLst = [int(i) for i in str(n)]
    numBreakerIndex = 0
    for i in range(1, len(numberLst)+1):
        if numBreakerIndex <= numberLst[-i]:
            numBreakerIndex = numberLst[-i]
        else:
            numBreakerIndex = len(numberLst)-i
            finalLst = [numberLst[x] for x in range(numBreakerIndex)]
            endOfLst = [numberLst[x] for x in range(numBreakerIndex,len(numberLst))]
            nextNum = 10
            nextNumIndex = 1
            for x in range(1,len(endOfLst)):
                if endOfLst[0] < endOfLst[x] and endOfLst[x] < nextNum:
                    nextNum = endOfLst[x]
                    nextNumIndex = x
            finalLst.append(endOfLst[nextNumIndex])
            print "endOfLst", endOfLst
            endOfLst.pop(nextNumIndex)
            print "endOfLst", endOfLst
            endOfLst.sort()
            print "endOfLst", endOfLst
            for blah in endOfLst:
                finalLst.append(blah)
            print "numBreakerIndex:", numBreakerIndex
            print "nextNum:", nextNum
            return int("".join([str(i) for i in finalLst]))
    return -1