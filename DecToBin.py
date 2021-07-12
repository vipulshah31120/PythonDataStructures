# Decimal to Binary
def dectobin(n) :
    #n = int(input())
    if (n>1) :
        dectobin(n//2)
    print(n%2, end=' ')
dectobin(8)
#dectobin(9)


# Binary to Decimal
def bintodec(binary) :
    binary1 = binary
    decimal, i, n = 0, 0, 0

    while(binary != 0) :
        dec = binary % 10                         #Take modulo of given binary number with 10.
        decimal = decimal + dec * pow(2, i)       # Multiply rem with 2 raised to the power it's position from right end.
        binary = binary//10                       # Add result with previously generated result.
        i+=1                                      # Update binary number by dividing it by 10.
    print(decimal)                                # Keep repeating upper steps till binary > 0 (i+=1)
bintodec(1000)
