inputstr = 'Vipul Shah'
res = ''

for i in range(len(inputstr)-1, -1, -1) :
    res = res + inputstr[i]

print(res)

#----------------------------------------------------------------------------------------------------------

inpustr1 = 'Rohini Delhi'

reverse1 = reversed(inpustr1)
print(''.join(reverse1))

#------------------------------------------------------------------------------------------------------------

inputstr2 = 'GTBIT'
print(inputstr2[-1 : : -1])
print(inputstr2[-1 : 0 : -1])
print(inputstr2[-1 : 1 : -1])

#-----------------------------------------------------------------------------------------------------------

inputstr3 = 'My name is Vipul Shah'

A = inputstr3.split(' ')
B = A[-1::-1]

print(A)
print(B)
print(' '.join(B))

#-----------------------------------------------------------------------------------------------------------

# Python3 code to reverse a string

# Reverse the string
def RevString(s, l):


# Check if number of words is even
    if l % 2 == 0:

    # Find the middle word
        j = int(l / 2)

    # Starting from the middle
    # start swapping words
    # at jth position and l-1-j position
        while (j <= l - 1):
            s[j], s[l - j - 1] = s[l - j - 1], s[j]
        j += 1

# Check if number of words is odd
    else:

    # Find the middle word
        j = int(l / 2 + 1)

    # Starting from the middle
    # start swapping the words
    # at jth position and l-1-j position
        while (j <= l - 1):
         s[j], s[l - 1 - j] = s[l - j - 1], s[j]
        j += 1

    # return the reversed sentence
        return s;

# Driver Code
s = 'getting good at coding needs a lot of practice'
string = s.split(' ')
string = RevString(string, len(string))
print(" ".join(string))