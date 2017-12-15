
def find_missing_numbers(arr):
    result = []
    try:
        n = list(range(arr[0], arr[-1]))
    except IndexError:
        return result
    if len(arr) > 1:
        for i in n:
            if i not in arr:
                result.append(i)
        return result
    else:
        return result
