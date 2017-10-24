import string


def find_missing_letter(chars):
    all = string.ascii_letters

    for n in range(len(all)+1):
        if (all[n] in chars):
            if not (all[n+1] in chars):
                return all[n+1]
