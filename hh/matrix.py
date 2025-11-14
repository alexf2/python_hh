def print_matrix(raw_data: str) -> str:
    data = [float(v) for v in raw_data.split(',')]
    if len(data) < 2:
        raise ValueError(
            f'Not enough arguments: {raw_data}. At least two numbers needed.')
    n_rows = int(data[0])
    n_cols = int(data[1])

    res = []
    for r in range(n_rows):
        row = []
        i = n_cols * r + 2
        for c in range(n_cols):
            row.append(f'{data[i + c]:10.3f}'.rstrip('0').rstrip('.'))
        res.append(row)

    return '\r\n'.join([' '.join(r) for r in res])


for m in [
    '2,4,1.1349,2.6876,3.99999,4.5678,5.8712,6.00001,7.19231,8.123012',
        '2,2,2,1.55555,1.66666,2']:
    print(print_matrix(m) + '\r\n')
