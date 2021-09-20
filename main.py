import timeit

code_set1 = ('a', 'i', 'b', 'f', 'p')
code_set2 = ('e', 'o', 't', 'g', 'm')
code = list(zip(code_set1, code_set2))
code2 = list(zip(code_set1, code_set2)) + list(zip(code_set2, code_set1))
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
    return new_string


def encode2(string: str):
    # print(string.replace(code_set1, code_set2))
    for code_right, code_left in changes:
        if code_right in string:
            string = string.replace(code_right, code_left)
        elif code_left in string:
            string = string.replace(code_left, code_right)
    # print(string)
    return string


def encode3(string: str):
    return ''.join(
        map(lambda x: code_set2[code_set1.index(x)] if x in code_set1 else (
            code_set1[code_set2.index(x)] if x in code_set2 else x),
            string)
    )


def encode4(string: str):
    for r in code2:
        string = string.replace(*r)
    return string


code3 = {'a': 'e', 'i': 'o', 'b': 't', 'f': 'g', 'p': 'm', 'e': 'a', 'o': 'i', 't': 'b', 'g': 'f', 'm': 'p'}


def encode5(string: str):
    return ''.join(
        map(lambda x: code3[x] if x in code3 else x,
            string)
    )


def encode6(string: str):
    return ''.join(code3[x] if x in code3 else x for x in string)


if __name__ == '__main__':
    print(f"{encode('bueno')=}")
    print(f"{encode2('bueno')=}")
    print(f"{encode3('bueno')=}")
    print(f"{encode4('bueno')=}")
    print(f"{encode5('bueno')=}")
    print(f"{encode6('bueno')=}")
    print(f"{encode('tuani')=}")
    print(f"{encode2('tuani')=}")
    print(f"{encode3('tuani')=}")
    print(f"{encode4('tuani')=}")
    print(f"{encode5('tuani')=}")
    print(f"{encode6('tuani')=}")
    print(timeit.timeit("encode('bueno')", number=1000000, setup="from __main__ import encode"))
    print(timeit.timeit("encode2('bueno')", number=1000000, setup="from __main__ import encode2"))
    print(timeit.timeit("encode3('bueno')", number=1000000, setup="from __main__ import encode3"))
    print(timeit.timeit("encode4('bueno')", number=1000000, setup="from __main__ import encode4"))
    print(timeit.timeit("encode5('bueno')", number=1000000, setup="from __main__ import encode5"))
    print(timeit.timeit("encode6('bueno')", number=1000000, setup="from __main__ import encode6"))

    print(f"{encode('trabajo')=}")
    print(f"{encode2('trabajo')=}")
    print(f"{encode3('trabajo')=}")
    print(f"{encode4('trabajo')=}")
    print(f"{encode5('trabajo')=}")
    print(f"{encode6('trabajo')=}")
