import timeit

code_set1 = ('a', 'i', 'b', 'f', 'p')
code_set2 = ('e', 'o', 't', 'g', 'm')
changes = [('a', 'e'), ('i', 'o'), ('b', 't'), ('f', 'g'), ('p', 'm')]


def encode(string: str):
    new_string = ''
    for c in string:
        if c in code_set1:
            new_string += code_set2[code_set1.index(c)]
        elif c in code_set2:
            new_string += code_set1[code_set2.index(c)]
        else:
            new_string += c
    # rint(new_string)
    return new_string


def encode2(string: str):
    # print(string.replace(code_set1, code_set2))

    for old, new in changes:
        if old in string:
            string = string.replace(old, new)
        elif new in string:
            string = string.replace(new, old)

    # print(string)
    return string


def encode3(string: str):
    new_string = ''.join(
        map(
            lambda x: code_set2[code_set1.index(x)] if x in code_set1 else (
                code_set1[code_set2.index(x)] if x in code_set2 else x), string
        ))

    # print(new_string)
    return new_string


if __name__ == '__main__':
    encode('bueno')
    encode2('bueno')
    encode3('bueno')
    encode('tuani')
    encode2('tuani')
    encode3('tuani')
    print(timeit.timeit("encode('bueno')", number=1000000, setup="from __main__ import encode"))
    print(timeit.timeit("encode2('bueno')", number=1000000, setup="from __main__ import encode2"))
    print(timeit.timeit("encode3('bueno')", number=1000000, setup="from __main__ import encode3"))
