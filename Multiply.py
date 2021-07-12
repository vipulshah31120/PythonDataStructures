# To print the table of a number and give the sum of all the values
def Multiply(n) :
    n = int(input())
    sum = 0
    for i in range(1, 11) :
        print(n, '*', i, '=', n*i)
        sum += n*i
    print('Sum: ', sum)
Multiply(int)                           # 'int' is used for the positional argument. If we haave an user input
                                        # we use the 'type' of the arugument which is an integer