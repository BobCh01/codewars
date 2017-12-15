def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    n = str(n)
    result = 0
    while True:
        n = str(n)
        if n != n[::-1]:
            result += 1
            n_1 = int(n)
            n_2 = int(n[::-1])
            n_3 = n_1 + n_2
            n = n_3
            continue
        else:
            break
    return result

