#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#

nme = 'vishwas'
nme1 = 'king'
print(nme[1])
print(nme[2:4])
print(nme[2:])
print(nme[:6])
print(nme1 + " " + nme[4:7])

k = ''
for i in range(len(nme)-1,-1,-1):
        k +=nme[i]

print(k)
print('-'*20)
print(nme*2)

