

def conversion(number: int) -> str:
    result = ""
    number = abs(number)
    while number > 0:
        y = str(number % 2)
        result = y + result
        number = int(number / 2)

    add = 15 - len(result)
    result = add * "0" + result

    return result


def conversion_ten(x: str) -> int:
    total = 0
    step = 0
    for i in range(len(x) - 1, 0, -1):
        if x[i] == "1":
            total += pow(2, step)
        step += 1
    if x[0] == "0":
        return total
    else:
        return int("-" + str(total))


def straight_code(x: int) -> str:
    result = conversion(x)
    if x > 0:
        result = "0" + result
    if x < 0:
        result = "1" + result

    return result


def reverse_code(x: int) -> str:
    result = conversion(x)
    if x > 0:
        result = "0" + result
    if x < 0:
        lst = list(result)
        for i in range(0, len(lst)):
            if lst[i] == "0":
                lst[i] = "1"
            else:
                lst[i] = "0"
        result = "1" + "".join(lst)

    return result


def additional_code(x: int) -> str:
    result = conversion(x)
    if x == 0:
        result = "0" * 16
    elif x >= 0:
        result = "0" + result
    if x < 0:
        result = reverse_code(x)
        lst = list(result)
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == "0":
                lst[i] = "1"
                break
            if lst[i] == "1":
                lst[i] = "0"
        result = "".join(lst)

    return result
