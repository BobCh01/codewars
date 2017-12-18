def format_duration(s):
    txt = ""
    year = 0
    day = 0
    hour = 0
    minute = 0
    seconds = s

    if s >= 31536000:
        year = s / 31536000
        seconds = s - (int(year) * 31536000)

        if year > 1:
            txt = "{} years".format(int(year))
        else:
            txt = "{} year".format(int(year))

    if seconds >= 86400:
        day = seconds / 86400
        seconds -= (int(day) * 86400)

        if len(txt) == 0:
            if day > 1:
                txt += "{} days".format(int(day))
            else:
                txt += "{} day".format(int(day))
        else:
            if day > 1:
                txt += " {} days".format(int(day))
            else:
                txt += " {} day".format(int(day))

    if seconds >= 3600:
        hour = seconds / 3600
        seconds -= (int(hour) * 3600)

        if len(txt) == 0:
            if hour > 1:
                txt += "{} hours".format(int(hour))
            else:
                txt += "{} hour".format(int(hour))
        else:
            if hour > 1:
                txt += " {} hours".format(int(hour))
            else:
                txt += " {} hour".format(int(hour))

    if seconds >= 60:
        minute = seconds / 60
        seconds -= (int(minute) * 60)

        if len(txt) == 0:
            if minute > 1:
                txt += "{} minutes".format(int(minute))
            else:
                txt += "{} minute".format(int(minute))
        else:
            if minute > 1:
                txt += " {} minutes".format(int(minute))
            else:
                txt += " {} minute".format(int(minute))

    if 0 < seconds < 60:
        if len(txt) == 0:

            if seconds > 1:
                txt += "{} seconds".format(int(seconds))
            else:
                txt += "{} second".format(int(seconds))
        else:
            if seconds > 1:
                txt += " {} seconds".format(int(seconds))
            else:
                txt += " {} second".format(int(seconds))
    if not txt:
        txt = "now"

    txt = txt.split(" ")
    result = ""
    if len(txt) >= 4:

        f = ","
        a = " and"
        for j, i in enumerate(txt):
            if j == 0:
                result += i
            else:
                result += " " + i
                if j % 2 == 1 and i != txt[-1] and i != txt[-3]:
                    result += f
                if i == txt[-3]:
                    result += a
    else:
        result = " ".join(txt)

    return result
