def rle(string):
    code = []
    count = 1
    for i in range(1, len(string)+1):
        if i < len(string) and string[i] == string[i-1]:
            count += 1
        else:
            if count <= 2:
                code.append(string[i-1] * count)
            else:
                code.append(str(count) + string[i-1])
            count = 1
    return ''.join(code)


gene = 'AAAAAAAATATTTCGCTTTTCAAAAATTGTCAGATGAGAGAAAAAATAAAA'
print(rle(gene))

