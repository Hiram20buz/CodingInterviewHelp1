# How to calculate the number of numerical digits in a string?

import re

p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'

#s = 'he33llo 42 I\'m a 32 string 30 444.4 12,001'

s="TESTu45"

if re.search(p, s) is not None:
    for catch in re.finditer(p, s):
        print(catch[0]) # catch is a match object
