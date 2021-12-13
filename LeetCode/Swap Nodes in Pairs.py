

#%% 
#Definition for singly-linked list.
from typing import List, Literal


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_nodes(l1):
    if l1 == None:
        return None
    elif l1.next == None:
        return l1 
    else:
        head = ListNode(l1.next.val)
        head.next = new_list = ListNode(l1.val, next=None)
        try:
            first_node = l1.next.next
            first_val = first_node.val
            odd = 1 
            second_node = l1.next.next.next
            second_val = second_node.val
            odd = 0 
            new_list.next = ListNode(second_val, next=ListNode(first_val, next=None))
            new_list = new_list.next.next
            while second_node.next != None: 
                first_node = first_node.next.next
                first_val = first_node.val
                odd = 1 
                second_node = second_node.next.next
                second_val = second_node.val
                odd = 0
                new_list.next = ListNode(second_val, next=ListNode(first_val, next=None))
                new_list = new_list.next.next
        except:
            pass
        if odd == 1:
            try:
                new_list.next = ListNode(first_val, next=None)
            except:
                pass

        return head

node_2_3 = ListNode(2)
node_2_2 = ListNode(2, next=node_2_3)
node_6 = ListNode(6, next=node_2_2)
node_4 = ListNode(4, next=node_6)
node_3 = ListNode(val=3, next=node_4)
node_5 = ListNode(val=5, next=node_3)
easy_list = ListNode(2, next=node_5)

swapped = swap_nodes(easy_list)

    
    


# %%


# %%
