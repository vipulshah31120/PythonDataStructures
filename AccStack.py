n = int(input())
a = list(map(int,input().split(None, n)[:n]))

print(n)
for i in a :
    if i == 0 :
        a.remove(i)
        a.append(i)

print(a)
