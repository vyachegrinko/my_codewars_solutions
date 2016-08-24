'''
Description:

The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("
'''


##########MY SOLUTION##########
def duplicate_encode(word):
    wordDict = {}
    blah = word.lower()
    for letter in blah:
        wordDict[letter] = wordDict.get(letter,0) + 1
    multiplesLst = []
    for k,v in wordDict.items():
        if v > 1:
            multiplesLst.append(k)
    finalString = ""
    for letter in blah:
        if letter in multiplesLst:
            finalString += ")"
        else:
            finalString += "("
    return finalString