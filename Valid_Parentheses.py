def valid_parentheses(s):
    # your code here
    check = 0
    for i in s:
        if i == "(":
            check += 1
        elif i == ")":
            check -= 1
            if check < 0:
                return False

    if check == 0:
        return True
    else:
        return False
