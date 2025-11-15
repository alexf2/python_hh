import re
from typing import Literal

expr_with_simple_math = re.compile(
    r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)')

Operation = Literal['+', '-', '*', '/']
resolvers = {
    '+': lambda v1, v2: v1 + v2,
    '-': lambda v1, v2: v1 - v2,
    '*': lambda v1, v2: v1 * v2,
    '/': lambda v1, v2: v1 / v2
}


def format_num(val: float) -> str:
    return f'{val:.2f}'


def eval_operation(val1: float, op: str, val2: float) -> float:
    if op not in resolvers:
        raise ValueError(f'Unsupported operation {op}')
    return resolvers[op](val1, val2)


def cal_math(str: str) -> str:
    return expr_with_simple_math.sub(
        lambda m: format_num(
            eval_operation(
                float(m.group(1)),
                m.group(2),
                float(m.group(3)))),
        str)


for val in [
    '10+0.01 равно 10.01, 0.127 округляется до 0.13',
    '10.4/2 0.13-2',
        'Текст без выражений',
        '201  - 2 и 10.77 + 0.234']:
    print(val, ':  ', cal_math(val))
