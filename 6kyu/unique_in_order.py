'''
Description:

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''


##########MY SOLUTION##########
def unique_in_order(iterable):
    newLst = list()
    try:
        newLst.append(iterable[0])
    except:
        return []
    num=0
    for x in iterable:
        if x == newLst[num]:
            continue
        else:
            newLst.append(x)
            num += 1
    return newLst