def isMatch(self, s: str, p: str) -> bool:
    if s == p:
        return True
    else:
        for i in range(len(s)):
            if s[i] != p[i] and p[i].isalpha:
                return False
            if p[i] == '.':
                p = list(p)
                p[i] = s[i]
                p = "".join(p)
            if p[i] == '*':



    return True

