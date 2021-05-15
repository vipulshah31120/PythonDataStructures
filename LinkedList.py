class Node :                                    #Represents individual elements
    def __init__(self, data = None, next = None) :
        self.data = data
        self.next = next                        #Pointer to the next element


class LinkedList :
    def __init__(self, head = None):
        self.head = None                        #Points to the head of the variable

    def insert_at_begining(self, data) :        #Inserts value at begining
        node  = Node(data, self.head)
        self.head = node                        #After insertion the head becomes node

    def print(self) :
        if self.head is None :
            print('LinkedList is Empty.')
            return

        itr = self.head                         #Assign head to the iterator
        llstr = ' '
        while itr :
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data) :
        if self.head is None :
            self.head = Node(data, None)
            return

        itr = self.head                         #If at the end it is not empty
        while itr.next :
            itr = itr.next

        itr.next = Node(data, None)             #If the last element is NULL


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(4)                    #Step-1 -> 4, 571, 28
    ll.insert_at_begining(571)
    ll.insert_at_begining(28)
    ll.insert_at_end(90)                        #Step-2 -> 90
    ll.print()

