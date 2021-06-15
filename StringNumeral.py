str = input()

alpha = ''
num = ''
let = ''

for i in range(len(str)) :
    if ((str[i]) >= 'A' and str[i] <= 'Z' or
        (str[i] >= 'a' and str[i] <= 'z')) :

        alpha+= str[i]

    elif (str[i].isdigit()) :
        num += str[i]

    else :
        let += str[i]

print(alpha)
print(num)
print(let)