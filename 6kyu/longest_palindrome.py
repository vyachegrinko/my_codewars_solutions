'''
Description:

Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
'''


##########MY SOLUTION##########
def longest_palindrome (s):
    startChopLst = list(s)
    longestPalindrome = 0
    while startChopLst != []:
        endChopLst = list(startChopLst)
        while endChopLst != []:
            if endChopLst == list(reversed(endChopLst)):
                if len(endChopLst) > longestPalindrome:
                    longestPalindrome = len(endChopLst)
            endChopLst.pop()
        startChopLst.pop(0)
    return longestPalindrome