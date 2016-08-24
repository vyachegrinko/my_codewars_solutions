'''
Description:

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''



##########MY SOLUTION##########
import re
def pig_it(text):
    words=text.split()
    for i in range(len(words)):
        if '?' in words[i] or '!' in words[i]:
            continue
        words[i]=words[i][1:]+words[i][0]+"ay"
    return " ".join(words)