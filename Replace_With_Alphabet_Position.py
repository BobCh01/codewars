import string


def alphabet_position(text):
    alphabet = list(string.ascii_lowercase)
    alph_value = list(range(1, len(alphabet) + 1))
    text = text.replace("", " ").lower().split()
    result = []
    try:
        for t in text:
            for i, n in enumerate(alphabet):
                if (t == n):
                    if (t in alphabet):
                        result.append(str(alph_value[i]))
    except IndexError:
        return "Test is wrong!"
    return " ".join(result)
