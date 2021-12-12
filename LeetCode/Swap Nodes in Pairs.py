

#%% 
#Definition for singly-linked list.
from typing import List, Literal


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_nodes(l1):
    if l1 == []:
        return []
    elif l1.next == None:
        return l1 
    else:
        head = l1.next.val
        head.next = new_list = ListNode(l1.val, next=None)
        try:
            first_node = l1.next.next
            second_node = l1.next.next.next
            first_val = first_node.val
            second_val = second_node.val
            while second_node.next != None: 
                new_list.next = ListNode(second_val, next=ListNode(first_val, next=None))
                first_node = first_node.next.next
                second_node = second_node.next.next
                first_val = first_node.val
                second_val = second_node.val

        return head


node_4 = ListNode(4)
node_3 = ListNode(val=3, next=node_4)
node_2 = ListNode(val=2, next=node_3)
easy_list = ListNode(1, next=node_2)

swapped = swap_nodes(easy_list)
# print(swapped.next.next)

    
    


# %%


# %%
