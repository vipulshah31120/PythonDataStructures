def addzeroes(strr, n) :
    for i in range(n) :
        strr += '0' + strr
    return strr

def getXOR(a, b) :
    alen = len(a)
    blen = len(b)

    if (alen > blen) :
        b = addzeroes(b, alen - blen)
    elif (blen > alen) :
        a = addzeroes(a, blen - alen)

    len = max(alen, blen)

    res = ''
    for i in range(len) :
        if (a[i] == b[i]) :
            res += '0'
        else :
            res += '1'
    return res




