import re


class BoolVar:
    def __init__(self, value):
        self.value = value
        # print("INIT =", value)

    # '-'
    def __neg__(self):
        return BoolVar(not self.value)

    # '+'
    def __add__(self, other):
        return BoolVar(self.value or other.value)

    # '*'
    def __mul__(self, other):
        return BoolVar(self.value and other.value)

    # строка
    def __str__(self):
        return "True" if self.value else "False"


def table_true(formula):
    variables = sorted(set(re.findall(r"[A-Za-z]", formula)))
    decor(variables)
    table = {}
    for i in range(pow(2, len(variables))):
        table[i] = list()
    values_for_eval = {}
    for row in range(pow(2, len(variables))):
        for i, key in reversed(list(enumerate(reversed(variables)))):
            values_for_eval[key] = BoolVar(row & (1 << i))
            check = BoolVar.__str__(values_for_eval[key])
            if check == "True":
                print(f"  1  ", end="|")
                table[row].append(1)
            else:
                print(f"  0  ", end="|")
                table[row].append(0)
        result = eval(formula, {}, values_for_eval)
        check_result = BoolVar.__str__(result)
        if check_result == "True":
            print(f" 1")
            table[row].append(1)
        else:
            print(f" 0")
            table[row].append(0)
    return table, variables


def decor(variables):
    header = [""] * 2
    for key in variables:
        header[0] += "-" * 5 + "+"
        header[1] += f"  {key}  |"
    header[0] += "-" * 7
    header[1] += "Result"
    print("\n".join(header + header[0:1]))
