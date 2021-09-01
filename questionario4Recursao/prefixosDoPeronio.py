def peronio(string1, string2):
    if len(string1) == 0 or len(string2) == 0 or string1[0] != string2[0]:
        return 1
    else:
        return 1+peronio(string1[1:], string2[1:])

print(peronio('hidro', 'hidroeletrica'))