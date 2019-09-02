#  Problem: Given a node, return the length of the linked list
#
# Examples:
# Input: 1 ; Return: 1
# Input 1->2->3 ; Return 3
#
class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def getLength(node):
        length = 0
        while (node != None):
            length += 1
            node = node.next

        return length

class ListNodeLength:
    if __name__ == '__main__':
        n0 = ListNode(0)
        print(str(getLength(n0) == 1) + '\n')

        n1 = ListNode(1)
        n2 = ListNode(2)
        n1.next = n2
        print(str(getLength(n1) == 2) + '\n')
