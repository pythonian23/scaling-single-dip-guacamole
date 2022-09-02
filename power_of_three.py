# 5 different ways of getting powers of 3

import math


def rpo3(n):
    if n == 0:
        return 1
    else:
        return 3 * rpo3(n - 1)


def mpo3(n):
    return 3**n


def epo3(n):
    return eval("*".join(["3"] * n))


def lpo3(n):
    k = 1
    for k in range(n):
        k *= 3
    return k


def xpo3(n):
    return math.exp(math.log(3) * n)


for po3 in [rpo3, mpo3, epo3, lpo3, xpo3]:
    print(po3.__name__)
    print(po3(3))
    print(po3(5))
    print()
