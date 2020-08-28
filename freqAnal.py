#!usr/bin/python3
from collections import Counter
#open txt doc with encrypted text
file = open('/home/zero/Documents/SecureSet/systemSec/Python/crypto/crypto100/CRY100_01_Lab_Substitution.txt', "r").read()

splitText = []
raw = ''

for i in file:
    if i != ' ':
        splitText.append(i)
        raw += i
    else:
        pass

result = Counter(splitText)


print(result)
print(raw)