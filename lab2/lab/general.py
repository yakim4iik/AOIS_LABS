from lab.constants import *
from typing import Dict


def check_input(formula: str) -> bool:
    valid_characters = "abc+*-()"
    for i in formula:
        if valid_characters.find(i) == -1:
            return False
    if 'a' not in formula or 'b' not in formula or 'c' not in formula:
        return False
    else:
        return True


def create_sknf(table: Dict[int, list], variables: list) -> str:
    sknf = ''
    for i in range(len(table)):
        if table[i][LAST] == 0:
            sknf += '('
            for k in range(len(table[i]) - 1):
                if table[i][k] == 0:
                    sknf += f'{variables[k]}+'
                else:
                    sknf += f'(-{variables[k]})+'
            sknf = sknf[:LAST]
            sknf += ')*'
        else:
            continue
    if sknf[LAST] == '*':
        sknf = sknf[:LAST]
    return sknf


def create_sdnf(table: dict[int, list], variables: list) -> str:
    sdnf = ''
    for i in range(len(table)):
        if table[i][LAST] == 1:
            sdnf += '('
            for k in range(len(table[i]) - 1):
                if table[i][k] == 0:
                    sdnf += f'(-{variables[k]})*'
                else:
                    sdnf += f'{variables[k]}*'
            sdnf = sdnf[:LAST]
            sdnf += ')+'
        else:
            continue
    if sdnf[LAST] == '+':
        sdnf = sdnf[:LAST]
    return sdnf


def binary_num_sknf(table: dict[int, list], variables: list) -> str:
    bi_sknf = '*('
    for i in range(len(table)):
        if table[i][LAST] == 0:
            for k in range(len(variables)):
                bi_sknf += str(table[i][k])
            bi_sknf += ','
    if bi_sknf[LAST] == ',':
        bi_sknf = bi_sknf[:LAST] + ')'
    return bi_sknf


def decimal_num_sknf(table: dict[int, list], variables: list) -> str:
    de_sknf = '*('
    for i in range(len(table)):
        if table[i][LAST] == 0:
            interval = ''
            for k in range(len(variables)):
                interval += str(table[i][k])
            interval = conversion_ten(interval)
            de_sknf += interval
            de_sknf += ','
    if de_sknf[LAST] == ',':
        de_sknf = de_sknf[:LAST] + ')'
    return de_sknf


def binary_num_sdnf(table: dict[int, list], variables: list) -> str:
    bi_sdnf = '+('
    for i in range(len(table)):
        if table[i][LAST] == 1:
            for k in range(len(variables)):
                bi_sdnf += str(table[i][k])
            bi_sdnf += ','
    if bi_sdnf[LAST] == ',':
        bi_sdnf = bi_sdnf[:LAST] + ')'
    return bi_sdnf


def decimal_num_sdnf(table: dict[int, list], variables: list) -> str:
    de_sdnf = '+('
    for i in range(len(table)):
        if table[i][LAST] == 1:
            interval = ''
            for k in range(len(variables)):
                interval += str(table[i][k])
            interval = conversion_ten(interval)
            de_sdnf += interval
            de_sdnf += ','
    if de_sdnf[LAST] == ',':
        de_sdnf = de_sdnf[:LAST] + ')'
    return de_sdnf


def index(table: dict[int, list]):
    index = ''
    for i in range(len(table)):
        index += str(table[i][LAST])
    return conversion_ten(index)


def conversion_ten(x: str) -> str:
    total = 0
    step = 0
    for i in range(len(x) - 1, -1, -1):
        if x[i] == "1":
            total += pow(2, step)
        step += 1

    return str(total)
