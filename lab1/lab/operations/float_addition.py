from lab.operations.addition import *
from lab.to_binary import *

'''
    print(result[0] + ',' + zero * '0' + index1 + ',' + mantissa + zero2 * '0')
'''


def float_to_bi(num: str) -> tuple:
    integer, float1 = num.split('.')
    dr = abs(float(num) - int(integer))
    dr2 = ''
    integer = straight_code(int(integer))
    integer = integer[integer.find('1') - 1:]
    i = -1
    while dr > 0:
        if dr - pow(2, i) >= 0:
            dr2 += '1'
            dr -= pow(2, i)
        else:
            dr2 += '0'
        i -= 1

    return integer, dr2


def float_addition() -> str:
    num1, num2 = a, b = '4.75', '5.5'
    num1_int, num1_fl = float_to_bi(num1)
    num2_int, num2_fl = float_to_bi(num2)
    max_fl, max_int = max(len(num1_fl), len(num2_fl)), max(len(num1_int), len(num2_int))
    num1_fl, num2_fl = num1_fl + (max_fl - len(num1_fl)) * '0', num2_fl + (max_fl - len(num2_fl)) * '0'
    num1_int, num2_int = (max_int - len(num1_int)) * '0' + num1_int, (max_int - len(num2_int)) * '0' + num2_int
    num1, num2 = num1_int + num1_fl, num2_int + num2_fl
    result = addition_additional(additional_code(conversion_ten(num1)), additional_code(conversion_ten(num2)))
    answer = ''.join(result[:-max_fl]) + ',' + ''.join(result[-max_fl:])
    index = conversion(max_fl)
    if float(num1) + float(num2) > 0:
        print(f'{result[0]}.{result[result.find("1", 1):]}*2^1.{index[index.find("1"):]}')
        return f'{a} + {b} = {bi_to_float(answer)} = {answer[0]}.{answer[answer.find("1", 1):]}'
    else:
        print(f'{result[0]}.{result[result.find("1", 1):]}*2^1.{index[index.find("1"):]}')
        return f'{a} + {b} = {bi_to_float(answer)} = {answer[0]}.{answer[answer.find("1", 1):]}'


def bi_to_float(num: str) -> float:
    integer, float1 = num.split(',')
    integer = conversion_ten(integer)
    total = integer
    k = -1
    for i in range(0, len(float1)):
        if float1[i] == "1":
            total += pow(2, k)
        k -= 1
    return total
