'''
Description:

Here you will create the classic pascal's triangle. Your function will be passed the depth of the triangle and you code has to return the corresponding pascal triangle upto that depth

The triangle should be returned as a nested array.

for example:

pascal(5) # should return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together (except for the edges, which are all "1"). eg

          [1]
        [1   1]
       [1  2  1]
      [1  3  3  1]
here you get the 3 by adding the 2 and 1 above it.
'''



##########MY SOLUTION##########
def pascal(p):
    currentArray = [[1]]
    while p > 1:
        nextLevel = [1]
        for index in range(0,len(currentArray[-1])-1):
            nextLevel.append(currentArray[-1][index] + currentArray[-1][index+1])
        nextLevel.append(1)
        currentArray.append(nextLevel)
        p -= 1
    return currentArray