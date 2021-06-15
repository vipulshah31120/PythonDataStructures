a = input()

for i in a :
    ans = 0
    p = ord(i) + 3
    if p > 122 :
        p = p - 26
        ans += (chr(p))
    print(ans)