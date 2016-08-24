'''
Description:

Write a function called validParentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.

Examples: 
validParentheses( "()" ) => returns true 
validParentheses( ")(()))" ) => returns false 
validParentheses( "(" ) => returns false 
validParentheses( "(())((()())())" ) => returns true 

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'
'''



##########MY SOLUTION##########
def valid_parentheses(string):
    right=0
    left=0
    for i in string:
        if i =='(':
            right +=1
            continue
        elif i == ')':
            left +=1
            if right-left<0:
                return False
            continue
        else:
            continue
    if right-left ==0:
        return True
    else:
        return False