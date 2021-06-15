def name(s) :
    l = s.split()                        # split the string into a list
    new = ''                             # storing the splitted words in new

    for i in range(len(l) - 1) :
        s = l[i]                            # l[-1] gives last item of list l. We
        new += (s[0].upper()+'.')               # adds the capital first character
    new += l[-1].title()                        # We use title to print first character in Capital

    return new
s ="mohandas karamchand gandhi"
print(name(s))

