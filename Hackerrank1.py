import textwrap
def wrap(string, max_width) :
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)
