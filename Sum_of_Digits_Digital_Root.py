def digital_root(n):
    n = str(n)
    result = 0
    if len(n) > 1:
        for i in n:
            result += int(i)
    if len(str(result)) > 1:
        return digital_root(result)
    return result
