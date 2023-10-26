#!/bin/python3

import math
import os
import random
import re
import sys


def binaryConvert(n):
    binaryList = []
    while n > 0:
        i = n
        i = i % 2
        binaryList.insert(0, i)
        n = math.floor(n/2)

    pos = 0
    sequence = 1
    higherSequence = 1
    listLenght = int(len(binaryList))

    while pos < listLenght:
        try:
            if binaryList[pos] == binaryList[pos + 1]:
                sequence += 1
                if sequence > higherSequence:
                    higherSequence = sequence
            elif binaryList[pos] != binaryList[pos + 1]:
                sequence = 1

        except IndexError:
            pass
        pos += 1

    print(higherSequence)

if __name__ == '__main__':
    n = int(input().strip())
    binaryConvert(n)