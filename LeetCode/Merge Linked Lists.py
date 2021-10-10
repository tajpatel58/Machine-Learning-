
#%% 
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)
    
def merge_linked_lists(l1, l2):
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    else:
        list_1_pointer = l1
        list_2_pointer = l2
        sorted_pointer = head = ListNode()
        if l1.val <= l2.val:
            head.val = l1.val
            list_1_pointer = l1.next
        else:
            head.val = l2.val
            list_2_pointer = l2.next
    while list_1_pointer != None or list_2_pointer != None:
        #sorted_pointer = sorted_pointer.next 
        if list_1_pointer == None:
            sorted_pointer.next = list_2_pointer
            list_2_pointer = list_2_pointer.next
        elif list_2_pointer == None:
            sorted_pointer.next = list_1_pointer
            list_1_pointer = list_1_pointer.next
        else:
            val_1 = list_1_pointer.val
            val_2 = list_2_pointer.val
            if val_1 <= val_2:
                sorted_pointer.next = list_1_pointer
                list_1_pointer = list_1_pointer.next
            else:
                sorted_pointer.next = list_2_pointer
                list_2_pointer = list_2_pointer.next
        sorted_pointer = sorted_pointer.next
    return head


node_9 = ListNode(val=9)
node_7 = ListNode(val=7, next=node_9)
node_5 = ListNode(val=5, next=node_7)

node_10 = ListNode(val=10)
node_8 = ListNode(val=8, next=node_10)
node_6 = ListNode(val=6, next=node_8)

print(merge_linked_lists(node_5, node_6).next.next.next.next.next)


# %%
