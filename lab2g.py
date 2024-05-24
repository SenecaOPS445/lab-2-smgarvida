#!/usr/bin/env python3

#Author: Shayna Mae Garvida
#Author ID: smgarvida
#Date Created: 2024/05/24

import sys


if len(sys.argv) != 2:
    timer = 3    

else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
