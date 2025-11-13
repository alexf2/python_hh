from collections import defaultdict
from typing import Tuple


def count_freq(str: str) -> list[Tuple[str, int]]:
    dic = defaultdict(int)
    for ch in str:
        count = dic.setdefault(ch, 0)
        dic[ch] = count + 1

    return sorted(dic.items(), key=lambda val: -val[1])


for data in ['aab', 'abcghjtgkabbbbde', 'abca', 'vbvvty']:
    print(data, ':  ', count_freq(data))
