def solution(s, n):
    
    s = list(s)
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 122:
            if 97 <= ord(s[i]) and ord(s[i]) + n > 122:
                s[i] = chr(ord(s[i]) + n - 26)
            elif 65 <= ord(s[i]) <= 90 and ord(s[i]) + n > 90:
                s[i] = chr(ord(s[i]) + n - 26)
            else:
                s[i] = chr(ord(s[i]) + n)
                
    return "".join(s)