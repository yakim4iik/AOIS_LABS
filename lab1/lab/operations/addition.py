from typing import List
from lab.constants import *


def addition_straight(a: str, b: str) -> str:
    lst1, lst2 = list(a), list(b)
    result = interval(lst1, lst2)
    return "".join(result)


def addition_reverse(a: str, b: str) -> str:
    lst1, lst2 = list(a), list(b)
    result1 = interval(lst1, lst2)
    total = result1
    if len(result1) > 16:
        total.pop(0)
        total = interval(result1, ONE)
    if total[0] == "1":
        for i in range(1, len(total)):
            if total[i] == "0":
                total[i] = "1"
            else:
                total[i] = "0"
    return "".join(total)


def addition_additional(a: str, b: str) -> str:
    lst1, lst2 = list(a), list(b)
    result1 = interval(lst1, lst2)
    if len(result1) > 16:
        result1.pop(0)
    if result1[0] == "1":
        for i in range(1, len(result1)):
            if result1[i] == "0":
                result1[i] = "1"
            else:
                result1[i] = "0"
        for i in range(len(result1) - 1, -1, -1):
            if result1[i] == "0":
                result1[i] = "1"
                break
            if result1[i] == "1":
                result1[i] = "0"
    return "".join(result1)


def interval(lst1: List[str], lst2: List[str]) -> List[str]:
    lst3 = list()
    count = 0
    for i in range(len(lst1) - 1, -1, -1):
        if int(lst1[i]) + int(lst2[i]) + count == 3:
            lst3.insert(0, "1")
            count = 1
        elif int(lst1[i]) + int(lst2[i]) + count == 2:
            lst3.insert(0, "0")
            count = 1
        elif int(lst1[i]) + int(lst2[i]) + count == 1:
            lst3.insert(0, "1")
            count = 0
        else:
            lst3.insert(0, "0")
            count = 0
    if count == 1:
        lst3.insert(0, "1")
    return lst3
