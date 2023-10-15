import sys

numOftestCases = sys.stdin.readline()
counter = int(numOftestCases)


while counter > 0:
    testCase = sys.stdin.readline()
    pos = 0
    t = ''
    u = ''

    if counter > 1:
        testCaseLen = len(testCase) - 1
    else:
        testCaseLen = len(testCase)

    while testCaseLen > 0:
        if pos %2 == 0:
            t += testCase[pos]
        elif pos %2 == 1:
            u += testCase[pos]
        pos += 1
        testCaseLen -= 1

    print(t + ' ' + u)
    counter -= 1
    t = None
    u = None
