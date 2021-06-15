s = input('Enter the password: ')

def password(s) :
    if (len(s) >= 4):
        return 1

    if (str.isdigit(s)) :
        return 1

    if (str.isupper(s)) :
        return 1

    if (str.isspace(s)) :
        return 0

    if (str.isalpha(s)) :
        return 1

    else :
        print('Invalid')

print(password(s))

