def chain_adder(num=0):
    acc = num

    def adder(val=None):
        nonlocal acc
        if val is not None:
            acc += val
            return adder

        return acc

    return adder


print(chain_adder(1)(2)())

print(chain_adder()())

print(chain_adder(2)(5)(1)(10)())
