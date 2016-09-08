'''
Description:

John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and the address.

Unfortunately everything is mixed, things are not always in the same order, lines are cluttered with non-alpha-numeric characters.

Examples of John's phone book lines:

"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"

" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"

Could you help John with a program that, given the lines of his phone book and a phone number returns a string for this number : "Phone => num, Name => name, Address => adress"

Examples:

s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
It can happen that, for a few phone numbers, there are many people for a phone number -say nb- , then

return : "Error => Too many people: nb"

or it can happen that the number nb is not in the phone book, in that case

return: "Error => Not found: nb"

You can see other examples in the test cases.'''



##########MY SOLUTION##########
import re

def phone(strng, num):
    count = 0
    for line in strng.split('\n'):
        if num in line:
            count += 1
            phone = "Phone => {}, ".format(num)
            name = "Name => {}, ".format(re.findall('<(.*)>',line)[0])
            address = re.sub('<.*>','',line)
            address = "Address => {}".format(re.sub('\+' + num,'',address).strip())
            address = re.sub(' *[;/*$:!,?] *',' ',address)
            address = re.sub('_',' ',address.strip())
            address = re.sub('  ',' ',address)
            entry = phone+name+address
    if count == 0: return 'Error => Not found: {}'.format(num)
    elif count == 1: return entry
    else: return 'Error => Too many people: {}'.format(num)
