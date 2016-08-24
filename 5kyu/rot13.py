'''
Description:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
'''



##########MY SOLUTION##########
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    letterLstLower = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
    letterLstUpper = ["Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
    cipher = []
    for char in message:
        if char in letterLstLower:
            cipher.append(letterLstLower[(letterLstLower.index(char) + 13)%26])
        elif char in letterLstUpper:
            cipher.append(letterLstUpper[(letterLstUpper.index(char) + 13)%26])
        else:
            cipher.append(char)
    return "".join(cipher)