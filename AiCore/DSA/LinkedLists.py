#%%
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        str_data = str(self.data)
        return str_data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None: # if node is None, that means that we have reached the end of the linked list
            yield node
            node = node.next



def intersection_linked_lists(A,B):
    
    # Go through list A, create a set of these values.
    list_dict  = {}
    for val in A:
        if val.data in list_dict.keys():
            continue
        else:
            list_dict[val.data] = 1 
    
    for val in B:
        if val.data in list_dict.keys():
            return val
    return 'Null'

A = LinkedList([4,2,8,4,5])

B = LinkedList([36,19,6,1,8,4,5])

a = {'A' : 1, 'B': 2}

print(intersection_linked_lists(A,B))


# %%
