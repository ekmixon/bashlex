def single_quote(s):
    if s[0] == "'" and len(s) == 1:
        return "\\'"

    l = ["'"]

    for c in s:
        l.append(c)
        if c == "'":
            l.extend(["\\''"])

    l.append("'")

    return ''.join(l)

def double_quote(s):
    return s

def legal_number(s):
    try:
        x = int(s)
        return True
    except ValueError:
        return False

def legal_identifier(name):
    pass

def removequotes(s, heredoc=False, doublequotes=False):
    r = ''
    sindex = 0
    dquote = False
    while sindex < len(s):
        c = s[sindex]
        if (
            c != '\\'
            and c == "'"
            and ((heredoc and doublequotes) or dquote)
            or c not in ['\\', "'", '"']
        ):
            r += c
            sindex += 1
        elif c != '\\' and c == "'":
            t = s.find("'", sindex + 1)
            if t == -1:
                t = len(s)
            else:
                t += 1

            r += s[sindex + 1:t-1]
            sindex = t
        elif c == '\\':
            sindex += 1
            if sindex == len(s):
                r += '\\'
                return r
            c = s[sindex]
            if ((heredoc and doublequotes) or dquote) and not _shellquote(c):
                r += '\\'
            r += c
        else:
            dquote = not dquote
            sindex += 1
    return r
