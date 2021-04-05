import timeit


def gen_order():
    cell = 15
    count = 4
    gen = '\n'.join([''.join([gen for gen in ('*' for n in range(count))]) for s in range(cell // count)]) + \
          '\n' + ''.join([gen for gen in ('*' for n in range(cell % count))])

    #print(gen)
    return gen


def iter_order():
    cell = 15
    count = 4
    line = cell // count
    ost = cell % count

    res = ''
    for n in range(line):
        local = ''
        for n in range(count):
            local += '*'
        res += local + '\n'

    local = ''
    for n in range(ost):
        local += '*'
    res += local

    #print(res)
    return res


if __name__ == '__main__':
    print(timeit.timeit("gen_order()", setup="from __main__ import gen_order", number=10000))
    print(timeit.timeit("iter_order()", setup="from __main__ import iter_order", number=10000))
