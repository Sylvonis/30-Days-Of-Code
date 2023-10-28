#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    highervalue = None
    colCount = 0
    rowCount = 0

    while True:
        if colCount == 4:
            rowCount += 1
            colCount = 0
        if rowCount == 4:
            break

        collumTaker = ( arr[0 + colCount][0 + rowCount] +
                        arr[0 + colCount][1 + rowCount] +
                        arr[0 + colCount][2 + rowCount] +

                        arr[1 + colCount][1 + rowCount] +

                        arr[2 + colCount][0 + rowCount] +
                        arr[2 + colCount][1 + rowCount] +
                        arr[2 + colCount][2 + rowCount])

        if highervalue is None:
            highervalue = collumTaker

        elif collumTaker > highervalue:
            highervalue = collumTaker

        colCount += 1

    print(highervalue)

