from lab.to_binary import *
from lab.operations.addition import *
from lab.constants import *


def multiplication(mult1: str, mult2: str) -> list[str]:

    result = ZERO
    flag = mult1[0] == mult2[0]
    if mult2[0] == '1':
        mult2 = '0' + mult2[1:]
    while mult2 != ''.join(ZERO):
        result = addition_additional(additional_code(conversion_ten(mult1)), additional_code(conversion_ten("".join(result))))
        mult2 = addition_additional(additional_code(conversion_ten(mult2)), ''.join(ONE_ADDITION))
    if flag:
        result = '0' + result[1:]
    else:
        result = '1' + result[1:]
    return result
