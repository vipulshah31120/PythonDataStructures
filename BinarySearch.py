#Using Linear Search
def linear_search(number_list, number_to_find) :
    for index , element in enumerate(number_list) :
        if element == number_to_find :
            return index
    return -1
def binary_search(number_list, number_to_find) :
    pass

if __name__ == '__main__':
    number_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 45

    index = linear_search(number_list, number_to_find)
    print(f'Number found at index {index} using linear search')